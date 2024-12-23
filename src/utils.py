import shutil
import os

def copydir(src: str):
    if os.path.isdir(src):
        shutil.copytree(src, os.path.join("./package", src))

def copyfile(src: str):
    if os.path.isfile(src):
        shutil.copyfile(src, os.path.join("./package", src))
