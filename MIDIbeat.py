import os
import sys
import itertools
import mido
import json
import copy
import MIDIbeat_utility_functions as uf
import MIDIbeat_settings as s
import tkinter as tk

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

        master.bind('<Return>', self.execute)
        master.bind('<Escape>', self.close)

        self.button = tk.Button(master, text='Execute')
        self.button.bind('<Button-1>', self.execute)
        self.button.pack()

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
        self.MidiReader()
    #UI code end

    def MidiReader(self):
        beatmap = copy.deepcopy(settings.map)
        currenttick = 0
        mid = mido.MidiFile(settings.path + "beatsaber.mid")
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
                        if note in range(89, 93): #if note is obstacle
                            obstacle_ontime = currentbeat
                            midinote = [item[0] for item in s.obstacle_tuple if msg.note == item[1]]
                            toJSONobstacle = midinote[0]
                            print("NOTEON: " + "#" + str(note) + " (" + midinote[0] + ")") #debug
                            #print("#" + str(note) + " ch:" + str(channel))
                        
                        elif note in range(96, 119):
                            midinote = [item[0] for item in s.note_favorites if msg.note == item[1]]
                            if msg.channel == 9: #really channel 10 (there is no midi channel 0) TODO fix
                                toJSONnote = midinote[0]
                                print("NOTEON: " + "#" + str(note) + " ch:" + str(channel) + " (" + midinote[0] + ")") #debug
                            else:
                                midichannel = [item[0] for item in s.cut_directions if msg.channel == item[1]]
                                toJSONnote = midinote[0] + "-" + midichannel[0]
                                print("NOTEON: " + "#" + str(note) + " ch:" + str(channel) + " (" + midinote[0] + midichannel[0] + ")") #debug
                            toJSONtime = currentbeat                          
                            #print("#" + str(note) + " ch:" + str(channel))
                            beatmap["_notes"].append(self.NoteToJSON(toJSONnote, toJSONtime))
                            
                        else:
                            midinote = [item[0] for item in s.input_tuple if msg.note == item[1]]
                            midichannel = [item[0] for item in s.cut_directions if msg.channel == item[1]]
                            toJSONnote = midinote[0] + "-" + midichannel[0]
                            toJSONtime = currentbeat
                            print("NOTEON: " + "#" + str(note) + " ch:" + str(channel) + " (" + midinote[0] + "-" + midichannel[0] + ")") #debug
                            #print("#" + str(note) + " ch:" + str(channel))
                            beatmap["_notes"].append(self.NoteToJSON(toJSONnote, toJSONtime))

                    elif msg.type == "note_off" or msg.type == "note_on" and msg.velocity == 0:
                        currenttick += msg.time
                        currentbeat = currenttick / ticks_per_beat
                        note = msg.note
                        if note in range(89, 93):
                            obstacleduration = currentbeat - obstacle_ontime
                            beatmap["_obstacles"].append(self.ObstacleToJSON(toJSONobstacle, obstacle_ontime, obstacleduration))
                            midinote = [item[0] for item in s.obstacle_tuple if msg.note == item[1]]
                            print("NOTEOFF: " + "#" + str(note) + " ch:" + str(channel) + " (" + midinote[0] + ")") #debug
                        else:
                            midinote = [item[0] for item in s.input_tuple if msg.note == item[1]]
                            midichannel = [item[0] for item in s.cut_directions if msg.channel == item[1]]
                            print("NOTEOFF: " + "#" + str(note) + " ch:" + str(channel) + " (" + midinote[0] + ")") #debug                   

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
                        if note in range(96, 119):
                            midinote = [item[0] for item in s.event_favorites if msg.note == item[1]]
                            if msg.channel == 9:
                                toJSONevent = midinote[0]
                                print("NOTEON: " + "#" + str(note) + " ch:" + str(channel) + " (" + midinote[0] + ")") #debug
                                beatmap["_events"].append(self.EventToJSON(toJSONevent, toJSONtime))
                            else:
                                if midinote[1] == 12 or midinote[1] == 13: 
                                    midichannel = [item[0] for item in s.lighting_rotationvalues if msg.channel == item[1]]
                                else:
                                    midichannel = [item[0] for item in s.lighting_lightvalues if msg.channel == item[1]]
                                toJSONevent = midinote[0] + "-" + midichannel[0]
                                print("NOTEON: " + "#" + str(note) + " ch:" + str(channel) + " (" + midinote[0] + midichannel[0] + ")") #debug
                                beatmap["_events"].append(self.EventToJSON(toJSONevent, toJSONtime))
                        else:                      
                            midinote = [item[0] for item in s.lighting_tuple if msg.note == item[1]]
                            if midinote[1] == 12 or midinote[1] == 13: 
                                midichannel = [item[0] for item in s.lighting_rotationvalues if msg.channel == item[1]]
                            else:
                                midichannel = [item[0] for item in s.lighting_lightvalues if msg.channel == item[1]]
                            toJSONevent = midinote[0] + "-" + midichannel[0]                        
                            print("NOTEON: " + "#" + str(note) + " ch:" + str(channel) + " (" + midinote[0] + "-" + midichannel[0] + ")") #debug
                            #print("#" + str(note) + " ch:" + str(channel))                 
                            beatmap["_events"].append(self.EventToJSON(toJSONevent, toJSONtime))
                      
                    elif msg.type == "note_off" or msg.type == "note_on" and msg.velocity == 0:
                        if note in range(96, 119):
                            currenttick += msg.time
                            currentbeat = currenttick / ticks_per_beat
                            note = msg.note
                            midinote = [item[0] for item in s.event_favorites if msg.note == item[1]]
                            if msg.channel == 9:
                                toJSONnote = midinote[0]
                                print("NOTEOFF: " + "#" + str(note) + " ch:" + str(channel) + " (" + midinote[0] + ")") #debug
                            else:
                                if midinote[1] == 12 or midinote[1] == 13: 
                                    midichannel = [item[0] for item in s.lighting_rotationvalues if msg.channel == item[1]]
                                else:
                                    midichannel = [item[0] for item in s.lighting_lightvalues if msg.channel == item[1]]
                                toJSONnote = midinote[0] + "-" + midichannel[0]
                                print("NOTEOFF: " + "#" + str(note) + " ch:" + str(channel) + " (" + midinote[0] + midichannel[0] + ")") #debug
                        else:
                            midinote = [item[0] for item in s.lighting_tuple if msg.note == item[1]]
                            if midinote[1] == 12 or midinote[1] == 13: 
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
            

    def NoteToJSON(self, inputnote, time):
        outputnote = copy.deepcopy(s.note)
        inputnote = inputnote.split("-")
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
