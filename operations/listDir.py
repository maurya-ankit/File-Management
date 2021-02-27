import os
import voiceResponse
# print(os.listdir("/"))
# for dirpath, dirnames, files in os.walk('./operations'):
#     print(f'Found directory: {dirpath}')
#     for file_name in files:
#         print(file_name)


def list_dir(folderName: str):
    try:
        dirs = os.listdir(folderName)
        voiceResponse.voice_response(
            "Here are the list of directories and files in the current directory, sir")
        for dir in dirs:
            print(dir)
            voiceResponse.voice_response(dir)
    except FileNotFoundError as e:
        print(f'FileNotFound error: {e.strerror}')
        voiceResponse.voice_response("No such directory found sir.")


if __name__ == "__main__":
    data = input("Enter : ").lower()
    # show the content in folder
    if(data.startswith("show")):
        foldername = data.split(" ")[4]
        list_dir(folderName=foldername)
