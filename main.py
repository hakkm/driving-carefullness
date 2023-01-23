import os 
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

def speech(text, filename="audios/default_voice.mp3"):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    
    return said

speech("Are you driving?")
get_audio()