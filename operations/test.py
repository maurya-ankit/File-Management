file_creation = [
    "Create <filetype> file <filename>",    # type--->0

    #"Create file named <filename>",
    "Create file named"  # <filename>.<filetype>",    # type--->1
    # "Create file named as <filename>",
    #"Create file named as <filename>.<filetype>",

    #"Create <filetype> file named <filename>",
    ## "Create <filetype> file named as <filename>",
    ## "Create <filetype> file named as <filename> here",
    ## "Create <filetype> file named as <filename> in this folder",
    "Create <filetype> file named as <filename> here in this folder",   # type--->2

    #"Create <filetype> file with name <filename>",
    "Create <filetype> file with name <filename>.<filetype>",   # type--->3

    "Create <filename>.<filetype>"    # type--->4
    "Create file <filename>.<filetype>"    # type--->5

    # "Create <filename>.<filetype> here"
    # "Create <filename>.<filetype> in this folder"
    "Create <filename>.<filetype> here in this folder"    # type--->6
]

type_map = {
    0: [1, 3],
    1: [3],
    2: [1, 4],
    3: [1, 4],
    4: [1],
    5: [2],
    6: [2]
}

# l = ["Create", "a", "file", "yahoo"]
# l2 = ["Create", "a", "file", "yahoo.c"]

# print(l, l2)


# import pyttsx3
# import os

# machine = pyttsx3.init()

# print('say : ')

# app = input('APP:')

# if app == 'chrome' or app == 'google chrome':
#     os.system('chrome')
# elif app == 'telegram':
#     os.system('telegram-desktop')
# elif app == 'finder':
#     os.system('finder')
# elif app == 'firefox' or app == 'mozilla firefox' or app == 'mozilla':
#     os.system('firefox')
# elif app == 'android-studio':
#     os.system('')
# elif app == 'vs code':
#     os.system('code')
# elif app == 'pycharm':
#     os.system('')
