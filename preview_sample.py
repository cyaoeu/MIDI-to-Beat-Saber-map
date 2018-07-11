from pydub import AudioSegment
import time
import shutil
import settings
import os
import sys
import json
import collections
from collections import Counter
import operator
import glob

def RenderNoteWavs(): #create samples from individual .wavs for preview purposes
    debugprint = []
    for note in settings.notes:
        for line in settings.lines:
            for layer in settings.layers:
                for cut in settings.cuts:
                    debugprint.append(note)
                    debugprint.append(line)
                    debugprint.append(layer)
                    note_wav = AudioSegment.from_wav(settings.path + note + settings.ext)
                    line_wav = AudioSegment.from_wav(settings.path + line + settings.ext)
                    layer_wav = AudioSegment.from_wav(settings.path + layer + settings.ext)
                    if note == "note_mine":
                        print(debugprint)
                        finalwav = note_wav + line_wav + layer_wav
                        finalwav.export(settings.path + "output\\" + note + "_" + line + "_" + layer + ".wav", format="wav")
                        debugprint = []
                        time.sleep(1)
                        break
                    else:
                        debugprint.append(cut)
                        layer_cut =  AudioSegment.from_wav(settings.path + cut + settings.ext)
                        finalwav = note_wav + line_wav + layer_wav + layer_cut
                        finalwav.export(settings.path + "output\\" + note + "_" + line + "_" + layer + "_" + cut + ".wav", format="wav")
                        print(debugprint)
                        debugprint = []
                        time.sleep(1)

def RenderObstacleWavs():
    debugprint = []
    for obstacle in settings.obstacles:
        for line in settings.obstaclelines:
            debugprint.append(obstacle)
            debugprint.append(line)
            obstacle_wav = AudioSegment.from_wav(settings.path + obstacle + settings.ext)
            
            if obstacle == "obstacle_ceiling":
                print(debugprint)
                finalwav = obstacle_wav
                finalwav.export(settings.path + "output\\" + obstacle + ".wav", format="wav")
                debugprint = []
                time.sleep(1)
                break
            else:
                debugprint.append(line)
                line_wav = AudioSegment.from_wav(settings.path + line + settings.ext)
                finalwav = obstacle_wav + line_wav
                finalwav.export(settings.path + "output\\" + obstacle + "_" + line + ".wav", format="wav")
                print(debugprint)
                debugprint = []
                time.sleep(1)

def RenameReaperOutput(): #renames wavs exported as individual items   note: specific order!
    wavlist = [filename for filename in os.listdir(settings.path) if filename.endswith(".wav")]
    combined_audio = settings.notes + settings.lines + settings.layers + settings.cuts + settings.obstacles + settings.obstaclelines
    for i, filename in enumerate(wavlist):
        shutil.move(settings.path + filename, settings.path + combined_audio[i] + settings.ext)
        print(settings.path + filename + " = " + settings.path + combined_audio[i] + settings.ext)

def CreateReaperNotenamesFile():
    keylist = []
    all_added_list = settings.input_tuple + settings.obstacle_tuple
    for thing in all_added_list:
        num = thing[1]
        list1 = thing[0].split("-")[0]
        list2 = thing[0].split("-")[1]
        if thing[0].startswith("obstacle"):
            print(str(num) + " " + list1.split("_")[1].capitalize() + " " + list2.split("_")[1].capitalize())
            keylist.append(str(num) + " " + list1.split("_")[1].capitalize() + " " + list2.split("_")[1].capitalize())       
        else:
            list3 = thing[0].split("-")[2]
            print(str(num) + " " + list1.split("_")[1].capitalize() + " " + list2.split("_")[1].capitalize() + " " + list3.split("_")[1].capitalize())
            keylist.append(str(num) + " " + list1.split("_")[1].capitalize() + " " + list2.split("_")[1].capitalize() + " " + list3.split("_")[1].capitalize())
    with open(settings.path + "reaper_keys.txt", "w") as file:
        file.write("//MIDI to Beat Saber map Reaper keys\n")
        for line in keylist:
            file.write(line + "\n")

def ParseJSON():
    fileindex = sys.argv[1]
    mode = sys.argv[2]
    typelist = []
    resultlist = []
    max = 0
    path = "C:\\beatsaber\\OST\\"
    filelist = glob.glob(path + "*.json")
    file = filelist[int(fileindex)]
    
    if mode == "--n":
        print("notes for " + file)
        with open(file, 'r') as jsonfile:
            data = json.load(jsonfile)
            for thing in data["_notes"]:
                thing.pop("_time")
                typelist.append((thing["_type"], thing["_lineIndex"], thing["_lineLayer"], thing["_cutDirection"]))
            resultlist = Counter(typelist).most_common()
            for value in resultlist:
                max += value[1]
            for key, value in resultlist:
                notetype = [item[0] for item in settings.note_types if key[0] == item[1]]
                notetype = notetype[0].split("_")[1].capitalize()
                lineindex = [item[0] for item in settings.line_indices if key[1] == item[1]]
                lineindex = lineindex[0].split("_")[1].capitalize()
                linelayer = [item[0] for item in settings.line_layers if key[2] == item[1]]
                linelayer = linelayer[0].split("_")[1].capitalize()
                cutdirection = [item[0] for item in settings.cut_directions if key[3] == item[1]]
                cutdirection = cutdirection[0].split("_")[1].capitalize()
                print("{:>2}{:<4}".format(str(value), "x") + "{:<1}{:^5.1%}{:>1}".format("(", value/max, ")") + "{:>8} {:>15} {:>10} {:>10}".format(notetype, lineindex, linelayer, cutdirection))

    elif mode == "--l":
        print("lighting for " + file)
        with open(file, 'r') as jsonfile:
            data = json.load(jsonfile)
            for thing in data["_events"]:
                thing.pop("_time")
                typelist.append((thing["_type"], thing["_value"]))
            resultlist = Counter(typelist).most_common()
            for value in resultlist:
                max += value[1]
            for key, value in resultlist:
                lighttype = [item[0] for item in settings.lighting_types if key[0] == item[1]]
                lighttype = lighttype[0].split("_")[1].capitalize()
                lightvalue = [item[0] for item in settings.lighting_values if key[1] == item[1]]
                lightvalue = lightvalue[0].split("_")[1].capitalize()
                print("{:>2}{:<4}".format(str(value), "x") + "{:<1}{:^5.1%}{:>1}".format("(", value/max, ")") + "{:>15} {:>12}".format(lighttype, lightvalue))

    elif mode == "--o":
        print("obstacles for " + file)
        with open(file, 'r') as jsonfile:
            data = json.load(jsonfile)
            for thing in data["_obstacles"]:
                thing.pop("_time")
                typelist.append((thing["_type"], thing["_lineIndex"], thing["_duration"], thing["_width"]))
            resultlist = Counter(typelist).most_common()
            for value in resultlist:
                max += value[1]
            for key, value in resultlist:
                obstacletype = [item[0] for item in settings.obstacle_types if key[0] == item[1]]
                obstacletype = obstacletype[0].split("_")[1].capitalize()
                obstaclelineindex = [item[0] for item in settings.obstacle_line_indices if key[1] == item[1]]
                obstaclelineindex = obstaclelineindex[0].split("_")[1].capitalize()
                obstacleduration = [item[0] for item in settings.obstacle_durations if key[2] == item[1]]
                obstacleduration = obstacleduration[0].split("_")[1].capitalize()
                obstaclewidth = [item[0] for item in settings.obstacle_widths if key[3] == item[1]]
                obstaclewidth = obstaclewidth[0].split("_")[1].capitalize()
                print("{:>2}{:<4}".format(str(value), "x") + "{:<1}{:^5.1%}{:>1}".format("(", value/max, ")") + "{:>8} {:>15} {:>14} {:>10}".format(obstacletype, obstaclelineindex, obstacleduration, obstaclewidth))


        
    

