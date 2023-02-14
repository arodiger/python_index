
from pygame import mixer
from gtts import gTTS
import time

def speak(**kwargs):
    # tts = gTTS('This is WebChat, data persistence has been implemented via postgresdb.')
    tts = gTTS(kwargs['text'])
    tts.save('output.mp3')
    mixer.init()
    mixer.music.load('output.mp3')
    mixer.music.play()
    
# wait for the mixer to finish with the file
    while mixer.music.get_busy():
        time.sleep(.25)

    mixer.quit()

if __name__ == "__main__":

    speak(text='This is WebChat, data persistence has been implemented via postgresdb.')
    speak(text='I am testing passing additional text to the mixer')
    speak(text='This is the third line of text passed to the mixer')


# #############################################################################################
# import pyttsx3 #import the library

# def voiceChange():
#     eng = pyttsx3.init() #initialize an instance
#     voice = eng.getProperty('voices') #get the available voices
#     eng.setProperty('voice', voice[0].id) #set the voice to index 0 for male voice
#     # eng.setProperty('voice', voice[1].id) #changing voice to index 1 for female voice
#     eng.say("This is a demonstration of how to convert index of voice using pyttsx3 library in python.") #say method for passing text to be spoken
#     eng.runAndWait() #run and process the voice command

# if __name__ == "__main__":
#     voiceChange()
# #############################################################################################
