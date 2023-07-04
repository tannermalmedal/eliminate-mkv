import os
import sys

# path = sys.argv[0]
# path = __file__

# path = path.split()
cheese = 'cheese'

path = os.getcwd()
# gg_path = 'E:\GG FOOTAGE'

###WORKING
# curr_path_info = os.scandir('/mnt/e/GG FOOTAGE') 

files = os.scandir(path)

for file in files:
    curr_name = file.name.split('.')

    if curr_name[-1] == 'mkv':
        os.remove(file.path)