# Question: Explore the os Module to Work with Files and Directories Task: Write a Python program using the os module to list all the files and directories in the current directory.

import os

def list_files_and_directories():
    for item in os.listdir('.'):
        print(item)

list_files_and_directories()
