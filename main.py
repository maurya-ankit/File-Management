import time
import voiceResponse
import speech_recognition as sr

# import preprocessing.extractMeaningful
from preprocessing.extractMeaningful import extract_meaningful

from operations.createFile import create_file
from operations.createFolder import create_folder
from operations.deleteFile import delete_file
from operations.deleteFolder import delete_folder
from operations.listDir import list_dir
from operations.moveFile import move_file
from operations.renameFile import rename_file
from operations.openFolder import open_folder
from operations.goBack import go_back

from mappings.filetype import file_type
from mappings.filetype import filetypedict

from systemControls import sysControl

IsRunning = True
isFirst = True

while(IsRunning):
    if isFirst:
        voiceResponse.voice_response("Hello sir, what can I do for you?")

    time.sleep(0 if isFirst else 1)
    isFirst = False

    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        transcript = r.recognize_google(audio).lower()
        print(transcript)

        command_array = extract_meaningful(transcript)
        print(extract_meaningful(transcript))

        if command_array[0] == 'change' or command_array[0] == 'set':
            obj = sysControl.SystemOperations()

            if command_array[1] == 'volume':
                new_volume = obj.change_volume(50)
                voiceResponse.voice_response(
                    "System volume is now set to " + str(new_volume) + "%")

            # elif command_array[1] == 'brightness':
            #     new_brightness = obj.change_brightness(50)
            #     voiceResponse.voice_response(
            #         "System volume is now set to " + str(new_brightness) + "%")

        elif command_array[0] == 'shutdown':
            obj2 = sysControl.SystemOperations()
            obj2.sys_shutdown()

        elif command_array[0] == 'restart':
            obj3 = sysControl.SystemOperations()
            obj3.sys_reboot()

        elif command_array[0] == 'stop' or command_array[0] == 'pause' or command_array[0] == 'wait' or (command_array[0] == 'Take' and command_array[1] == 'rest'):
            voiceResponse.voice_response(
                "I am sleep in mode now, please say Resume to wake me up")
            print("Sleep mode on, say Resume to resume!")

            while True:
                r_pause_state = sr.Recognizer()
                with sr.Microphone() as source2:
                    print("Listening quietly, will activate if Resume is heard !!!")
                    r_pause_state.adjust_for_ambient_noise(source2)
                    audio_pause_state = r_pause_state.listen(source2)

                time.sleep(2)

                transcript_pause_state = r_pause_state.recognize_google(
                    audio).lower()
                command_array_pause_state = extract_meaningful(transcript)

                if 'start' in command_array_pause_state or 'resume' in command_array_pause_state:
                    break

            continue

        elif("close" in command_array):
            IsRunning = False
            voiceResponse.voice_response("Thank you")
            break

        # Condition for file creation
        elif(command_array[0] == "open"):
            status = "successfull" if open_folder(
                folderName=command_array[1]) else "unsuccessfull"

        elif(transcript == "go back"):
            status = "successfull" if go_back() else "unsuccessfull"

        elif(command_array[0] == "create" or command_array[0] == "make"):
            print("make ran")

            # Create file
            if(command_array[1] == "file"):
                try:
                    extension = file_type(command_array[3])
                except:
                    extension = file_type = ""
                filename = command_array[2]+extension
                status = "successful" if create_file(
                    filename) else "unsuccessful"
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
                status = "successful" if delete_file(
                    filename) else "unsuccessful"
                print(status)

            # Delete folder/directory
            elif(command_array[1] == "folder" or command_array[1] == "directory"):
                status = "successful" if delete_folder(
                    command_array[2]) else "unsuccessfull"
                print(status)

        # Condition to list files/directories
        elif (command_array[0] == "list" or command_array[0] == "show"):
            # list files in <directory_name>
            status = 'Successful' if list_dir() else 'Unsuccessful'
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
                status = "successful" if rename_file(
                    src, dst) else "unsuccessful"
                print(status)

            # Rename folder
            elif(command_array[1] == "folder" or command_array[1] == "directory"):
                pass

            print("this ran")
        else:
            voiceResponse.voice_response(
                'Sorry sir, I could not understand you, please repeat.')
            continue

    except sr.UnknownValueError:
        print("google could not understand audio")
        voiceResponse.voice_response(
            'Sorry sir, I could not understand you, please repeat.')

    except sr.RequestError as e:
        print("google error; {0}".format(e))
        voiceResponse.voice_response(
            'Sorry sir, an unkown error occured. Try again')
