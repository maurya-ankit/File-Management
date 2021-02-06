from pathlib import Path
import shutil

def DeleteFolder(folderName : str):

    # If the file exists, delete it
    

    trash_dir = Path(folderName)

    try:
        trash_dir.rmdir()
        print(f"{folderName} folder deleted successfully")
    except FileNotFoundError as e:
        print(f'Error: {trash_dir} : {e.strerror}')
    except OSError as e:
        print(f'Error: {trash_dir} : {e.strerror}')
        if input("enter yes or no: ")=="yes":
            try:
                shutil.rmtree(trash_dir)
                print(f"{folderName} folder deleted successfully")
            except OSError as e:
                print(f'Error: {trash_dir} : {e.strerror}')




if __name__ == "__main__":
    data = input("Enter : ").lower()
    # remove/delete folder [foldername]
    if(data.startswith("remove") or data.startswith("delete")):
        foldername = data.split(" ")[2]
        DeleteFolder(folderName=foldername)