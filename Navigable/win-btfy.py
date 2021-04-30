import argparse
import os
import collections
from os import system
import re

from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument(
    "-f",
    "--folder",
    default=".",
    help="Specifies which folder to make the  naviagtable bat file",
)
parser.add_argument(
    "-n",
    "--name",
    default="jump",
    help="Specifies what is the name of the bat file, other wise it adds to the jump.bat",
)
parser.add_argument(
    "-r",
    "--recursive",
    default=0,
    help="Specifies if we want: to make navigation recursive to all the folders recursively",
)
parser.add_argument(
    "-j",
    "--injump",
    default=0,
    help="Specifies if we want: to make navigation inside jump command",
)
parser.add_argument(
    "-c",
    "--code",
    default=0,
    help="Specifies if we want: to add open in code options for the base folder ",
)
parser.add_argument(
    "-s",
    "--start",
    default=0,
    help="Specifies if we want: to add open in file manager options for the base folder ",
)
args = parser.parse_args()
__name__ = args.name
_name = f"C:\\nable-bin\{args.name}.bat"  # shotcut batch file
_folder = args.folder
_r = args.recursive
_code = int(args.code)
_jump = args.injump
_start = int(args.start)
_fPath = os.path.abspath(_folder)
__help__ = f""" if "%{2 if args.name == "jump" else 1:d}"  == "-h" (\n \necho Shortcut for the Folder are\necho {"":=<70}"""
__taken__ = defaultdict(bool)  # <-- name is taken
__initial__ = defaultdict(int)
"""
./ds/hon/stat
      py
      scikit
./ds/tf/dl/relu
           conv
        /ml/lr
           /mr
        /stat/
# --> ds .honstat ds ..py  ds ..scikit ..dl ..ml .tfstat
# --> ds ...relu
#  so for conflict resolution we expand the dot

"""


def check():
    if _jump:

        if __name__ == "jump":
            raise Exception(
                "Warning: Jump Flag raised but no name specified!\n----------> -j 1\nYou must specifie name option as\n----------> -j 1 -n XXXX"
            )


"""---------------------------Code generator---------------------------"""


"""________________folder extraction _______________"""


def __explore(r: int) -> list:

    if r:
        for root, _, _ in os.walk(_folder):
            if not root.startswith(".\."):
                yield f"{os.getcwd()}\{root.lstrip('.')}".replace("\\\\", "\\")

    else:

        for entry in os.scandir(_folder):
            if not entry.is_file() and not entry.name.startswith("."):
                yield f"{os.getcwd()}\{entry.name}"


"""________________folder processing_______________"""


def __process(fPath: str):

    _rel = os.path.relpath(fPath)
    _lvl = __gtLvl(_rel)
    _ret = ""
    if _lvl == ".":
        _ret = __gt(fPath)
    elif _lvl < "..." and _lvl > ".":
        _ret = __gt(fPath, 0)

    return _ret


"""________________code gen_______________"""


def __gt(fPath: str, lvl1=True):

    _name = __gtName(fPath)
    _rel = os.path.relpath(fPath)
    _lvl = __gtLvl(_rel) if not lvl1 else ""
    _ret = f""" if "%{__gtScope():d}" == "{_lvl}{_name}" (
            cd /d  "{fPath}"
            {__code(__gtScope()+1,fPath)}
            {__start(__gtScope()+1,fPath)}
    )


     """
    global __help__
    __help__ += f"\necho {_lvl}{_name:-<50}{_rel}"
    return _ret


def __gtScope() -> int:
    return 2 if args.name == "jump" else 1


def __gtLvl(relPath: str) -> str:
    _l = len(relPath.split("\\"))
    _lvl = ""
    for _ in range(_l):
        _lvl += "."
    return _lvl


"""---------------------------Options---------------------------"""


"""________________code_______________"""


def __gtCode(path: str) -> str:
    _ret = f""" code "{os.path.abspath(path)}"
    """
    return _ret


def __code(scope: int, path: str = _fPath, rflg: int = 0) -> str:
    _ret = ""
    if _code == 1:
        _ret = f""" if "%{scope}" == "c"  (
            cd /d "{path}"
         {__gtCode(path)}
         )
     """
        _ret = _ret if not rflg == 1 else ""

    elif _code == 2:
        _ret = __gtCode(path)
        _ret = _ret if not rflg == 2 else ""

    return _ret


"""________________start_______________"""


def __gtStart(path: str) -> str:
    _ret = f""" start .
    """
    return _ret


def __start(scope: int, path: str = _fPath, rflg=0) -> str:
    _ret = ""
    if _start == 1:
        _ret = f""" if "%{scope}" == "s"  (
            cd /d "{path}"
         {__gtStart(path)}
         )
     """
        _ret = _ret if not rflg == 1 else ""

    elif _start == 2:
        _ret = __gtStart(path)

        _ret = _ret if not rflg == 2 else ""
    return _ret


"""---------------------------Process name---------------------------"""


def __gtName(relPath: str) -> str:
    global __taken__
    _items = relPath.rsplit("\\", 1)
    name = _items[1] if (len(_items) > 1) else relPath

    _commons = defaultdict(str)
    for k, v in {
        "argument": "arg",
        "git": "git",
        "arguments": "args",
        "basics": "bsc",
        "utilities": "utils",
        "fuctions": "funcs",
        "database": "db",
        "numpy": "np",
        "io": "io",
        "string": "str",
        "function": "fucn",
        "utility": "util",
        "oop": "oop",
        "networking": "net",
    }.items():
        _commons[k] = v
    name = name.lstrip(".")
    _ret = _commons[name.lower()]
    _pat = r"^[A-Za-z0-9]|\s[A-Za-z]|[A-Z]|[0-9]{,2}$|_[a-zA-Z]"
    _mtchs = re.findall(_pat, name)
    _ret = (
        "".join(_mtchs[:5]).replace(" ", "").replace("_", "").lower()
        if _ret == ""
        else _ret
    )
    """               ___Note:For Name collision___               """

    if __taken__[_ret]:
        __initial__[_ret] += 1
        _ret = f"{_ret}{__initial__[_ret]}"
    else:
        __taken__[_ret] = True
    return _ret


"""---------------------------Final draft---------------------------"""

"""________________basics root folder and option_______________"""


def __bsc_op(iflg: int = 0) -> str:

    _ret = ""
    _ret += f""" 
                cd /d "{_fPath}"     
                {__start(2, _fPath, 1)}
                {__code(2, _fPath, 1)}
            """
    _ret = (
        f""" if "%2" == "" (
                            {_ret}
                        ) """
        if iflg
        else f""" 
                        if "%1" == "" (
                            {_ret}  
                          
                        )
                         """
    )
    _ret = f""" 
            {_ret}
            {__start(1, _fPath, 2)}
            {__code(1, _fPath, 2)}
     """

    return _ret


def __gtWrite(_data: str):
    global __help__
    _write = ""
    if __name__ == "jump":
        _write += f"""
       \n\n
     \rREM {'':-<30} {__gtName(_fPath)} {'':-<30}

        if "%1" == "-{__gtName(_fPath) if not _jump else __name__ }" (

          {__bsc_op(1)}
          {_data}
          {__help__}

        )
         """
    else:
        _write += f"""
    \r@echo off\n


        {__bsc_op()}
        {_data}
        {__help__}
         """
    return _write


"""---------------------------Execution code---------------------------"""


def __cached(data: str) -> None:
    if os.path.exists(_name) and __name__ == "jump":
        with open(_name, "a") as file:
            file.write(data)
    else:
        with open(_name, "w") as file:
            file.write(data)


def __main__():
    check()

    _data = ""
    global __main__
    global __help__
    for pth in __explore(_r):
        _data += __process(pth) + "\n"
    __help__ += f"\necho {'':=<70} \n)"

    __cached(__gtWrite(_data))


try:
    __main__()
except Exception as e:
    print(e)
