# works for both file and folder
import shutil

def MoveFile(src:str,dst:str):
    try:
        shutil.move(src, dst)
        print(f"{src} move to {dst} successfully")
        return True
    except FileExistsError as e:
        print(f"{e}: {dst}:file already exist with this name")
        return False
    except OSError as e:
        print(f"{e}")
        return False



if __name__ == "__main__":
    data = input("Enter : ").lower()
    # move [src] to [dst]
    if(data.startswith("move")):
        source = data.split(" ")[1]
        destination = data.split(" ")[3]
        MoveFile(source,destination)
