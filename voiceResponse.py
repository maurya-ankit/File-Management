import pyttsx3

jarvis = pyttsx3.init()
jarvis.setProperty('rate', 172)


def voice_response(response: str):
    jarvis.say(response)
    jarvis.runAndWait()
