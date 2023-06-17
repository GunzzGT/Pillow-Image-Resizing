import os
from pathlib import Path

def open_bulk (path):
    directory_name = r"{}".format(path)
    file_list = []
    for (root, dirs, files) in os.walk(directory_name):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def open_single():
    path = Path('./dump')
    #path = Path.cwd().parent / 'dump'
    print(path)
    file_list = []
    for (root,dirs,files) in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list