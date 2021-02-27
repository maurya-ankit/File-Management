import os
import voiceResponse


def rename_file(src: str, dst: str):
    try:
        os.rename(src, dst)
        print(f"{src} renamed to {dst} successfully")
        voiceResponse.voice_response(
            f'Sir the the file {src} was renamed successfully to {dst}')

    except FileExistsError as e:
        print(f"{e}: {dst}:file already exist with this name")
        voiceResponse.voice_response(
            f'Sorry sir, but this {dst} already exists, try renaming it with some other name')
    except OSError as e:
        print(f"{e}")
        voiceResponse.voice_response(
            'Sorry sir, an error occured, please try again.')


if __name__ == "__main__":
    data = input("Enter : ").lower()
    # rename [src] to [dst]
    if(data.startswith("rename")):
        source = data.split(" ")[1]
        destination = data.split(" ")[3]
        rename_file(source, destination)
