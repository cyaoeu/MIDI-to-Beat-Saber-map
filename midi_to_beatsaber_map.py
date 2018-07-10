from pydub import AudioSegment
import time
import os
import itertools
import shutil
import mido
import json
import copy

class Beatsaber_Python:
    path = "C:\\beatsaber\\"
    ext = ".wav"

    notes = ["note_red", "note_blue", "note_mine"]
    lines = ["line_right", "line_middleright", "line_middleleft", "line_left"]
    layers = ["layer_bottom", "layer_middle", "layer_top"]
    cuts = ["cut_up", "cut_down", "cut_left", "cut_right", "cut_upleft", "cut_upright", "cut_downleft", "cut_downright", "cut_any"] 

    obstacles = ["obstacle_wall", "obstacle_ceiling"]
    obstaclelines = ["obstacleline_right", "obstacleline_middleright", "obstacleline_middleleft", "obstacleline_left"]

    input_tuple = [ #configure notes here
        #Red saber: default C6 (84) to D7 (98)
        ("note_red-line_right-layer_bottom", 84),
        ("note_red-line_right-layer_middle", 85),
        ("note_red-line_right-layer_top", 86),

        ("note_red-line_middleright-layer_bottom", 88),
        ("note_red-line_middleright-layer_middle", 89),
        ("note_red-line_middleright-layer_top", 90),

        ("note_red-line_middleleft-layer_bottom", 92),
        ("note_red-line_middleleft-layer_middle", 93),
        ("note_red-line_middleleft-layer_top", 94),

        ("note_red-line_middleleft-layer_bottom", 96),
        ("note_red-line_middleleft-layer_middle", 97),
        ("note_red-line_middleleft-layer_top", 98),

        #Blue saber: default C4 (60) to D5 (74)
        ("note_blue-line_right-layer_bottom", 60),
        ("note_blue-line_right-layer_middle", 61),
        ("note_blue-line_right-layer_top", 62),

        ("note_blue-line_middleright-layer_bottom", 64),
        ("note_blue-line_middleright-layer_middle", 65),
        ("note_blue-line_middleright-layer_top", 66),

        ("note_blue-line_middleleft-layer_bottom", 68),
        ("note_blue-line_middleleft-layer_middle", 69),
        ("note_blue-line_middleleft-layer_top", 70),

        ("note_blue-line_middleleft-layer_bottom", 72),
        ("note_blue-line_middleleft-layer_middle", 73),
        ("note_blue-line_middleleft-layer_top", 74),

        #Mines: default C2 (36) to D3 (50)
        ("note_mine-line_right-layer_bottom", 36),
        ("note_mine-line_right-layer_middle", 37),
        ("note_mine-line_right-layer_top", 38),

        ("note_mine-line_middleright-layer_bottom", 40),
        ("note_mine-line_middleright-layer_middle", 41),
        ("note_mine-line_middleright-layer_top", 42),

        ("note_mine-line_middleleft-layer_bottom", 44),
        ("note_mine-line_middleleft-layer_middle", 45),
        ("note_mine-line_middleleft-layer_top", 46),

        ("note_mine-line_middleleft-layer_bottom", 48),
        ("note_mine-line_middleleft-layer_middle", 49),
        ("note_mine-line_middleleft-layer_top", 50)
    ]

    cut_directions =  [
        ("cut_up", 0),
        ("cut_down", 1),
        ("cut_left", 2),
        ("cut_right", 3),
        ("cut_upleft", 4),
        ("cut_upright", 5),
        ("cut_downleft", 6), 
        ("cut_downright", 7), 
        ("cut_any", 8)
    ]

    note_types = [
        ("note_red", 0),
        ("note_blue", 1),
        ("note_mine", 3),
    ]

    line_indices = [
        ("line_left", 0),
        ("line_middleleft", 1),
        ("line_middleright", 2),
        ("line_right", 3)
    ]

    line_layers = [
        ("layer_bottom", 0),
        ("layer_middle", 1),
        ("layer_top", 2)
    ]


    #JSON (credits to ciwolsey)
    map = {
        "_version": "1.5.0",
        "_beatsPerMinute": 0,
        "_beatsPerBar": 8,
        "_noteJumpSpeed": 10,
        "_shuffle": 0,
        "_shufflePeriod": 0.5,
        "_events": [],
        "_notes": [],
        "_obstacles": []
    }

    note = {
        "_time": 0,
        "_lineIndex": 0,
        "_lineLayer": 0,
        "_type": 0,
        "_cutDirection": 8
    }

    obstacle = { #todo
        "_time": 0,
        "_lineIndex": 0,
        "_type": 0,
        "_duration": 0,
        "_width": 0
    }

    def RenderNoteWavs(self): #create samples from individual .wavs for preview purposes
        debugprint = []
        for note in self.notes:
            for line in self.lines:
                for layer in self.layers:
                    for cut in self.cuts:
                        debugprint.append(note)
                        debugprint.append(line)
                        debugprint.append(layer)
                        note_wav = AudioSegment.from_wav(self.path + note + self.ext)
                        line_wav = AudioSegment.from_wav(self.path + line + self.ext)
                        layer_wav = AudioSegment.from_wav(self.path + layer + self.ext)
                        if note == "note_mine":
                            print(debugprint)
                            finalwav = note_wav + line_wav + layer_wav
                            finalwav.export(self.path + "output\\" + note + "_" + line + "_" + layer + ".wav", format="wav")
                            debugprint = []
                            time.sleep(1)
                            break
                        else:
                            debugprint.append(cut)
                            layer_cut =  AudioSegment.from_wav(self.path + cut + self.ext)
                            finalwav = note_wav + line_wav + layer_wav + layer_cut
                            finalwav.export(self.path + "output\\" + note + "_" + line + "_" + layer + "_" + cut + ".wav", format="wav")
                            print(debugprint)
                            debugprint = []
                            time.sleep(1)

    def RenderObstacleWavs(self):
        debugprint = []
        for obstacle in self.obstacles:
            for line in self.obstaclelines:
                debugprint.append(obstacle)
                debugprint.append(line)
                obstacle_wav = AudioSegment.from_wav(self.path + obstacle + self.ext)
                
                if obstacle == "obstacle_ceiling":
                    print(debugprint)
                    finalwav = obstacle_wav
                    finalwav.export(self.path + "output\\" + obstacle + ".wav", format="wav")
                    debugprint = []
                    time.sleep(1)
                    break
                else:
                    debugprint.append(line)
                    line_wav = AudioSegment.from_wav(self.path + line + self.ext)
                    finalwav = obstacle_wav + line_wav
                    finalwav.export(self.path + "output\\" + obstacle + "_" + line + ".wav", format="wav")
                    print(debugprint)
                    debugprint = []
                    time.sleep(1)
    
    def RenameReaperOutput(self): #renames wavs exported as individual items   note: specific order!
        wavlist = [filename for filename in os.listdir(self.path) if filename.endswith(".wav")]
        combined_audio = self.notes + self.lines + self.layers + self.cuts + self.obstacles + self.obstaclelines
        for i, filename in enumerate(wavlist):
            shutil.move(self.path + filename, self.path + combined_audio[i] + self.ext)
            print(self.path + filename + " = " + self.path + combined_audio[i] + self.ext)

    def MidiReader(self):
        beatmap = copy.deepcopy(self.map)
        currenttick = 0
        mid = mido.MidiFile(self.path + "beatsaber.mid")
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

                if msg.type == "note_off":
                    currenttick += msg.time
                elif msg.type == "note_on":
                    currenttick += msg.time
                    currentbeat = currenttick / ticks_per_beat
                    note = msg.note
                    channel = msg.channel
                    #if note
                    midinote = [item[0] for item in self.input_tuple if msg.note == item[1]]
                    midichannel = [item[0] for item in self.cut_directions if msg.channel == item[1]]
                    toJSONnote = midinote[0] + "-" + midichannel[0]
                    toJSONtime = currentbeat
                    #print("#" + str(note) + " ch:" + str(channel) + " (" + midinote[0] + "-" + midichannel[0] + ")") #debug
                    #print("#" + str(note) + " ch:" + str(channel))
                    beatmap["_notes"].append(self.NoteToJSON(toJSONnote, toJSONtime))
        with open(self.path + 'data.json', 'w') as outfile:
            json.dump(beatmap, outfile)

    def NoteToJSON(self, inputnote, time):
        outputnote = copy.deepcopy(self.note)
        inputnote = inputnote.split("-")
        notetype = [item[1] for item in self.note_types if inputnote[0] == item[0]]
        lineindex = [item[1] for item in self.line_indices if inputnote[1] == item[0]]
        linelayer = [item[1] for item in self.line_layers if inputnote[2] == item[0]]
        cutdirection = [item[1] for item in self.cut_directions if inputnote[3] == item[0]]
        outputnote["_time"] = str(time)
        outputnote["_lineIndex"] = str(lineindex[0])
        outputnote["_lineLayer"] = str(linelayer[0])
        outputnote["_type"] = str(notetype[0])
        outputnote["_cutDirection"] = str(cutdirection[0])
        #print(inputnote)
        #print(outputnote)
        return(outputnote)

instance = Beatsaber_Python()
#instance.RenameReaperOutput()
instance.MidiReader()