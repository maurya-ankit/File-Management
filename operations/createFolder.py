from pathlib import Path

def CreateFolder(folderName : str):
    p = Path(folderName)
    try:
        p.mkdir()
        print("created Successfully")
    except FileExistsError as exc:
        print(exc)
        print("File already exist")
    


if __name__ == "__main__":
    data = input("Enter : ").lower()
    # make/create a/the/one folder/directory [foldername]
    if(data.startswith("make") or data.startswith("create")):
        foldername = data.split(" ")[3]
        CreateFolder(folderName=foldername)