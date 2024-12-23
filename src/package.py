####
# Package only the relevant source for serving the site
####

import os
import subprocess
import sys
from src.utils import copydir, copyfile

## Get version number
if len(sys.argv) == 1 or not sys.argv[1][0] == "p" or not sys.argv[1][0] == "p":
    print("No valid version supplied.")
    exit()
else:
    version = sys.argv[1]

## Create package dir
if not os.path.isdir("./package"):
    os.mkdir("./package")

## Build the NODE source
subprocess.Popen(["npm", "install"]).wait()
subprocess.Popen(["npm", "run", "build"]).wait()

basedir = "./"
dirs = [
    "acf-json",
    "assets",
    "includes",
    "lib",
    "languages",
    "template-parts",
    "templates"
]

## All PHP files
files = ["style.css", "screenshot.png"]
for f in os.listdir(basedir):
    if f.endswith(".php"):
        files.append(os.path.join(basedir, f))

for dir in dirs:
    copydir(dir)
    
for file in files:
    copyfile(file)


style_path = os.path.join(basedir, "package", "style.css")
with open(style_path, "r") as file:
    lines = file.readlines()

for i, line in enumerate(lines):
    if "Version:" in line:
        print(version)
        lines[i] = f"    Version: {version[1:]}\n"

with open(style_path, "w") as file:
    file.writelines(lines)
