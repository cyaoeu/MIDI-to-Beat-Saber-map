from pydub import AudioSegment
import time
import shutil
import MIDIbeat_settings as s
import os
import sys
import json
import collections
from collections import Counter
import operator
import glob


def RenderNoteWavs(): #create samples from individual .wavs for preview purposes
    debugprint = []
    for note in s.notes:
        for line in s.lines:
            for layer in s.layers:
                for cut in s.cuts:
                    debugprint.append(note)
                    debugprint.append(line)
                    debugprint.append(layer)
                    note_wav = AudioSegment.from_wav(s.path + note + s.ext)
                    line_wav = AudioSegment.from_wav(s.path + line + s.ext)
                    layer_wav = AudioSegment.from_wav(s.path + layer + s.ext)
                    if note == "note_mine":
                        print(debugprint)
                        finalwav = note_wav + line_wav + layer_wav
                        finalwav.export(s.path + "output\\" + note + "_" + line + "_" + layer + ".wav", format="wav")
                        debugprint = []
                        time.sleep(1)
                        break
                    else:
                        debugprint.append(cut)
                        layer_cut =  AudioSegment.from_wav(s.path + cut + s.ext)
                        finalwav = note_wav + line_wav + layer_wav + layer_cut
                        finalwav.export(s.path + "output\\" + note + "_" + line + "_" + layer + "_" + cut + ".wav", format="wav")
                        print(debugprint)
                        debugprint = []
                        time.sleep(1)

def RenderObstacleWavs():
    debugprint = []
    for obstacle in s.obstacles:
        for line in s.obstaclelines:
            debugprint.append(obstacle)
            debugprint.append(line)
            obstacle_wav = AudioSegment.from_wav(s.path + obstacle + s.ext)
            
            if obstacle == "obstacle_ceiling":
                print(debugprint)
                finalwav = obstacle_wav
                finalwav.export(s.path + "output\\" + obstacle + ".wav", format="wav")
                debugprint = []
                time.sleep(1)
                break
            else:
                debugprint.append(line)
                line_wav = AudioSegment.from_wav(s.path + line + s.ext)
                finalwav = obstacle_wav + line_wav
                finalwav.export(s.path + "output\\" + obstacle + "_" + line + ".wav", format="wav")
                print(debugprint)
                debugprint = []
                time.sleep(1)

def RenameReaperOutput(): #renames wavs exported as individual items   note: specific order!
    wavlist = [filename for filename in os.listdir(s.path) if filename.endswith(".wav")]
    combined_audio = s.notes + s.lines + s.layers + s.cuts + s.obstacles + s.obstaclelines
    for i, filename in enumerate(wavlist):
        shutil.move(s.path + filename, s.path + combined_audio[i] + s.ext)
        print(s.path + filename + " = " + s.path + combined_audio[i] + s.ext)

def CreateReaperNotenamesFile():
    notekeylist = []
    eventkeylist = []
    notelist = s.input_tuple + s.obstacle_tuple
    favorite_notelist = s.note_favorites
    eventlist = s.lighting_tuple
    favorite_eventlist = s.event_favorites
    for thing in notelist:
        num = thing[1]
        list1 = thing[0].split("-")[0]
        list2 = thing[0].split("-")[1]
        if thing[0].startswith("obstacle"):
            print(str(num) + " " + list1.split("_")[1].capitalize() + " " + list2.split("_")[1].capitalize())
            notekeylist.append(str(num) + " " + list1.split("_")[1].capitalize() + " " + list2.split("_")[1].capitalize())       
        else:
            list3 = thing[0].split("-")[2]
            print(str(num) + " " + list1.split("_")[1].capitalize() + " " + list2.split("_")[1].capitalize() + " " + list3.split("_")[1].capitalize())
            notekeylist.append(str(num) + " " + list1.split("_")[1].capitalize() + " " + list2.split("_")[1].capitalize() + " " + list3.split("_")[1].capitalize())
    for thing in favorite_notelist:
        num = thing[1]
        list1 = thing[0].split("-")[0]
        list2 = thing[0].split("-")[1]
        list3 = thing[0].split("-")[2]
        list4 = thing[0].split("-")[3]
        print(str(num) + " " + list1.split("_")[1].capitalize() + " " + list2.split("_")[1].capitalize() + " " + list3.split("_")[1].capitalize() + " " + list4.split("_")[1].capitalize())
        notekeylist.append(str(num) + " " + list1.split("_")[1].capitalize() + " " + list2.split("_")[1].capitalize() + " " + list3.split("_")[1].capitalize() + " " + list4.split("_")[1].capitalize())

    for thing in eventlist:
        num = thing[1]
        list1 = thing[0].split("-")[0]
        print(str(num) + " " + list1.split("_")[1].capitalize())
        eventkeylist.append(str(num) + " " + list1.split("_")[1].capitalize())  
    for thing in favorite_eventlist:
        num = thing[1]
        list1 = thing[0].split("-")[0]
        list2 = thing[0].split("-")[1]
        print(str(num) + " " + list1.split("_")[1].capitalize() + " " + list2.split("_")[1].capitalize())
        eventkeylist.append(str(num) + " " + list1.split("_")[1].capitalize() + " " + list2.split("_")[1].capitalize())  
    

    with open(s.path + "reaper_keys_notes.txt", "w") as file:
        file.write("//MIDI to Beat Saber map Reaper keys (Notes)\n")
        for line in notekeylist:
            file.write(line + "\n")

    with open(s.path + "reaper_keys_events.txt", "w") as file:
        file.write("//MIDI to Beat Saber map Reaper keys (Events)\n")
        for line in eventkeylist:
            file.write(line + "\n")

def CreateVisualizationFavoritesFile(): # crappy setup but it works for now
    favorite_notelist = s.note_favorites
    output = []
    blue_num = []
    blue_n_pointer = "200"
    blue_n = []
    blue_saber_start = "96"
    blue_saber_end = "107"
    blue_x_note_pointer = "1200"
    blue_x_note = []
    blue_y_note_pointer = "1500"
    blue_y_note = []
    blue_cut_direction_pointer = "1700"
    blue_cut_direction = []

    red_num = []
    red_n_pointer = "700"
    red_n = []
    red_saber_start = "108"
    red_saber_end = "119"
    red_x_note_pointer = "2200"
    red_x_note = []
    red_y_note_pointer = "2500"
    red_y_note = []
    red_cut_direction_pointer = "2700"
    red_cut_direction = []
    for thing in favorite_notelist:
        num = thing[1]
        list1 = thing[0].split("-")[0]
        list2 = thing[0].split("-")[1]
        list3 = thing[0].split("-")[2]
        list4 = thing[0].split("-")[3]
        if list1 == "note_blue":
            blue_num.append(num)
            blue_n.append(list1)
            blue_x_note.append(list2)
            blue_y_note.append(list3)
            blue_cut_direction.append(list4)
        elif list1 == "note_red":
            red_num.append(num)
            red_n.append(list1)
            red_x_note.append(list2)
            red_y_note.append(list3)
            red_cut_direction.append(list4)

    output.append("blue_n = " + blue_n_pointer + ";")
    output.append("blue_saber_start = " + blue_saber_start + ";") 
    output.append("blue_saber_end = " + blue_saber_end + ";") 
    output.append("blue_x_note = " + blue_x_note_pointer + ";") 
    output.append("blue_y_note = " + blue_y_note_pointer + ";") 
    output.append("blue_cut_direction = " + blue_cut_direction_pointer + ";")   
    
    for i, thing in enumerate(blue_n):
        output.append("blue_n[" + str(i) + "] = " + str(blue_num[i]) + ";")
        output.append("blue_x_note[" + str(i) + "] = " + blue_x_note[i] + ";")
        output.append("blue_y_note[" + str(i) + "] = " + blue_y_note[i] + ";")
        output.append("blue_cut_direction[" + str(i) + "] = " + blue_cut_direction[i] + ";")
    
    output.append("red_n = " + red_n_pointer + ";")
    output.append("red_saber_start = " + red_saber_start + ";") 
    output.append("red_saber_end = " + red_saber_end + ";") 
    output.append("red_x_note = " + red_x_note_pointer + ";") 
    output.append("red_y_note = " + red_y_note_pointer + ";") 
    output.append("red_cut_direction = " + red_cut_direction_pointer + ";")   

    for i, thing in enumerate(red_n):
        output.append("red_n[" + str(i) + "] = " + str(red_num[i]) + ";")
        output.append("red_x_note[" + str(i) + "] = " + red_x_note[i] + ";")
        output.append("red_y_note[" + str(i) + "] = " + red_y_note[i] + ";")
        output.append("red_cut_direction[" + str(i) + "] = " + red_cut_direction[i] + ";")

    for line in output:
        print(line)

    with open(s.path + "visualization_effect_favorite_notes.txt", "w") as file:
        for line in output:
            file.write(line + "\n")

    



def ParseJSON():
    mode = sys.argv[1]
    fileindex = sys.argv[2]
    typelist = []
    resultlist = []
    max = 0
    path = "C:\\beatsaber\\OST\\"
    filelist = glob.glob(path + "*.json")
    #filelist = glob.glob(path + "**/" + "*.json")
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
            filelist = []
            for key, value in resultlist:
                notetype = [item[0] for item in s.note_types if key[0] == item[1]]
                notetype_print = notetype[0].split("_")[1].capitalize()
                lineindex = [item[0] for item in s.line_indices if key[1] == item[1]]
                lineindex_print = lineindex[0].split("_")[1].capitalize()
                linelayer = [item[0] for item in s.line_layers if key[2] == item[1]]
                linelayer_print = linelayer[0].split("_")[1].capitalize()
                cutdirection = [item[0] for item in s.cut_directions if key[3] == item[1]]
                cutdirection_print = cutdirection[0].split("_")[1].capitalize()
                print("{:>2}{:<4}".format(str(value), "x") + "{:<1}{:^5.1%}{:>1}".format("(", value/max, ")") + "{:>8} {:>15} {:>10} {:>10}".format(notetype_print, lineindex_print, linelayer_print, cutdirection_print))
                filelist += notetype + list("-") + lineindex + list("-") + linelayer + list("-") + cutdirection + list("                " + str(value) + "x (" + "{:^5.1%}".format(value/max)) + list("\n")
            with open(file.rsplit(".", 1)[0] + "_notes.txt", 'w') as txtfile:
                for thing in filelist:
                    txtfile.write(str(thing))


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
            filelist = []
            for key, value in resultlist:
                lighttype = [item[0] for item in s.lighting_types if key[0] == item[1]]
                lighttype_print = lighttype[0].split("_")[1].capitalize()
                lightvalue = [item[0] for item in s.lighting_lightvalues if key[1] == item[1]]
                lightvalue_print = lightvalue[0].split("_")[1].capitalize()
                print("{:>2}{:<4}".format(str(value), "x") + "{:<1}{:^5.1%}{:>1}".format("(", value/max, ")") + "{:>15} {:>12}".format(lighttype_print, lightvalue_print))
                filelist += lighttype + list("-") + lightvalue + list("                " + str(value) + "x (" + "{:^5.1%}".format(value/max)) + list("\n")
            with open(file.rsplit(".", 1)[0] + "_events.txt", 'w') as txtfile:
                for thing in filelist:
                    txtfile.write(str(thing))
                



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
            filelist = []
            for key, value in resultlist:
                obstacletype = [item[0] for item in s.obstacle_types if key[0] == item[1]]
                obstacletype_print = obstacletype[0].split("_")[1].capitalize()
                obstaclelineindex = [item[0] for item in s.obstacle_line_indices if key[1] == item[1]]
                obstaclelineindex_print = obstaclelineindex[0].split("_")[1].capitalize()
                obstacleduration = [item[0] for item in s.obstacle_durations if key[2] == item[1]]
                obstacleduration_print = obstacleduration[0].split("_")[1].capitalize()
                obstaclewidth = [item[0] for item in s.obstacle_widths if key[3] == item[1]]
                obstaclewidth_print = obstaclewidth[0].split("_")[1].capitalize()
                print("{:>2}{:<4}".format(str(value), "x") + "{:<1}{:^5.1%}{:>1}".format("(", value/max, ")") + "{:>8} {:>15} {:>14} {:>10}".format(obstacletype_print, obstaclelineindex_print, obstacleduration_print, obstaclewidth_print))
                filelist += obstacletype + list("-") + obstaclelineindex + list("-") + obstacleduration + list("-") + obstaclewidth + list("                " + str(value) + "x (" + "{:^5.1%}".format(value/max)) + list("\n")
            with open(file.rsplit(".", 1)[0] + "_obstacles.txt", 'w') as txtfile:
                for thing in filelist:
                    txtfile.write(str(thing))
                

        
    

