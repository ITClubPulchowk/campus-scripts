"""
    Python script to replace blank space from the name of directories, sub-directories, and appropriate files with hyphen.
    The script will take action on all the child folders and the files of the current directory.
    It will rename only the PDF, Excel, Document, PNG, JPG, TXT, MP4, MP3 files, and folders and sub-directories.

    Blank spaces in folder names and filenames are good to be avoided.
    Site for explanation why we should avoid blank spaces,
    https://www.mtu.edu/umc/services/websites/writing/characters-avoid/

    Reference for argparse:
    https://docs.python.org/3/howto/argparse.html#id1

    Place this script in the directory whose sub-folders, files and sub-files you want to rename.
    Change the working directory in command line to this directory and run the python command;

    Some examples,

    Command: python _rename.py --kebab
    Renames only the folders and files of the current directory:
        python programs → python-programs
        Summer of '69.mp3 → Summer-of-'69.mp3
        OS module.txt → OS-module.txt

    Command: python _rename.py --uppercamelkebab
    Renames only the folders and files of the current directory:
        python programs → Python-Programs
        Summer of '69.mp3 → Summer-Of-'69.mp3
        OS module.txt → OS-Module.txt

    Flags:
    Use --recurse flag for depth renaming
    Example: 
    python _rename.py --kebab --recurse
    kebab renaming for all the child directories and files of the current directory.
    
    python _rename.py --uppercamelkebab --recurse
    Upper-Camel-Kebab renaming for all the child directories and files of the current directory.
"""

import os
import argparse
import platform
import sys

# uppercamelkebab support for Linux
file_separator = "\\"
if platform.system() == "Linux":
    file_separator = "/"

cwd = os.getcwd()  # current working directory

# File extension is checked to prevent messing with the system. If we change the filename of system files that may cause errors.
extensions = (".pdf", ".doc", ".docx", ".xls", ".xlsx",
              ".png", ".jpg", ".txt", ".mp4", ".mp3")


def make_upper_camel_kebab(x):
    # convert
    # \\python programming\\hello world\\hello world.txt to
    # \\Python-Programming\\Hello-World\\Hello-World.txt
    dir_in_list = x.split(file_separator)
    titled_path = ""
    for s in dir_in_list:
        if " " in s:
            strings = s.split()
            titled_words = [a.capitalize() for a in strings]
            titled_path += file_separator + "-".join(titled_words)
        else:
            titled_path += file_separator + s

    # rstrip is for handling error renaming the working directory
    return titled_path.rstrip(file_separator)


def try_rename(old_name, new_name):
    # handle FileExistsError
    if os.path.exists(new_name) and old_name != new_name:
        print(f"Can't rename {old_name} to {new_name}.")
        print(f"{new_name} already exists.\n")
        return

    try:
        os.rename(old_name, new_name)
    except PermissionError:
        print(
            f"Can't rename {old_name}, it is being used by another process.\n")
    except FileNotFoundError:
        print(f"{old_name} not found")


def rename(cwd):
    # rename only directories and files of the current directory
    if not args.recurse:
        # only the dirs and files of the current directory
        dirs_files = os.listdir(cwd)
        dirnames = [item for item in dirs_files if os.path.isdir(item)]
        filenames = [item for item in dirs_files if os.path.isfile(item)]

        for dirname in dirnames:
            if args.kebab:
                new_dirname = dirname.replace(" ", "-")
                try_rename(dirname, new_dirname)

            elif args.uppercamelkebab:
                if " " in dirname:
                    strings = dirname.split()
                    titled_words = [a.capitalize() for a in strings]
                    new_dirname = "-".join(titled_words)
                    try_rename(dirname, new_dirname)

        for filename in filenames:
            if filename.endswith(extensions):
                if args.kebab:
                    new_filename = filename.replace(" ", "-")
                    try_rename(filename, new_filename)
                elif args.uppercamelkebab:
                    if " " in filename:
                        strings = filename.split()
                        titled_words = [a.capitalize() for a in strings]
                        new_filename = "-".join(titled_words)
                        try_rename(filename, new_filename)
        return

    # Depth renaming
    # Rename folders
    dirpaths = [x[0] for x in os.walk(cwd)]

    for dirpath in dirpaths:
        # prevent renaming the parent directory
        child = dirpath.replace(cwd, "")

        if not os.path.exists(dirpath):
            last_index = child.rfind("\\")  # index of the last backslash
            part1 = child[:last_index]
            part2 = child[last_index:]
            if args.kebab:
                dirpath = cwd + part1.replace(" ", "-") + part2
            elif args.uppercamelkebab:
                dirpath = cwd + make_upper_camel_kebab(part1[1:]) + part2

        if args.kebab:
            new_dirpath = cwd + child.replace(" ", "-")
        elif args.uppercamelkebab:
            new_dirpath = cwd + make_upper_camel_kebab(child[1:])

        # for renaming and exception handling
        try_rename(dirpath, new_dirpath)

    # Rename files
    for dirpath, _, filenames in os.walk(cwd):
        for f in filenames:
            # check the file extension
            if f.endswith(extensions):
                filepath = os.path.join(dirpath, f)

                # prevent renaming the parent directory
                child = filepath.replace(cwd, "")

                if not os.path.exists(filepath):
                    # index of the last backslash
                    last_index = child.rfind("\\")
                    part1 = child[:last_index]
                    part2 = child[last_index:]
                    if args.kebab:
                        filepath = cwd + part1.replace(" ", "-") + part2
                    elif args.uppercamelkebab:
                        filepath = cwd + \
                            make_upper_camel_kebab(part1[1:]) + part2

                if args.kebab:
                    new_filepath = cwd + child.replace(" ", "-")
                elif args.uppercamelkebab:
                    new_filepath = cwd + make_upper_camel_kebab(child[1:])

                # for handling escape character in path
                new_filepath.replace("\\", "/")

                # for renaming and exception handling
                try_rename(filepath, new_filepath)


parser = argparse.ArgumentParser(
    allow_abbrev=False, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("--kebab",
                    help="The action will be taken on only the folders and the files of the current directory.\n" +
                    "Rename all the folders, pdf files, text files, excel files, document files, media files as following:\n" +
                    "Summer of '69.mp3 → Summer-of-'69.mp3\n" +
                    "Python programs → Python-programs\n" +
                    "OS module.txt → OS-module.txt\n" +
                    "test teXt filE.txt → test-teXt-filE.txt",
                    action="store_true")

parser.add_argument("--uppercamelkebab",
                    help="The action will be taken on only the folders and files of the current directory.\n" +
                    "Rename all the folders, pdf files, text files, excel files, document files, media files as following:\n" +
                    "Summer of '69.mp3 → Summer-Of-'69.mp3\n" +
                    "Python programs → Python-Programs\n" +
                    "OS module.txt → OS-Module.txt\n" +
                    "test teXt filE.txt → Test-TeXt-FilE.txt",
                    action="store_true")

parser.add_argument("--recurse",
                    help="Depth renaming\n" +
                    "Rename all the child folders and files of the current directory.\n",
                    action="store_true")

# For displaying help message even if no argument is passed
if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)
args = parser.parse_args()

if args.kebab and args.uppercamelkebab:
    print("Please add only one rename case flag.")
    sys.exit(1)

if args.recurse and not (args.kebab or args.uppercamelkebab):
    print("Please use a rename case flag.")
    sys.exit(1)

if args.kebab or args.uppercamelkebab:
    rename(cwd)
