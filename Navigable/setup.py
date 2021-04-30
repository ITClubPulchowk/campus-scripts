# copy all file from the folder to ~/nable-bin | C:\nable-bin\ folder
# set the folder to path
import sys
import os
from os import system
import shutil

_arguments = "$2 $3 $4 $5 $6 $7 $9"
_fname = "t-nable"
_commandpath = ""
_ptfrm = "w"


def _fetch_essential():
    global _arguments, _cp, _com, _commandpath, _clear, _ptfrm

    if sys.platform.startswith("win"):
        _arguments = _arguments.replace("$", "%")
        _commandpath = f"C:\\nable-bin\\"
        _fname = "t-nable.bat"

        print("Preparing for windows")
        print(f"Environment to path;{_commandpath[1:]}")
        system(f'setx /m path "%PATH%;{_commandpath[1:]}"')
    else:
        _ptfrm = "l"
        _arguments += " ${10} ${11} ${12} ${13} ${14} ${15} ${16}"
        _commandpath = f"{os.environ['HOME']}/nable-bin/"
        __hasnbs(_commandpath)
        with open(f"{_commandpath}aliases", "w+") as a:
            a.writelines(
                [
                    "alias uprc='source ~/.bashrc'",
                ]
            )

        print("Preparing for linux")
        system(f"echo PATH=$PATH:{_commandpath}>>~/.bashrc")
        system(f"echo source {_commandpath}aliases>>~/.bashrc")


def __hasnbs(nbloc):
    if not os.path.exists(nbloc):
        os.makedirs(nbloc)


def _fetch_file_to_dir():
    _fetch_essential()
    global _arguments, _cp, _com, _commandpath, _clear, _ptfrm

    fcon = os.listdir(".")  # folder
    # print(fcon)
    # print(_commandpath)
    __hasnbs(_commandpath)

    for f in fcon:
        if os.path.isfile(f):
            shutil.copy(f, f"{_commandpath}{f}")
    if _ptfrm == "l":
        system(f"chmod +x {_commandpath}t-nable")

    print(f"Installation Complete!\nDataDir: {_commandpath}")


if __name__ == "__main__":
    _fetch_file_to_dir()