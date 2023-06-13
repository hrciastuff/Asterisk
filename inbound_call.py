
import speech_recognition as sr
import time
import unidecode
import sys

pin = sys.argv[1]
r = sr.Recognizer()

with sr.AudioFile("/tmp/opt." + pin + ".wav") as source:
    
    audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio, language='us-US')
        time.sleep(1.5)
        print(unidecode.unidecode(text.replace('','')))
    except:
        print("i can´t understand")
