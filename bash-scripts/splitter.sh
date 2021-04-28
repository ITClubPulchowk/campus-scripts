# split files into chunks so that you can send files over a platform that
# only allows limited file upload size (ex, 8 MB in discord)

# packages/dependencies required: openssl (for encryption/decryption)

# SPLIT_FILE_EXTENSION is the extension you want your file to be split into
# CHUNK_SIZE defines the individual split file size
# PASSWORD is for encryption

# Create an empty directory and execute the split script:
#
#   ./file_splitter.sh -s <path-to-file-you-want-to-split>
#
# All the split files will be stored inside this empty directory.
# Important Note: The split files will be in the .txt format, 
# so make sure there are no other txt files in the directory initially 
# (all txt files will be purged midway using regex in the working directory).

# To re-assemble the file on the other side, simply use the command
#
#   ./file_splitter.sh -a
#
# inside the directory where you have placed all the file chunks.
# Same rule applies as to the splitting process, make sure that the directory 
# only contains the split files. Also, make sure the password is same on both sides.


#!/usr/bin/bash
set -euo pipefail
IFS=$'\n\t'

# variables you can change
SPLIT_FILE_EXTENSION=".txt"
CHUNK_SIZE=18000000
PASSWORD=password

function splitter(){
  if [ -z "$1" ] || [ $1 = "-s" ] 
  then
    echo "Missing Argument: No file path for the file to split"
    return 1
  fi

  local FILENAME=$1
  PREFIX=$(tr -dc A-Za-z0-9 < /dev/urandom | head -c 10 ; echo)

  split --bytes=$CHUNK_SIZE --additional-suffix=$SPLIT_FILE_EXTENSION -d $FILENAME $PREFIX
  
  SPLIT_FILES=$(ls | grep "$SPLIT_FILE_EXTENSION")

  mkdir fenc
  for file in $SPLIT_FILES
  do
    openssl enc -aes-256-cbc -base64 -pbkdf2 -iter 100000 -pass pass:$PASSWORD -in $file -out fenc/$file
  done

  rm *$SPLIT_FILE_EXTENSION 
  mv fenc/* ./
  rm -rf fenc
}

function assembler(){
  if [ -z "$1" ] || [ $1 = "-a" ] 
  then
    echo "Missing Argument: No file path for the file to split"
    return 1
  fi

  local FILENAME=$1
  SPLIT_FILES=$(ls | grep "$SPLIT_FILE_EXTENSION")

  mkdir fenc
  for file in $SPLIT_FILES
  do
    openssl enc -d -aes-256-cbc -base64 -pbkdf2 -iter 100000 -pass pass:$PASSWORD -in $file -out fenc/$file
  done
  
  rm *$SPLIT_FILE_EXTENSION 
  mv fenc/* ./
  rm -rf fenc

  cat *$SPLIT_FILE_EXTENSION > $FILENAME
  rm *$SPLIT_FILE_EXTENSION
}

function help_screen(){
  echo "./splitter.sh [FLAGS] [FILENAME]"
  echo "FLAGS:"
  echo "-a <filename>: Assemble split files and save as filename."
  echo "-s <filename>: Split file into encrypted chunks."
  echo "-h: To display the help screen."
}

while getopts sah flag
do
  case "${flag}" in
    s) splitter ${BASH_ARGV};;
    a) assembler ${BASH_ARGV};;
    h) help_screen;;
    ?) echo "incorrect flag passed";;
  esac
done
