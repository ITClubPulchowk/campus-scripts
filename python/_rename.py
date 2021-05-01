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
    Renames the files and the folders:
        python programs → python-programs
        Summer of '69.mp3 → Summer-of-'69.mp3
        OS module.txt → OS-module.txt

    Command: python _rename.py --uppercamelkebab
    Renames the files and the folders:
        python programs → Python-Programs
        Summer of '69.mp3 → Summer-Of-'69.mp3
        OS module.txt → OS-Module.txt
"""

import os
import argparse
import sys

cwd = os.getcwd()  # current working directory


def make_upper_camel_kebab(x):
    # convert test folder to Test-Folder
    strings = x.split()
    title_words = [a[0].upper() + a[1:] for a in strings]
    return "-".join(title_words)


def handle_exceptions(old_name, new_name):
    try:
        os.rename(old_name, new_name)
    except FileExistsError:
        print(f"Can't rename {old_name} to {new_name}.")
        print(f"{new_name} already exists.\n")
    except PermissionError:
        print(
            f"Can't rename {old_name}, it is being used by another process.\n")
    except FileNotFoundError:
        print(f"{old_name} not found")


def upper_camel_kebab(cwd):
    # Rename folders
    for dirpath, _, filenames in os.walk(cwd):
        # split the dirpath in "\"
        dir_in_list = dirpath.split("\\")

        # capitalize the first letter after each space
        # replace blank space with hyphen
        dir_in_list2 = []
        for s in dir_in_list:
            if " " in s:
                dir_in_list2.append(make_upper_camel_kebab(s))
            else:
                dir_in_list2.append(s)

        # join the list with "\" to get new dir name
        new_dirpath = "\\".join(dir_in_list2)

        # for renaming and exception handling
        handle_exceptions(dirpath, new_dirpath)

    # Rename files
    # File extension is checked to prevent messing with the system. If we change the filename of system files that may cause errors.
    extensions = (".pdf", ".doc", ".docx", ".xls", ".xlsx",
                  ".png", ".jpg", ".txt", ".mp4", ".mp3")
    for dirpath, _, filenames in os.walk(cwd):
        for f in filenames:
            # check the file extension
            if f.endswith(extensions):
                # full path of file
                filepath = os.path.abspath(os.path.join(dirpath, f))

                # split the filepath in "\"
                filepath_in_list = filepath.split("\\")

                # capitalize the first letter after each space
                # replace blank space with hyphen
                filepath_in_list2 = []
                for s in filepath_in_list:
                    if " " in s:
                        filepath_in_list2.append(make_upper_camel_kebab(s))
                    else:
                        filepath_in_list2.append(s)

                # join the list with "\" to get new dir name
                new_filepath = "\\".join(filepath_in_list2)

                # for renaming and handling exceptions
                handle_exceptions(filepath, new_filepath)


def kebab(cwd):
    # Rename folders
    for dirpath, _, filenames in os.walk(cwd):
        # replace the dir path blank spaces with hyphen
        new_dirpath = dirpath.replace(" ", "-")

        # for renaming and exception handling
        handle_exceptions(dirpath, new_dirpath)

    # Rename files
    # File extension is checked to prevent messing with the system. If we change the filename of system files that may cause errors.
    extensions = (".pdf", ".doc", ".docx", ".xls", ".xlsx",
                  ".png", ".jpg", ".txt", ".mp4", ".mp3")
    for dirpath, _, filenames in os.walk(cwd):
        for f in filenames:
            # check the file extension
            if f.endswith(extensions):
                filepath = os.path.abspath(os.path.join(dirpath, f))
                new_filepath = filepath.replace(" ", "-")

                # for renaming and handling exceptions
                handle_exceptions(filepath, new_filepath)


parser = argparse.ArgumentParser(allow_abbrev=False, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("--kebab",
                    help="The action will be taken on all the child folders and the files of the current directory.\n" +
                    "Rename all the folders and sub-folders, pdf files, text files, excel files, document files, media files as following:\n" +
                    "Summer of '69.mp3 → Summer-of-'69.mp3\n" +
                    "Python programs → Python-programs\n" +
                    "OS module.txt → OS-module.txt\n" +
                    "test teXt filE.txt → test-teXt-filE.txt",
                    action="store_true")

parser.add_argument("--uppercamelkebab",
                    help="The action will be taken on all the child folders and the files of the current directory.\n" +
                    "Rename all the folders and sub-folders, pdf files, text files, excel files, document files, media files as following:\n" +
                    "Summer of '69.mp3 → Summer-Of-'69.mp3\n" +
                    "Python programs → Python-Programs\n" +
                    "OS module.txt → OS-Module.txt\n" +
                    "test teXt filE.txt → Test-TeXt-FilE.txt",
                    action="store_true")

# For displaying help message even if no argument is passed
if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)
args = parser.parse_args()

if args.kebab:
    kebab(cwd)
elif args.uppercamelkebab:
    upper_camel_kebab(cwd)
