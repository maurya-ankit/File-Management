import os
import voiceResponse


def create_file(fileName: str):
    with open(fileName, "w"):
        pass
    voiceResponse.voice_response(
        f"Sir, file named {fileName} was created successfully")
    return True


if __name__ == "__main__":
    data = input("Enter : ").lower()
    # make/create a/the/one file [filename]
    if(data.startswith("make") or data.startswith("create")):
        filename = data.split(" ")[3]
        create_file(fileName=filename)
