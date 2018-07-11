from pydub import AudioSegment
import time
import shutil
import settings
import os

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
    

