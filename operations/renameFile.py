import os

def RenameFile(src:str,dst:str):
    try:
        os.rename(src, dst)
        print(f"{src} renamed to {dst} successfully")
    except FileExistsError as e:
        print(f"{e}: {dst}:file already exist with this name")
    except OSError as e:
        print(f"{e}")

if __name__ == "__main__":
    data = input("Enter : ").lower()
    # rename [src] to [dst]
    if(data.startswith("rename")):
        source = data.split(" ")[1]
        destination = data.split(" ")[3]
        RenameFile(source,destination)
