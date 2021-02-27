from pathlib import Path
import voiceResponse


def create_folder(folderName: str):
    p = Path(folderName)
    try:
        p.mkdir()
        voiceResponse.voice_response(
            f"Sir, directory named {folderName} was created successfully")
        print("created Successfully")
    except FileExistsError as exc:
        print(exc)
        print("File already exist")
        voiceResponse.voice_response(
            f'Sorry sir but folder named {folderName} already exists, please give it a different name')


if __name__ == "__main__":
    data = input("Enter : ").lower()
    # make/create a/the/one folder/directory [foldername]
    if(data.startswith("make") or data.startswith("create")):
        foldername = data.split(" ")[3]
        create_folder(folderName=foldername)
