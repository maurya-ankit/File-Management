import os
import voiceResponse
# print(os.listdir("/"))
# for dirpath, dirnames, files in os.walk('./operations'):
#     print(f'Found directory: {dirpath}')
#     for file_name in files:
#         print(file_name)


def list_dir():
    try:
        dirs = os.listdir(".")
        voiceResponse.voice_response(
            "Here are the list of directories and files in the current directory, sir")
        for dir in dirs:
            print(dir)
            voiceResponse.voice_response(dir)
        return True
    except FileNotFoundError as e:
        print(f'FileNotFound error: {e.strerror}')
        voiceResponse.voice_response("No such directory found sir.")
        return False


if __name__ == "__main__":
    # data = input("Enter : ").lower()
    # show the content in folder
    # if(data.startswith("show")):
    # foldername = data.split(" ")[4]
    list_dir()
