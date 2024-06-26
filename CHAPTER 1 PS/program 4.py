import os

# specify directory path
dir_path = '/'

# list all files and directories
content = os.listdir(dir_path)

for item in content:
    print(item)