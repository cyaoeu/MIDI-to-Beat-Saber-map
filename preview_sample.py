from pydub import AudioSegment
import time
import shutil



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