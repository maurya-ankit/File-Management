import sys
import time
import pyttsx3
import voiceResponse
import speech_recognition as sr

from mainOperations import operations
from preprocessing.extractMeaningful import extract_meaningful


class AdminCenter(operations.Operations):
    def __init__(self):
        operations.Operations.__init__(self)

    def voice_response(self, response: str):
        jarvis = pyttsx3.init()
        jarvis.setProperty('rate', 172)
        jarvis.say(response)
        jarvis.runAndWait()

    def voice_recog(self) -> str:
        r2 = sr.Recognizer()
        with sr.Microphone() as source2:
            print("Say something!2")
            r2.adjust_for_ambient_noise(source2)
            audio2 = r2.listen(source2)

        return r2.recognize_google(audio2).lower()

    def ifNotFirst(self, transcript: str):
        # transcript2 = self.voice_recog()  # r2.recognize_google(audio2).lower()
        print("Your response: " + transcript)

        command_array2 = extract_meaningful(transcript)
        print("After segmentation: " + str(extract_meaningful(transcript)))

        if command_array2[0] == 'close':
            IsRunning = False
            voiceResponse.voice_response("Thank you, sir, Shutting Down")
            sys.exit()

        else:
            super().start_operation(command_array2)
            # attempt = attempt + 1
            # return attempt

    def auth(self, isFirst: bool):
        try:
            transcript = self.voice_recog()  # r.recognize_google(audio).lower()
            print("Your response: " + transcript)

            command_array = extract_meaningful(transcript)
            print("After segmentation: " + str(extract_meaningful(transcript)))

            print(isFirst)

            if isFirst and command_array[0] == 'kitretsu' or command_array[0] == 'ankit' or command_array[0] == 'ayush':
                self.voice_response("Authorization successful")
                time.sleep(0.002)
                self.voice_response("Hello sir, what can I do for you")
                time.sleep(0.001)

                new_transcript = self.voice_recog()

                self.ifNotFirst(new_transcript)

            elif not isFirst and not command_array[0] == 'kitretsu' or not command_array[0] == 'ankit' or not command_array[0] == 'ayush':
                self.voice_response("Authorization unsuccessful")

            else:
                self.ifNotFirst(transcript)

        except sr.UnknownValueError:
            print("Google could not understand audio")
            voiceResponse.voice_response(
                'Sorry sir, I could not understand you, please repeat.')

        except sr.RequestError as e:
            print("Google error; {0}".format(e))
            voiceResponse.voice_response(
                'Sorry sir, an unkown error occured. Try again')

    def audio_capture(self):
        IsRunning = True
        isFirst = True

        while IsRunning:
            if isFirst:
                self.voice_response("Please provide authorization passcode")

            time.sleep(0 if isFirst else 1)
            isFirst = False

            # obtain audio from the microphone
            # r = sr.Recognizer()
            # with sr.Microphone() as source:
            #     print("Say something!")
            #     r.adjust_for_ambient_noise(source)
            #     audio = r.listen(source)

            # attempt = 1

            # while attempt <= 5:
            #     attempt = self.auth(audio, r, attempt)

            self.auth(isFirst)
            #self.auth(audio, r, isFirst)


obj = AdminCenter()
obj.audio_capture()
