import speech_recognition as sr
#import preprocessing.extractMeaningful
from preprocessing.extractMeaningful import extract_meaningful
# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

try:
    transcript = r.recognize_google(audio)
    print(transcript)
    extract_meaningful(transcript)
    print(extract_meaningful(transcript))

except sr.UnknownValueError:
    print("google could not understand audio")
except sr.RequestError as e:
    print("google error; {0}".format(e))
