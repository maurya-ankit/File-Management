import speech_recognition as sr
import voiceResponse

#import preprocessing.extractMeaningful
from preprocessing.extractMeaningful import extract_meaningful

from operations.createFile import create_file
from operations.createFolder import create_folder
from operations.deleteFile import delete_file
from operations.deleteFolder import delete_folder
from operations.listDir import list_dir
from operations.moveFile import move_file
from operations.renameFile import rename_file

from mappings.filetype import file_type
from mappings.filetype import filetypedict

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

try:
    transcript = r.recognize_google(audio)
    print(transcript)
    command_array = extract_meaningful(transcript)
    print(extract_meaningful(transcript))

    # Condition for file creation
    if(command_array[0] == "create" or command_array[0] == "make"):
        print("make ran")

        # Create file
        if(command_array[1] == "file"):
            try:
                extension = file_type(command_array[3])
            except:
                extension = file_type = ""
            filename = command_array[2]+extension
            status = "successful" if create_file(filename) else "unsuccessful"
            print(status)

        # Create folder/directory
        elif(command_array[1] == "folder" or command_array[1] == "directory"):
            status = "successful" if create_folder(
                command_array[2]) else "unsuccessful"

    # Condition for file deletion
    elif (command_array[0] == "delete" or command_array[0] == "remove"):
        print("delete ran")

        # Delete file
        if(command_array[1] == "file"):
            try:
                extension = file_type(command_array[3])
            except:
                extension = ""
            filename = command_array[2]+extension
            status = "successful" if delete_file(filename) else "unsuccessful"
            print(status)

        # Delete folder/directory
        elif(command_array[1] == "folder" or command_array[1] == "directory"):
            status = "successful" if delete_folder(
                command_array[2]) else "unsuccessfull"
            print(status)

    # Condition to list files/directories
    elif (command_array[0] == "list" or command_array[0] == "show"):
        # list files in <directory_name>
        status = 'Successful' if list_dir(
            command_array[-1]) else 'Unsuccessful'
        print(status)

    # Condition for moving file
    elif(command_array[0] == "move"):

        # Move a file
        if(command_array[1] == "file"):
            extension = ""
            if(len(command_array) > 4):
                try:
                    extension = file_type(command_array[3])
                except:
                    pass
            filename = command_array[2]+extension
            status = "successful" if move_file(
                filename, command_array[-1]) else "unsuccessful"
            print(status)

        # Move foler
        elif(command_array[1] == "folder" or command_array[1] == "directory"):
            pass

    # Condition for renaming a file
    elif(command_array[0] == "rename"):
        print("rename array")

        # Rename file
        if(command_array[1] == "file"):
            src_extension = ""
            dst_extension = ""
            if(command_array[-1] in filetypedict.keys()):
                print("dst txt")

                dst = command_array[-2]
                dst_extension = file_type(command_array[-1])
                if (command_array[-3] in filetypedict.keys()):
                    print("src txt")

                    src = command_array[-4]
                    src_extension = file_type(command_array[-3])
                else:
                    print("src ")
                    src = command_array[-3]
                    src_extension = ""
            else:
                print("dst txt")
                dst = command_array[-1]
                dst_extension = ""
                if (command_array[-2] in filetypedict.keys()):
                    print("src txt")
                    src = command_array[-3]
                    src_extension = file_type(command_array[-2])
                else:
                    print("src ")
                    src = command_array[-2]
                    src_extension = ""
            dst = dst+dst_extension
            src = src+src_extension
            status = "successful" if rename_file(src, dst) else "unsuccessful"
            print(status)

        # Rename folder
        elif(command_array[1] == "folder" or command_array[1] == "directory"):
            pass

except sr.UnknownValueError:
    print("google could not understand audio")
    voiceResponse.voice_response(
        'Sorry sir, I could not understand you, please repeat.')

except sr.RequestError as e:
    print("google error; {0}".format(e))
    voiceResponse.voice_response(
        'Sorry sir, an unkown error occured. Try again')
