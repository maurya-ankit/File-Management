import os

def CreateFile(fileName : str):
    with open(fileName,"w"):
        pass
    print("created Successfully")


if __name__ == "__main__":
    data = input("Enter : ").lower()
    # make/create a/the/one file [filename]
    if(data.startswith("make") or data.startswith("create")):
        filename = data.split(" ")[3]
        CreateFile(fileName=filename)