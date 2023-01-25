import pyttsx3
from gtts import gTTS
import playsound
import os

'''
def speak(text):
    tts = gTTS(text=text, lang='en', tld='ca')

    filename = "abc.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

speak("Hello noobs lol")
'''
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
text = "Python is a great programming language"
engine.say(text)
engine.runAndWait()


