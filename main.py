import speech_recognition as sr
# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

try:
    transcript = r.recognize_google(audio)
    print(transcript)
except sr.UnknownValueError:
    print("google could not understand audio")
except sr.RequestError as e:
    print("google error; {0}".format(e))

  