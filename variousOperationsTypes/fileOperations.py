import os
import shutil
import voiceResponse
from pathlib import Path


class Creation():
    def __init__(self):
        pass

    def create_file(self, fileName: str) -> bool:
        with open(fileName, "w"):
            pass
        voiceResponse.voice_response(
            f"Sir, file named {fileName} was created successfully")
        return True

    def create_folder(self, folderName: str):
        p = Path(folderName)
        try:
            p.mkdir()
            voiceResponse.voice_response(
                f"Sir, directory named {folderName} was created successfully")
            print("created Successfully")
        except FileExistsError as exc:
            print(exc)
            print("File already exist!")
            voiceResponse.voice_response(
                f'Sorry sir but folder named {folderName} already exists, please give it a different name')


class Deletion():
    def __init__(self):
        pass

    def delete_file(self, fileName: str) -> bool:

        # If the file exists, delete it
        if os.path.isfile(fileName):
            os.remove(fileName)
            remFile = fileName
            voiceResponse.voice_response(
                f"File named {remFile} was deleted successfully, Sir")
            print(f"{remFile} deleted successfully")
            return True
        else:
            print(f'Error: {fileName} not a valid filename')
            voiceResponse.voice_response(
                f'Sorry sir, {fileName} is not a valid file name, operation failed')
            return False

    def delete_folder(self, folderName: str):

        # If the file exists, delete it

        trash_dir = Path(folderName)

        try:
            rem_dir = trash_dir
            trash_dir.rmdir()
            voiceResponse.voice_response(
                f"Directory named {rem_dir} was deleted successfully, Sir")
            print(f"{folderName} folder deleted successfully")
            return True
        except FileNotFoundError as e:
            print(f'Error: {trash_dir} : {e.strerror}')
            voiceResponse.voice_response(
                f'Sorry sir, but I could not find any directory named {trash_dir}. Operation failed')
        except OSError as e:
            print(f'Error: {trash_dir} : {e.strerror}')
            if input("enter yes or no: ") == "yes":
                try:
                    shutil.rmtree(trash_dir)
                    print(f"{folderName} directory deleted successfully")
                    voiceResponse.voice_response(
                        f"Folder named {folderName} was deleted successfully, Sir")
                except OSError as e:
                    print(f'Error: {trash_dir} : {e.strerror}')
                    voiceResponse.voice_response(
                        'Sorry sir, an error occured, please try again')


class Navigation():
    def __init__(self):
        pass

    def show_dir(self) -> bool:
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

    def go_back(self) -> bool:
        os.chdir("..")
        voiceResponse.voice_response("back to the parent directory")
        return True

    def open_folder(self, folderName: str) -> bool:
        if folderName in os.listdir("."):
            os.chdir(folderName)
            voiceResponse.voice_response(
                f"Sir, current working directory is now {folderName}")
            return True
        else:
            voiceResponse.voice_response(
                f"Sir, no folder named {folderName} here")
            return False


class Rename():
    def __init__(self):
        pass

    def rename_file(self, src: str, dst: str):
        try:
            os.rename(src, dst)
            print(f"{src} renamed to {dst} successfully")
            voiceResponse.voice_response(
                f'Sir the the file {src} was renamed successfully to {dst}')

        except FileExistsError as e:
            print(f"{e}: {dst}:file already exist with this name")
            voiceResponse.voice_response(
                f'Sorry sir, but this {dst} already exists, try renaming it with some other name')
        except OSError as e:
            print(f"{e}")
            voiceResponse.voice_response(
                'Sorry sir, an error occured, please try again.')

    def rename_folder(self):
        pass


class ContentNavigation():
    def __init__(self):
        pass

    def move_file(self, src: str, dst: str) -> bool:
        try:
            shutil.move(src, dst)
            print(f"{src} move to {dst} successfully")
            voiceResponse.voice_response(
                f'Selected file was successfully moved from {src} to {dst}, sir')
            return True
        except FileExistsError as e:
            print(f"{e}: {dst}:file already exist with this name")
            voiceResponse.voice_response(
                f'Sorry sir, but the selected file already exists at the {dst} directory')
            return False
        except OSError as e:
            print(f"{e}")
            voiceResponse.voice_response(
                f'Sorry sir, an error occured, please try again.')
            return False

    def move_folder(self):
        pass

    def copy_file(self):
        pass

    def copy_folder(self):
        pass

    def paste_file(self):
        pass

    def paste_folder(self):
        pass

    def cut_file(self):
        pass

    def cut_folder(self):
        pass
