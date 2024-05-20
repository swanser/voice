#speechEngine GUI

import tkinter
import pyttsx3
import subprocess

class speechWindow(tkinter.Frame):

    def __init__(self, parent):

        tkinter.Frame.__init__(self, parent)

        self.parent = parent

        self.parent.wm_title("Robots.software Speech Engine GUI")

        self.engineStatus = False

        self.engine = pyttsx3.init()

        self.engineStatus = True

        self.voices = self.engine.getProperty('voices')    

        for eachVoice in self.voices:

            print("=================")
            print(eachVoice.id)
            print(eachVoice.name)

        self.createWidgets()
        
    def createWidgets(self):

        self.testFrame = tkinter.LabelFrame(self, text = "Configuration")

        self.wordField = tkinter.Text(self.testFrame, width = 50, height = 1)
        self.wordField.grid(row = 3, column = 1)

        self.sayButton = tkinter.Button(self.testFrame, text = "Test", command = lambda : self.sayWords(self.wordField.get("1.0", tkinter.END)))
        self.sayButton.grid(row = 3, column = 2)

        self.testFrame.voiceListLabel = tkinter.Label(self.testFrame, text = "Voices:")
        self.testFrame.voiceList = tkinter.Listbox(self.testFrame, height = 6, width = 80)
        self.testFrame.voiceListLabel.grid(row = 0, column = 0)
        self.testFrame.voiceList.grid(row = 1, column = 0, columnspan = 3)
        
        for voice in self.voices:
            self.testFrame.voiceList.insert(tkinter.END, voice.id)
        
        self.testFrame.voiceList.bind('<<ListboxSelect>>', self.updateSelectedVoice)


        self.testFrame.optionsFrame = tkinter.Frame(self.testFrame)
        self.testFrame.optionsFrame.volumeLabel = tkinter.Label(self.testFrame.optionsFrame, text = "Volume")
        self.testFrame.optionsFrame.volumeText = tkinter.Text(self.testFrame.optionsFrame, height = 1, width = 3)
        self.testFrame.optionsFrame.volumeText.insert("1.0",self.engine.getProperty('volume'))
        self.testFrame.optionsFrame.voiceVolumeSetButton = tkinter.Button(self.testFrame.optionsFrame, text = "Set", command = self.setVolume)
        
        self.testFrame.optionsFrame.rateLabel = tkinter.Label(self.testFrame.optionsFrame, text = "Rate")
        self.testFrame.optionsFrame.rateText = tkinter.Text(self.testFrame.optionsFrame, height = 1, width = 3)
        self.testFrame.optionsFrame.rateText.insert("1.0",self.engine.getProperty('rate'))
        self.testFrame.optionsFrame.voiceSpeechRateSetButton = tkinter.Button(self.testFrame.optionsFrame, text = "Set", command = self.setRate)

        self.testFrame.optionsFrame.volumeLabel.grid(row = 2, column = 0)
        self.testFrame.optionsFrame.volumeText.grid(row = 2, column = 1)
        self.testFrame.optionsFrame.voiceVolumeSetButton.grid(row = 2, column = 3)
        
        self.testFrame.optionsFrame.rateLabel.grid(row = 3, column = 0)
        self.testFrame.optionsFrame.rateText.grid(row = 3, column = 1)
        self.testFrame.optionsFrame.voiceSpeechRateSetButton.grid(row = 3, column = 3)
        
        self.testFrame.optionsFrame.grid(row = 3, column = 0)

        self.launchFrame = tkinter.LabelFrame(self, text = "API Launcher")

        self.launchFrame.launcherConfigDisplayHeader = tkinter.Label(self.launchFrame, text = "Voice API Configuration:")
        self.launchFrame.launcherConfigDisplayHeader.grid(row = 0, column = 0)

        self.launchFrame.voiceIDLabel = tkinter.Label(self.launchFrame, text = "Voice ID:")
        self.launchFrame.voiceIDVar = tkinter.StringVar()
        self.launchFrame.voiceIDDisplayLabel = tkinter.Label(self.launchFrame, textvar = self.launchFrame.voiceIDVar)

        self.launchFrame.voiceNameLabel = tkinter.Label(self.launchFrame, text = "Voice Name:")
        self.launchFrame.voiceNameVar = tkinter.StringVar()
        self.launchFrame.voiceNameDisplayLabel = tkinter.Label(self.launchFrame, textvar = self.launchFrame.voiceNameVar)

        self.launchFrame.voiceAgeLabel = tkinter.Label(self.launchFrame, text = "Voice Age:")
        self.launchFrame.voiceAgeVar = tkinter.StringVar()
        self.launchFrame.voiceAgeDisplayLabel = tkinter.Label(self.launchFrame, textvar = self.launchFrame.voiceAgeVar)

        self.launchFrame.voiceGenderLabel = tkinter.Label(self.launchFrame, text = "Voice Gender:")
        self.launchFrame.voiceGenderVar = tkinter.StringVar()
        self.launchFrame.voiceGenderDisplayLabel = tkinter.Label(self.launchFrame, textvar = self.launchFrame.voiceGenderVar)

        self.launchFrame.voiceSpeechRateLabel = tkinter.Label(self.launchFrame, text = "Speech Rate:")
        self.launchFrame.voiceSpeechRateVar = tkinter.StringVar()
        self.launchFrame.voiceSpeechRateVar.set(self.engine.getProperty('rate'))
        self.launchFrame.voiceSpeechRateDisplayLabel = tkinter.Label(self.launchFrame, textvar = self.launchFrame.voiceSpeechRateVar)

        self.launchFrame.voiceVolumeLabel = tkinter.Label(self.launchFrame, text = "Volume:")
        self.launchFrame.voiceVolumeVar = tkinter.StringVar()
        self.launchFrame.voiceVolumeVar.set(self.engine.getProperty('volume'))
        self.launchFrame.voiceVolumeDisplayLabel = tkinter.Label(self.launchFrame, textvar = self.launchFrame.voiceVolumeVar)
        
        self.launchFrame.launchButton = tkinter.Button(self.launchFrame, text = "Launch!", command = self.launchAPI)
        self.launchFrame.portLabel = tkinter.Label(self.launchFrame, text = "Port")
        self.launchFrame.portField = tkinter.Text(self.launchFrame, width = 6, height = 1)
        
        self.launchFrame.voiceIDLabel.grid(row = 1, column = 0, sticky = 'w')
        self.launchFrame.voiceIDDisplayLabel.grid(row = 1, column = 1, sticky = 'w')
        self.launchFrame.voiceNameLabel.grid(row = 2, column = 0, sticky = 'w')
        self.launchFrame.voiceNameDisplayLabel.grid(row = 2, column = 1, sticky = 'w')
        self.launchFrame.voiceAgeLabel.grid(row = 3, column = 0, sticky = 'w')
        self.launchFrame.voiceAgeDisplayLabel.grid(row = 3, column = 1, sticky = 'w')
        self.launchFrame.voiceGenderLabel.grid(row = 4, column = 0, sticky = 'w')
        self.launchFrame.voiceGenderDisplayLabel.grid(row = 4, column = 1, sticky = 'w')
        self.launchFrame.voiceSpeechRateLabel.grid(row = 5, column = 0, sticky = 'w')
        self.launchFrame.voiceSpeechRateDisplayLabel.grid(row = 5, column = 1, sticky = 'w')
        self.launchFrame.voiceVolumeLabel.grid(row = 6, column = 0, sticky = 'w')
        self.launchFrame.voiceVolumeDisplayLabel.grid(row = 6, column = 1, sticky = 'w')
        self.launchFrame.launchButton.grid(row = 7, column = 0)
        self.launchFrame.portLabel.grid(row = 7, column = 1, sticky = 'e')
        self.launchFrame.portField.grid(row = 7, column = 2, sticky = 'w')
        
                
        self.testFrame.grid(row = 0, column = 0)
        self.launchFrame.grid(row = 0, column = 1)

        self.pack()

    def updateSelectedVoice(self, event):
        try:
            print(self.testFrame.voiceList.get(self.testFrame.voiceList.curselection()))
            voiceIDClicked = self.testFrame.voiceList.get(self.testFrame.voiceList.curselection())
            self.engine.setProperty('voice', voiceIDClicked)
            print("Voice id set to", voiceIDClicked)

            for eachVoice in self.voices:
                if eachVoice.id == voiceIDClicked:
                    self.launchFrame.voiceNameVar.set(eachVoice.name)
                    self.launchFrame.voiceIDVar.set(eachVoice.id)
                    self.launchFrame.voiceAgeVar.set(eachVoice.age)
                    self.launchFrame.voiceGenderVar.set(eachVoice.gender)
        except Exception as e:
            print("Error switching voice!", e)

    def setRate(self):

        try:
            rate = int(self.testFrame.optionsFrame.rateText.get('1.0', tkinter.END))
            self.engine.setProperty('rate', rate)
            self.launchFrame.voiceSpeechRateVar.set(str(rate))
            print("NEW RATE:", rate)
        except Exception as E:
            print(E)

    def setVolume(self):

        try:
            volume = float(self.testFrame.optionsFrame.volumeText.get('1.0', tkinter.END))
            self.engine.setProperty('volume', volume)
            self.launchFrame.voiceVolumeVar.set(str(volume))
            print("NEW volume:", volume)
        except Exception as E:
            print(E)

    def sayWords(self, words):

        self.engine.say(words)
        self.engine.runAndWait()
        print("Done")

    def launchAPI(self):
        results=subprocess.run(["flask", "--app", "talker", "run"], capture_output=True, shell=True)
        print(results)
        
print("INIT")

mySpeechEngineWindow = speechWindow(tkinter.Tk())

