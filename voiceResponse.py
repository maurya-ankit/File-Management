import pyttsx3


def voice_response(response: str):
    jarvis = pyttsx3.init()
    jarvis.setProperty('rate', 172)
    jarvis.say(response)
    jarvis.runAndWait()
