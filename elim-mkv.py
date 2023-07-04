import os
import sys

# get path of current working directory
path = os.getcwd()
 
# get every file within directory
files = os.scandir(path)


#for every file
for file in files:
    curr_name = file.name.split('.') #split files by '.'

    if curr_name[-1] == 'mkv': #if the last split segment is 'mkv' we know to delete this file
        os.remove(file.path)