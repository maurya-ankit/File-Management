import os
import voiceResponse


def open_folder(folderName: str):
    if folderName in os.listdir("."):
        os.chdir(folderName)
        voiceResponse.voice_response(
        f"Sir, current working directory is now {folderName}")
        return True
    else:
        voiceResponse.voice_response(
        f"Sir, no folder named {folderName} here")
        return False


if __name__ == "__main__":
    data = input("Enter : ").lower()
    # open folder
    if(data.startswith("open")):
        filename = data.split(" ")[1]
        open_folder(folderName=filename)
