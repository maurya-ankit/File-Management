import speech_recognition as sr
#import preprocessing.extractMeaningful
from preprocessing.extractMeaningful import extract_meaningful

from operations.createFile import CreateFile
from operations.createFolder import CreateFolder
from operations.deleteFile import DeleteFile
from operations.deleteFolder import DeleteFolder
from operations.moveFile import MoveFile
from operations.renameFile import RenameFile
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
    if(command_array[0]=="create" or command_array[0] == "make"):
        print("make ran")
        if(command_array[1]=="file"):
            try:
                extension = file_type(command_array[3])
            except:
                extension = file_type=""
            filename = command_array[2]+extension
            status = "successfull" if CreateFile(filename) else "unsuccessfull"
            print(status)
        elif(command_array[1]=="folder"):
            status = "successfull" if CreateFolder(command_array[2]) else "unsuccessfull"
    elif (command_array[0]=="delete" or command_array[0] == "remove"):
        print("delete ran")
        if(command_array[1]=="file"):
            try:
                extension = file_type(command_array[3])
            except:
                extension = ""
            filename = command_array[2]+extension
            status = "successfull" if DeleteFile(filename) else "unsuccessfull"
            print(status)
        elif(command_array[1]=="folder"):
            status = "successfull" if DeleteFolder(command_array[2]) else "unsuccessfull"
            print(status)
            
    elif(command_array[0]=="move"):
        if(command_array[1]=="file"):
            extension = ""
            if(len(command_array)>4):
                try:
                    extension = file_type(command_array[3])
                except:
                    pass
            filename = command_array[2]+extension
            status = "successfull" if MoveFile(filename,command_array[-1]) else "unsuccessfull"
            print(status)
        elif(command_array[1]=="folder"):
            pass

    elif(command_array[0]=="rename"):
        print("rename array")
        if(command_array[1]=="file"):
            src_extension = ""
            dst_extension = ""
            if(command_array[-1] in filetypedict.keys()):
                print("dst txt")

                dst = command_array[-2]
                dst_extension=file_type(command_array[-1]);
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
                dst_extension=""
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
            status = "successfull" if RenameFile(src,dst) else "unsuccessfull"
            print(status)
        elif(command_array[1]=="folder"):
            pass

except sr.UnknownValueError:
    print("google could not understand audio")
except sr.RequestError as e:
    print("google error; {0}".format(e))
