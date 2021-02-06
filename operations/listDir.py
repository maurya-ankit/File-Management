import os
# print(os.listdir("/"))
# for dirpath, dirnames, files in os.walk('./operations'):
#     print(f'Found directory: {dirpath}')
#     for file_name in files:
#         print(file_name)

def listDir(folderName:str):
    dirs = os.listdir(folderName)
    for dir in dirs:
        print(dir)

if __name__ == "__main__":
    data = input("Enter : ").lower()
    # show the content in folder
    if(data.startswith("show")):
        foldername = data.split(" ")[4]
        listDir(folderName=foldername)