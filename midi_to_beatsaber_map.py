import os
import itertools
import mido
import json
import copy
import preview_sample
import settings

class Beatsaber_Python:

    def MidiReader(self):
        beatmap = copy.deepcopy(settings.map)
        currenttick = 0
        mid = mido.MidiFile(settings.path + "beatsaber.mid")
        ticks_per_beat = mid.ticks_per_beat
        for i, track in enumerate(mid.tracks):
            print('Track {}: {}'.format(i, track.name))
            for msg in track:
                #print(msg)

                if msg.is_meta:
                    if msg.type == "set_tempo":
                        print(msg)
                        bpm = mido.tempo2bpm(msg.tempo)
                        beatmap["_beatsPerMinute"] = bpm
                        tempo = msg.tempo
                
                if msg.type == "note_on" and msg.velocity != 0:
                    currenttick += msg.time
                    currentbeat = currenttick / ticks_per_beat
                    note = msg.note
                    channel = msg.channel
                    if note in range(101, 106): #if note is obstacle
                        savednote = note
                        obstacle_ontime = currentbeat
                        midinote = [item[0] for item in settings.obstacle_tuple if msg.note == item[1]]
                        toJSONobstacle = midinote[0]
                        print("NOTEON: " + "#" + str(note) + " (" + midinote[0] + ")") #debug
                        #print("#" + str(note) + " ch:" + str(channel))
                        
                    else:
                        midinote = [item[0] for item in settings.input_tuple if msg.note == item[1]]
                        midichannel = [item[0] for item in settings.cut_directions if msg.channel == item[1]]
                        toJSONnote = midinote[0] + "-" + midichannel[0]
                        toJSONtime = currentbeat
                        print("NOTEON: " + "#" + str(note) + " ch:" + str(channel) + " (" + midinote[0] + "-" + midichannel[0] + ")") #debug
                        #print("#" + str(note) + " ch:" + str(channel))
                        beatmap["_notes"].append(self.NoteToJSON(toJSONnote, toJSONtime))

                elif msg.type == "note_off" or msg.type == "note_on" and msg.velocity == 0:
                    currenttick += msg.time
                    currentbeat = currenttick / ticks_per_beat
                    note = msg.note
                    if note in range(101, 106):
                        obstacleduration = currentbeat - obstacle_ontime
                        beatmap["_obstacles"].append(self.ObstacleToJSON(toJSONobstacle, obstacle_ontime, obstacleduration))
                        midinote = [item[0] for item in settings.obstacle_tuple if msg.note == item[1]]
                        print("NOTEOFF: " + "#" + str(note) + " ch:" + str(channel) + " (" + midinote[0] + ")") #debug
                    else:
                        midinote = [item[0] for item in settings.input_tuple if msg.note == item[1]]
                        midichannel = [item[0] for item in settings.cut_directions if msg.channel == item[1]]
                        print("NOTEOFF: " + "#" + str(note) + " ch:" + str(channel) + " (" + midinote[0] + ")") #debug                   


        with open(settings.path + 'data.json', 'w') as outfile:
            json.dump(beatmap, outfile)

    def NoteToJSON(self, inputnote, time):
        outputnote = copy.deepcopy(settings.note)
        inputnote = inputnote.split("-")
        notetype = [item[1] for item in settings.note_types if inputnote[0] == item[0]]
        lineindex = [item[1] for item in settings.line_indices if inputnote[1] == item[0]]
        linelayer = [item[1] for item in settings.line_layers if inputnote[2] == item[0]]
        cutdirection = [item[1] for item in settings.cut_directions if inputnote[3] == item[0]]
        outputnote["_time"] = str(time)
        outputnote["_lineIndex"] = str(lineindex[0])
        outputnote["_lineLayer"] = str(linelayer[0])
        outputnote["_type"] = str(notetype[0])
        outputnote["_cutDirection"] = str(cutdirection[0])
        #print(inputnote)
        #print(outputnote)
        return(outputnote)

    def ObstacleToJSON(self, inputobstacle, time, duration):
        outputobstacle = copy.deepcopy(settings.obstacle)
        inputobstacle = inputobstacle.split("-")
        obstacletype = [item[1] for item in settings.obstacle_types if inputobstacle[0] == item[0]]
        if obstacletype == "obstacle_wall":
            obstaclelineindex = [item[1] for item in settings.obstacle_line_indices if inputobstacle[1] == item[0]]
        else:
            obstaclelineindex = "0"
        outputobstacle["_time"] = str(time)
        outputobstacle["_lineIndex"] = str(obstaclelineindex[0])
        outputobstacle["_type"] = str(obstacletype[0])
        outputobstacle["_duration"] = duration #default to 1 for now
        outputobstacle["_width"] = 1 #default to 1 for now
        #print(inputnote)
        #print(outputnote)
        return(outputobstacle)

instance = Beatsaber_Python()
#instance.RenameReaperOutput()
#instance.MidiReader()
preview_sample.CreateReaperNotenamesFile()
