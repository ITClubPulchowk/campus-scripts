# Replace blank space of folder names and filenames with hyphen

Python script to replace all the blank spaces of all the directories, sub-directories, and suitable files with hypen(-). <br>
The script will take action on all the child folders and the files of the directory from where the script is run.

It is a good idea to never use blank spaces for file and folder names.<br>
Site for explanation why we should avoid blank spaces,
https://www.mtu.edu/umc/services/websites/writing/characters-avoid/ <br>
Many people come to know about this lately, and it is a tedious work to rename all those files and folders one by one. <br>
This script makes the work easier. Run this script once, and it will rename the files and folders at once.

<br>

```
python _rename.py
```
Displays the help text for using the script.<br><br>

Some examples,
```
python _rename.py --kebab
```
Renames the files and the folders:<br>
python programs → python-programs<br>
Summer of '69.mp3 → Summer-of-'69.mp3<br>
OS module.txt → OS-module.txt<br>

<br>

``` 
python _rename.py --uppercamelkebab
```
Renames the files and the folders:<br>
python programs → Python-Programs<br>
Summer of '69.mp3 → Summer-Of-'69.mp3<br>
OS module.txt → OS-Module.txt<br>