# File-Management

> Basic setup

```sh
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

> for working with michrophone

```sh
sudo apt-get install python3-pyaudio
```

pyaudio setup problem solution (Ubuntu OS) : [stackoverflow](https://stackoverflow.com/questions/20023131/cannot-install-pyaudio-gcc-error)

# Estimeted Blueprint (As of Now)

- Listen to michrophone
- text mining
- Write operations logic
- use data structure to store whole directory structure for optmising the operation
- create log file for whatever going on
- give voice feedback when process done

> Some more operations needs to be added like

```sh
compressing a folder (zip/tar)
uncompressing a file (unzip)
launching some popular applications installed on system
```

# Building standalone Executable file (linux/mac/windows)

```sh
source venv/bin/activate
pip install pyinstaller
pyinstaller -D -F -n main -c "main.py" --name filemanager --onefile
```

running above command will create two folders and one file as follows

- build [Folder]

```sh
build
└── filemanager
    ├── Analysis-00.toc
    ├── base_library.zip
    ├── EXE-00.toc
    ├── localpycos
    │   └── struct.pyo
    ├── PKG-00.pkg
    ├── PKG-00.toc
    ├── PYZ-00.pyz
    ├── PYZ-00.toc
    ├── warn-filemanager.txt
    └── xref-filemanager.html

2 directories, 10 files
```

- dist [Folder]

```sh
dist
└── filemanager

0 directories, 1 file
```

- filemanager.spec [File]

```sh
filemanager.spec
```
