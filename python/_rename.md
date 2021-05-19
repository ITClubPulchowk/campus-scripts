# Replace blank space of file and folder names with hyphen

## Description
Python script to replace all the blank spaces of all the directories, sub-directories, and suitable files with hypen(-). <br>
The script will take action on all the child folders and the files of the directory from where the script is run.

It is a good idea to never use blank spaces for file and folder names.<br>
Site for explanation why we should avoid blank spaces,
https://www.mtu.edu/umc/services/websites/writing/characters-avoid/ <br>
Many people come to know about this lately, and it is a tedious work to rename all those files and folders one by one. <br>
This script makes the work easier. Run this script once, and it will rename the files and folders at once.

---

## Prerequisite

[Download and install Python](https://www.python.org/downloads/)

---

## Usage
```
python _rename.py
```
Displays the help text for using the script.

---

```
python _rename.py --kebab
```
Renames only the files and the folders of the working directory:<br>
python programs → python-programs<br>
Summer of '69.mp3 → Summer-of-'69.mp3<br>
OS module.txt → OS-module.txt<br>

---

``` 
python _rename.py --uppercamelkebab
```
Renames only the files and the folders of the working directory:<br>
python programs → Python-Programs<br>
Summer of '69.mp3 → Summer-Of-'69.mp3<br>
OS module.txt → OS-Module.txt<br>

---

### Flags:
Use --recurse flag for depth renaming
``` 
python _rename.py --kebab --recurse
```
kebab renaming for all the child folders and directories of the working directory.

---

``` 
python _rename.py --uppercamelkebab --recurse
```
Upper-Camel-Kebab renaming for all the child folders and directories of the working directory.
