import os

def DeleteFile(fileName : str):

    # If the file exists, delete it
    if os.path.isfile(fileName):
        os.remove(fileName)
        print(f"{fileName} deleted successfully")
    else:
        print(f'Error: {fileName} not a valid filename')


if __name__ == "__main__":
    data = input("Enter : ").lower()
    # remove/delete file [filename]
    if(data.startswith("remove") or data.startswith("delete")):
        filename = data.split(" ")[2]
        DeleteFile(fileName=filename)