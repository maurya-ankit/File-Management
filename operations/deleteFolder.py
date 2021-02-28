from pathlib import Path
import shutil
import voiceResponse


def delete_folder(folderName: str):

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


if __name__ == "__main__":
    data = input("Enter : ").lower()
    # remove/delete folder [foldername]
    if(data.startswith("remove") or data.startswith("delete")):
        foldername = data.split(" ")[2]
        delete_folder(folderName=foldername)
