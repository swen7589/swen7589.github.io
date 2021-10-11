print('hello world')

# absolute path - path that works anywhere, references the file no matter where you're located
# /Users/swenihueze/Documents/GitHub/swen7589.github.io/weeksix/classwork.py

# the computer always converts relative paths to absolute to access a file

# pwd - print working directory
# working directory is where you are located
# directory is a folder

# put the working directory at the beginning of the relative path to make the absolute path

# cd - change directory

# cd .. - go out of the folder 

# with open('path_to_file') as f:
#   text = f.read()
# print(text)

# if you make a file, insert name of file into ' ' (where path_to_file is)
# the .read() function reads the file (the characters, not just string) and prints it out

# folder/ - to get to file in different folder, put that into ' ' (before path_to_file)

# import os         # os = operating system

# os.getcwd()       # cwd = current working directory
# returns string of working directory

# Rule 1: know your working directory
# Rule 2: know your file encoding

# encoding = utf-8 (default on mac)

# put the encoding after ' ' in with open()

# if you use the open function, you must specify the encoding




