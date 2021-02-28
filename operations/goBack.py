import os
import voiceResponse


def go_back():
    os.chdir("..")
    voiceResponse.voice_response("back to the parent directory")
    return True
        


if __name__ == "__main__":
    # go back
        go_back()