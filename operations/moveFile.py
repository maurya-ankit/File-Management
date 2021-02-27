# works for both file and folder
import shutil
import voiceResponse


def move_file(src: str, dst: str):
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


if __name__ == "__main__":
    data = input("Enter : ").lower()
    # move [src] to [dst]
    if(data.startswith("move")):
        source = data.split(" ")[1]
        destination = data.split(" ")[3]
        move_file(source, destination)
