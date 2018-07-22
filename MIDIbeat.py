import os
import sys
import itertools
import mido
import json
import copy
import MIDIbeat_utility_functions as uf
import MIDIbeat_settings as s
import tkinter as tk
from operator import itemgetter

class MIDIbeat:
    #UI code
    def __init__(self, master):

        self.master = master
        master.geometry("800x400")
        self.center(self.master)
        tk.Label(master, text="MIDIbeat")

        e1 = tk.Entry(master)
        e1.pack()
        e1.focus_set()

        master.bind('<Return>', self.CreateReaperNoteNamesFile)
        master.bind('<Escape>', self.close)

        self.button = tk.Button(master, text='MIDI to .json')
        self.button.bind('<Button-1>', self.execute)
        self.button2 = tk.Button(master, text='Create Reaper note names file')
        self.button2.bind('<Button-1>', self.CreateReaperNoteNamesFile)
        self.button3 = tk.Button(master, text='Create visualization effect favorites file')
        self.button3.bind('<Button-1>', self.CreateVisualizationFavoritesFile)
        self.button4 = tk.Button(master, text='JSON to MIDI')
        self.button4.bind('<Button-1>', self.CreateMIDIFromJSON)
        self.button.pack()
        self.button2.pack()
        self.button3.pack()
        self.button4.pack()
    
    def close(self, event):
        self.master.withdraw() # if you want to bring it back
        sys.exit() # if you want to exit the entire thing

    def center(self, toplevel):
        toplevel.update_idletasks()
        w = toplevel.winfo_screenwidth()
        h = toplevel.winfo_screenheight()
        size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

    def execute(self, event):
        self.CreateJSONFromMIDI()

    def CreateReaperNoteNamesFile(self, event):
        uf.CreateReaperNotenamesFile()

    def CreateVisualizationFavoritesFile(self, event):
        uf.CreateVisualizationFavoritesFile()

    #UI code end
   

    def CreateJSONFromMIDI(self):
        beatmap = copy.deepcopy(s.map)
        currenttick = 0
        mid = mido.MidiFile(s.path + s.midifile)
        ticks_per_beat = mid.ticks_per_beat
        for i, track in enumerate(mid.tracks):
            print('Track {}: {}'.format(i, track.name))
            if track.name == "Notes":
                for msg in track:
                    #print(msg)
                    if msg.is_meta:
                        if msg.type == "set_tempo":
                            print(msg)
                            print("set BPM")
                            bpm = mido.tempo2bpm(msg.tempo)
                            beatmap["_beatsPerMinute"] = bpm
                            tempo = msg.tempo
                    
                    if msg.type == "note_on" and msg.velocity != 0:
                        currenttick += msg.time
                        currentbeat = currenttick / ticks_per_beat
                        note = msg.note
                        channel = msg.channel
                        if note in range(89, 94): #if note is obstacle
                            obstacle_ontime = currentbeat
                            midinote = [item[0] for item in s.obstacle_tuple if msg.note == item[1]]
                            toJSONobstacle = midinote[0]
                            print("NOTEON: " + "#" + str(note) + " (" + midinote[0] + ")") #debug
                            #print("#" + str(note) + " ch:" + str(channel))
                        
                        elif note in range(96, 120):
                            midinote = [item[0] for item in s.note_favorites if msg.note == item[1]]
                            if msg.channel == 9: #really channel 10 (there is no midi channel 0) TODO fix
                                toJSONnote = midinote[0]
                                print("NOTEON: " + "#" + str(note) + " ch:" + str(channel) + " (" + midinote[0] + ")") #debug
                                toJSONtime = currentbeat                          
                                beatmap["_notes"].append(self.NoteToJSON(toJSONnote, toJSONtime, False))                                

                            elif msg.channel == 10: #really channel 11 (there is no midi channel 0) TODO fix
                                toJSONnote = midinote[0]
                                print("NOTEON: " + "#" + str(note) + " ch:" + str(channel) + " (" + midinote[0] + ")") #debug   
                                toJSONtime = currentbeat                          
                                beatmap["_notes"].append(self.NoteToJSON(toJSONnote, toJSONtime, True))  
                                                       
                            else:
                                midichannel = [item[0] for item in s.cut_directions if msg.channel == item[1]]
                                toJSONnote = midinote[0] + "-" + midichannel[0]
                                print("NOTEON: " + "#" + str(note) + " ch:" + str(channel) + " (" + midinote[0] + midichannel[0] + ")") #debug
                                toJSONtime = currentbeat                          
                                beatmap["_notes"].append(self.NoteToJSON(toJSONnote, toJSONtime, False))  

                            
                        else:
                            midinote = [item[0] for item in s.input_tuple if msg.note == item[1]]
                            midichannel = [item[0] for item in s.cut_directions if msg.channel == item[1]]
                            toJSONnote = midinote[0] + "-" + midichannel[0]
                            toJSONtime = currentbeat
                            print("NOTEON: " + "#" + str(note) + " ch:" + str(channel) + " (" + midinote[0] + "-" + midichannel[0] + ")") #debug
                            #print("#" + str(note) + " ch:" + str(channel))
                            beatmap["_notes"].append(self.NoteToJSON(toJSONnote, toJSONtime, False))

                    elif msg.type == "note_off" or msg.type == "note_on" and msg.velocity == 0:
                        currenttick += msg.time
                        currentbeat = currenttick / ticks_per_beat
                        note = msg.note
                        if note in range(89, 94):
                            obstacleduration = currentbeat - obstacle_ontime
                            beatmap["_obstacles"].append(self.ObstacleToJSON(toJSONobstacle, obstacle_ontime, obstacleduration))
                            midinote = [item[0] for item in s.obstacle_tuple if msg.note == item[1]]
                            print("NOTEOFF: " + "#" + str(note) + " ch:" + str(channel) + " (" + midinote[0] + ")") #debug
                        else:
                            if msg.channel == 9:
                                midinote = [item[0] for item in s.note_favorites if msg.note == item[1]]
                                print("NOTEOFF: " + "#" + str(note) + " ch:" + " (" + midinote[0] + ")") #debug  
                            elif msg.channel == 10:
                                print("NOTEOFF: " + "#" + str(note) + " ch:" + " (MINE)") #debug  
                            else:
                                midinote = [item[0] for item in s.input_tuple if msg.note == item[1]]
                                midichannel = [item[0] for item in s.cut_directions if msg.channel == item[1]]
                                print("NOTEOFF: " + "#" + str(note) + " ch:" + str(midichannel) + " (" + midinote[0] + ")") #debug                   

            elif track.name == "Events":
                print("events here")
                currenttick = 0
                currentbeat = 0
                for msg in track:
                    #print(msg)
                    if msg.is_meta:
                        if msg.type == "set_tempo":
                            print(msg)
                            bpm = mido.tempo2bpm(msg.tempo)
                            beatmap["_beatsPerMinute"] = bpm
                            tempo = msg.tempo
                    
                    if msg.type == "note_on" and msg.velocity != 0:
                        note = msg.note
                        channel = msg.channel
                        currenttick += msg.time
                        currentbeat = currenttick / ticks_per_beat
                        toJSONtime = currentbeat
                        if note in range(96, 120):
                            midinote = [item[0] for item in s.event_favorites if msg.note == item[1]]
                            print(midinote)
                            if msg.channel == 9:
                                toJSONevent = midinote[0]
                                print("NOTEON: " + "#" + str(note) + " ch:" + str(channel) + " (" + midinote[0] + ")") #debug
                                beatmap["_events"].append(self.EventToJSON(toJSONevent, toJSONtime))
                            else:
                                print(midinote[0].split("-")[0])
                                if midinote[0].split("-")[0] in ["speed_speedlaserleft", "speed_speedlaserright"]:
                                    midichannel = [item[0] for item in s.lighting_rotationvalues if msg.channel == item[1]]
                                else:
                                    midichannel = [item[0] for item in s.lighting_lightvalues if msg.channel == item[1]]
                                toJSONevent = midinote[0] + "-" + midichannel[0]
                                print("NOTEON: " + "#" + str(note) + " ch:" + str(channel) + " (" + midinote[0] + midichannel[0] + ")") #debug
                                beatmap["_events"].append(self.EventToJSON(toJSONevent, toJSONtime))
                      
                    elif msg.type == "note_off" or msg.type == "note_on" and msg.velocity == 0:
                        if note in range(96, 120):
                            currenttick += msg.time
                            currentbeat = currenttick / ticks_per_beat
                            note = msg.note
                            midinote = [item[0] for item in s.event_favorites if msg.note == item[1]]
                            if msg.channel == 9:
                                toJSONnote = midinote[0]
                                print("NOTEOFF: " + "#" + str(note) + " ch:" + str(channel) + " (" + midinote[0] + ")") #debug
                            else:
                                if midinote[0].split("-")[0] in ["speed_speedlaserleft", "speed_speedlaserright"]:
                                    midichannel = [item[0] for item in s.lighting_rotationvalues if msg.channel == item[1]]
                                else:
                                    midichannel = [item[0] for item in s.lighting_lightvalues if msg.channel == item[1]]
                                toJSONnote = midinote[0] + "-" + midichannel[0]
                                print("NOTEOFF: " + "#" + str(note) + " ch:" + str(channel) + " (" + midinote[0] + midichannel[0] + ")") #debug
                        else:
                            midinote = [item[0] for item in s.lighting_tuple if msg.note == item[1]]
                            if midinote[0].split("-")[0] in ["speed_speedlaserleft", "speed_speedlaserright"]:
                                midichannel = [item[0] for item in s.lighting_rotationvalues if msg.channel == item[1]]
                            else:
                                midichannel = [item[0] for item in s.lighting_lightvalues if msg.channel == item[1]]
                            print("NOTEOFF: " + "#" + str(note) + " ch:" + str(channel) + " (" + midinote[0] + ")") #debug

            else:
                for msg in track:
                    #print(msg)
                    if msg.is_meta:
                        if msg.type == "set_tempo":
                            print(msg)
                            print("set BPM")
                            bpm = mido.tempo2bpm(msg.tempo)
                            beatmap["_beatsPerMinute"] = bpm
                            tempo = msg.tempo

        with open(s.outputpath + s.songname + "\\" + 'Expert.json', 'w') as outfile:
            json.dump(beatmap, outfile, indent=4)

        #InfoJSON values
        songname = s.songname
        subname = "subname"
        authorname = "authorname"
        environmentname = "BigMirrorEnvironment" #find rest of names
        coverimagepath = "cover.png"
        previewstart = 0
        previewduration = 12
        difficulty = "Expert"
        difficultyrank = 4
        audiopath = "beatsaber.ogg"
        jsonpath = "Export.json"
        infopath = "info.json"
        offset = 0
        oldoffset = 0
        difficultylevels = [
            # {"difficulty":"Expert","difficultyRank":4,"audioPath":"beatsaber.ogg","jsonPath":"Expert.json","offset":0,"oldOffset":0}]
            {"difficulty" : difficulty,
            "difficultyRank" : difficultyrank,
            "audioPath" : audiopath,
            "jsonPath" : jsonpath,
            "offset" : offset,
            "oldoffset" : 0 }
        ]
        infojson = copy.deepcopy(s.info)

        info = self.CreateInfoJSON(infojson, songname, subname, authorname, bpm, previewstart, previewduration, coverimagepath, environmentname, difficultylevels)

        with open(s.outputpath + s.songname + "\\" + infopath, "w") as infofile:
            json.dump(info, infofile, indent=4)

    def CreateInfoJSON(self, info, songname, songsubname, authorname, bpm, previewstart, previewduration, coverimagepath, environmentname, difficultylevels):
        info["songName"] = songname
        info["songSubName"] = songsubname
        info["authorName"] = authorname
        info["beatsPerMinute"] = bpm
        info["previewStartTime"] = previewstart
        info["previewDuration"] = previewduration
        info["coverImagePath"] = coverimagepath 
        info["environmentName"] = environmentname
        info["difficultyLevels"] = difficultylevels
        return info
        #{"difficulty":"Expert","difficultyRank":4,"audioPath":"beatsaber.ogg","jsonPath":"Expert.json","offset":0,"oldOffset":0}]
            
    def CreateMIDIFromJSON(self, event):
        with open(s.path + "OST\\SongLevelData_Breezer_Expert-resources.assets-231-MonoBehaviour.json") as f:
            data = json.load(f)
            bpm = data["_beatsPerMinute"]
            tempo = mido.bpm2tempo(bpm) 
            mid = mido.MidiFile(type=1, ticks_per_beat=480)
            midi_track = mido.MidiTrack()
            mid.tracks.append(midi_track)
            notes_track = mido.MidiTrack()
            mid.tracks.append(notes_track)
            obstacles_track = mido.MidiTrack()
            mid.tracks.append(obstacles_track)
            midi_track.append(mido.MetaMessage('time_signature', numerator=4, denominator=4, clocks_per_click=24, notated_32nd_notes_per_beat=8, time=0))
            midi_track.append(mido.MetaMessage('set_tempo', tempo=tempo))
            currenttick = 0
            notes = []
            obstacles = []
            events = []
            bps = bpm / 60
            for note in data["_notes"]:
                notes.append(note)
                #print(note)
            for obstacle in data["_obstacles"]:
                obstacles.append(obstacle)
            for event in data["_events"]:
                events.append(event)
            

            prevtime = 0
            noteofftime = 0
            ticks_per_beat = 480
            #currenttick += msg.time
            last_note = 0
            last_obstacle = 0
            last_channel = 0
            multiple_notes = False
            
            for note in notes:
                #print(note["_cutDirection"])
                notetimeinticks = int(mido.second2tick(note["_time"] / bps, 480, tempo))
                note_number, channel = self.JSONNoteToSaberSlash(note)
                notes_track.append(mido.Message('note_on', note=note_number, channel=channel, velocity=64, time=notetimeinticks-prevtime))              
                notes_track.append(mido.Message('note_off', note=last_note, channel=last_channel, velocity=0, time=0))         
                last_note = note_number
                last_channel = channel
                prevtime = notetimeinticks
                
            prevtime = 0
            duration = 0
            for obstacle in obstacles:
                notetimeinticks = int(mido.second2tick(obstacle["_time"] / bps, 480, tempo))
                obstacle_note_number = self.JSONNoteToObstacle(obstacle)
                obstacles_track.append(mido.Message('note_on', note=obstacle_note_number, velocity=64, time=notetimeinticks-prevtime-duration))              
                duration = int(mido.second2tick(obstacle["_duration"] / bps, 480, tempo))
                obstacles_track.append(mido.Message('note_off', note=obstacle_note_number, velocity=0, time=duration))         
                last_obstacle = obstacle_note_number
                prevtime = notetimeinticks 

            mid.tracks.append(mido.merge_tracks(mid.tracks))
            events_track = mido.MidiTrack()
            mid.tracks.append(events_track)

            last_event = 0
            prevtime = 0
            for event in events:
                eventtimeinticks = int(mido.second2tick(event["_time"] / bps, 480, tempo))
                event_number, channel = self.JSONNoteToEvent(event)
                events_track.append(mido.Message('note_on', note=event_number, channel=channel, velocity=64, time=eventtimeinticks-prevtime))              
                events_track.append(mido.Message('note_off', note=last_event, channel=last_channel, velocity=0, time=0))         
                last_event = event_number
                last_channel = channel
                prevtime = eventtimeinticks


            mid.tracks.remove(notes_track)
            mid.tracks.remove(obstacles_track)
            mid.save(s.path + 'new_song.mid')

    def JSONNoteToSaberSlash(self, inputnote):

        type = [item[0] for item in s.note_types if inputnote["_type"] == item[1]]
        line = [item[0] for item in s.line_indices if inputnote["_lineIndex"] == item[1]]
        layer = [item[0] for item in s.line_layers if inputnote["_lineLayer"] == item[1]]
        cutdirection = [item[0] for item in s.cut_directions if inputnote["_cutDirection"] == item[1]]

        notedetails =  type[0] + "-" + line[0] + "-" + layer[0] + "-" + cutdirection[0]
        favoritenote = [item[1] for item in s.note_favorites if notedetails == item[0]]
        #print(notedetails)
        if type[0] == "note_mine":
            notedetails = notedetails.split("-", 1)[1].rsplit("-", 1)[0]
            outputnote = [item[1] for item in s.note_favorites if notedetails == item[0].split("-", 1)[1].rsplit("-", 1)[0]]
            return(outputnote[0], 10)
        elif not favoritenote:
            notedetails =  type[0] + "-" + line[0] + "-" + layer[0]
            notfavoritenote = [item[1] for item in s.note_favorites if notedetails == item[0].rsplit("-", 1)[0]]
            if notfavoritenote:
                channel = [item[1] for item in s.cut_directions if cutdirection[0] == item[0]]
                return(notfavoritenote[0], channel[0])
                #print(str(notfavoritenote[0]) + "channel " + str(channel[0]) + " (not favorite")
        else:
            return(favoritenote[0], 9)

    def JSONNoteToObstacle(self, inputobstacle):
        type = [item[0] for item in s.obstacle_types if inputobstacle["_type"] == item[1]]
        line = [item[0] for item in s.obstacle_line_indices if inputobstacle["_lineIndex"] == item[1]]
        duration = [item[0] for item in s.obstacle_durations if inputobstacle["_duration"] == item[1]] #not implemented in MIDI yet
        width = [item[0] for item in s.obstacle_widths if inputobstacle["_width"] == item[1]]          #not implemented in MIDI yet

        notedetails =  type[0] + "-" + line[0] + "-" + duration[0] + "-" + width[0]
        print(notedetails)
        favoriteobstacle = [item[1] for item in s.obstacle_tuple if notedetails.rsplit("-", 2)[0] == item[0]]
        return(favoriteobstacle[0])

    def JSONNoteToEvent(self, inputevent):

        type = [item[0] for item in s.lighting_types if inputevent["_type"] == item[1]]
        if type[0] not in ["speed_speedlaserleft", "speed_speedlaserright"]: 
            value = [item[0] for item in s.lighting_lightvalues if inputevent["_value"] == item[1]]
        else:
            value = [item[0] for item in s.lighting_rotationvalues if inputevent["_value"] == item[1]]

        notedetails =  type[0] + "-" + value[0]
        print(notedetails)
        favoritenote = [item[1] for item in s.event_favorites if notedetails == item[0]]
        if not favoritenote:
            notedetails =  type[0]
            
            notfavoritenote = [item[1] for item in s.event_favorites if notedetails == item[0].rsplit("-", 1)[0]]
            if notfavoritenote:
                if type[0] in ["speed_speedlaserleft", "speed_speedlaserright"]: 
                    channel = [item[1] for item in s.lighting_rotationvalues if value[0] == item[0]]
                    return(notfavoritenote[0], channel[0])
                else:
                    channel = [item[1] for item in s.lighting_lightvalues if value[0] == item[0]]
                    return(notfavoritenote[0], channel[0])
        else:
            return(favoritenote[0], 9)


        
    def NoteToJSON(self, inputnote, time, mine):
        outputnote = copy.deepcopy(s.note)
        inputnote = inputnote.split("-")
        if mine:
            notetype = "note_mine"
        else:
            notetype = [item[1] for item in s.note_types if inputnote[0] == item[0]]
        lineindex = [item[1] for item in s.line_indices if inputnote[1] == item[0]]
        linelayer = [item[1] for item in s.line_layers if inputnote[2] == item[0]]
        cutdirection = [item[1] for item in s.cut_directions if inputnote[3] == item[0]]
        outputnote["_time"] = str(time)
        outputnote["_lineIndex"] = str(lineindex[0])
        outputnote["_lineLayer"] = str(linelayer[0])
        outputnote["_type"] = str(notetype[0])
        outputnote["_cutDirection"] = str(cutdirection[0])
        return(outputnote)

    def ObstacleToJSON(self, inputobstacle, time, duration):
        outputobstacle = copy.deepcopy(s.obstacle)
        inputobstacle = inputobstacle.split("-")
        obstacletype = [item[1] for item in s.obstacle_types if inputobstacle[0] == item[0]]
        if obstacletype == "obstacle_wall":
            obstaclelineindex = [item[1] for item in s.obstacle_line_indices if inputobstacle[1] == item[0]]
        else:
            obstaclelineindex = "0"
        outputobstacle["_time"] = str(time)
        outputobstacle["_lineIndex"] = str(obstaclelineindex[0])
        outputobstacle["_type"] = str(obstacletype[0])
        outputobstacle["_duration"] = duration
        outputobstacle["_width"] = 1 #default to 1 for now
        return(outputobstacle)

    def EventToJSON(self, inputevent, time):
        outputevent = copy.deepcopy(s.event)
        inputevent = inputevent.split("-")
        eventtype = [item[1] for item in s.lighting_types if inputevent[0] == item[0]]
        if eventtype[0] >= 12:
            eventvalue = [item[1] for item in s.lighting_rotationvalues if inputevent[1] == item[0]]
        else:    
            eventvalue = [item[1] for item in s.lighting_lightvalues if inputevent[1] == item[0]]
        outputevent["_time"] = time
        outputevent["_type"] = eventtype[0]
        outputevent["_value"] = eventvalue[0]
        return(outputevent)

#instance.RenameReaperOutput()
#utility_functions.CreateReaperNotenamesFile() # uncomment the start of this line to generate a notenames file for Reaper
#utility_functions.ParseJSON() # uncomment the start of this line to analyze .json files getting most common notes/obstacles/lighting (int, --n or --o or --l)

root = tk.Tk()
my_gui = MIDIbeat(root)
root.mainloop()
