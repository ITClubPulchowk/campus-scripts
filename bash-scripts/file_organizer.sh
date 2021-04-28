# to clean up your messy downloads folder

# you can either sort by file names (first letter) and place it in 
# respective alphabetical directories, or sort by file extension

# Move the script to a folder where you want to organize the files.
# 
# ./file_organizer -[FLAG]
# 
# Flags:
# 
# a : To organize files within a folder by name (alphabetically)
# e : To organize files within a folder by extension
# h : To display help screen

#!/bin/bash

function organize_by_extension(){
  FILE_EXTENSIONS=$(find . -maxdepth 1 -type f  | 
    (awk -F . '{print $NF}') | 
    (sort -u))

  for extension in ${FILE_EXTENSIONS[@]}
  do
    mkdir $extension
    mv *.$extension ./$extension
  done
}

function organize_by_name(){
  F_NAMES=$(find -maxdepth 1 -type f | 
    (awk -F . '{print $2}') | 
    (awk -F / '{print substr($NF,1,1)}') | 
    (tr "[:lower:]" "[:upper:]") |
    (sort -u)) 

  for starting_char in ${F_NAMES[@]}
  do 
    mkdir $starting_char
    lower=$(echo "$starting_char" | tr '[:upper:]' '[:lower:]')
    mv `find -maxdepth 1 -type f | grep "./[$lower$starting_char]"` $starting_char
  done
}

function help_screen(){
  echo "This script organizes files within a directory into sub-directories."
  echo "FLAGS:"
  echo "-a: To organize files within a folder by name (alphabetically)"
  echo "-e: To organize files within a folder by extension"
  echo "-h: To display the help screen"
}

while getopts aeh flag
do
  case "${flag}" in
    e) organize_by_extension;;
    a) organize_by_name;;
    h) help_screen;;
    ?) echo "incorrect flag passed";;
  esac
done

exit 0
