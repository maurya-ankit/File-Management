import os
import voiceResponse


def delete_file(fileName: str):

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


if __name__ == "__main__":
    data = input("Enter : ").lower()
    # remove/delete file [filename]
    if(data.startswith("remove") or data.startswith("delete")):
        filename = data.split(" ")[2]
        delete_file(fileName=filename)
