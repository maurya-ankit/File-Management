from variousOperationsTypes import fileOperations, sysControl
from fileMappings import fileType
import voiceResponse


creation = fileOperations.Creation()
deletion = fileOperations.Deletion()
rename = fileOperations.Rename()
navigation = fileOperations.Navigation()
content_navigation = fileOperations.ContentNavigation()

file_extension = fileType.FileType()

sys_control = sysControl.SystemOperations()


class Operations():
    def __init__(self):
        pass

    def start_operation(self, command_array: list):
        print('HI')
        if(command_array[0] == "create" or command_array[0] == "make"):
            print("Creation in process...")

            # Create file
            if(command_array[1] == "file"):
                try:
                    extension = file_extension.file_type(command_array[3])
                except:
                    extension = file_extension.file_type = ""

                filename = command_array[2] + extension

                status = "Successful" if creation.create_file(
                    filename) else "Unsuccessful"
                print("Operation was " + status)

            # Create folder/directory
            elif(command_array[1] == "folder" or command_array[1] == "directory"):
                status = "Successful" if creation.create_folder(
                    command_array[2]) else "Unsuccessful"

                print("Operation was " + status)

        # Condition for file deletion
        elif (command_array[0] == "delete" or command_array[0] == "remove"):
            print("Deletion in process...")

            # Delete file
            if(command_array[1] == "file"):
                try:
                    extension = file_extension.file_type(command_array[3])
                except:
                    extension = ""

                filename = command_array[2]+extension

                status = "successful" if deletion.delete_file(
                    filename) else "unsuccessful"
                print(status)

            # Delete folder/directory
            elif(command_array[1] == "folder" or command_array[1] == "directory"):
                status = "successful" if deletion.delete_folder(
                    command_array[2]) else "unsuccessful"

                print("Operation was " + status)

        elif (command_array[0] == "list" or command_array[0] == "show"):
            # list files in <directory_name>
            status = 'Successful' if navigation.show_dir() else 'Unsuccessful'
            print("Operation was " + status)

        elif(command_array[0] == "go back"):
            status = "Successful" if navigation.go_back() else "Unsuccessful"
            print("Operation was " + status)

        elif(command_array[0] == "open"):
            status = "Successful" if navigation.open_folder(
                folderName=command_array[1]) else "Unsuccessful"
            print("Operation was " + status)

        elif(command_array[0] == "rename"):
            print("rename array")

            # Rename file
            if(command_array[1] == "file"):
                src_extension = ""
                dst_extension = ""
                if(command_array[-1] in file_extension.get_file_type().keys()):
                    print("dst txt")

                    dst = command_array[-2]
                    dst_extension = file_extension.file_type(command_array[-1])
                    if (command_array[-3] in file_extension.get_file_type().keys()):
                        print("src txt")

                        src = command_array[-4]
                        src_extension = file_extension.file_type(
                            command_array[-3])
                    else:
                        print("src ")
                        src = command_array[-3]
                        src_extension = ""
                else:
                    print("dst txt")
                    dst = command_array[-1]
                    dst_extension = ""
                    if (command_array[-2] in file_extension.get_file_type().keys()):
                        print("src txt")
                        src = command_array[-3]
                        src_extension = file_extension.file_type(
                            command_array[-2])
                    else:
                        print("src ")
                        src = command_array[-2]
                        src_extension = ""

                dst = dst+dst_extension
                src = src+src_extension

                status = "Successful" if rename.rename_file(
                    src, dst) else "Unsuccessful"

                print(status)

            # Rename folder
            elif(command_array[1] == "folder" or command_array[1] == "directory"):
                pass

            print("this ran")

        elif(command_array[0] == "move"):

            # Move a file
            if(command_array[1] == "file"):
                extension = ""
                if(len(command_array) > 4):
                    try:
                        extension = file_extension.file_type(command_array[3])
                    except:
                        pass

                filename = command_array[2] + extension

                status = "Successful" if content_navigation.move_file(
                    filename, command_array[-1]) else "Unsuccessful"
                print("Operation was " + status)

            # Move foler
            elif(command_array[1] == "folder" or command_array[1] == "directory"):
                pass

        elif command_array[0] == 'change' or command_array[0] == 'set':
            if command_array[1] == 'volume':
                new_volume = sys_control.change_volume(50)
                voiceResponse.voice_response(
                    "System volume is now set to " + str(new_volume) + "%")

            # elif command_array[1] == 'brightness':
            #     new_brightness = obj.change_brightness(50)
            #     voiceResponse.voice_response(
            #         "System volume is now set to " + str(new_brightness) + "%")

        elif command_array[0] == 'shutdown':
            sysControl.sys_shutdown()

        elif command_array[0] == 'restart':
            sys_control.sys_reboot()

        elif("close" in command_array):
            IsRunning = False
            voiceResponse.voice_response("Thank you")

        else:
            voiceResponse.voice_response(
                'Sorry sir, I could not understand you, please repeat.')
