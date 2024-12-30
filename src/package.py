####
# Package only the relevant source for serving the site
####

import os
import subprocess
import json
from src.utils import copydir, copyfile

def package(version: str, build: bool):
    ## Create package dir
    if not os.path.isdir("./package"):
        os.mkdir("./package")

    ## Build the NODE source
    if build:
        subprocess.Popen(["npm", "install"]).wait()
        subprocess.Popen(["npm", "run", "build"]).wait()

    ## Get user defined included files/dirs
    user_config = {}
    if os.path.isfile("publish.json"):
        with open("publish.json") as f:
            user_config = json.load(f)

    basedir = "./"
    dirs = [
        "acf-json",
        "assets",
        "includes",
        "languages",
        "template-parts",
        "templates",

        ## Legacy
        "lib",
        "page-templates",
        "post-templates",
    ]

    ## Add user defined indluded dirs
    if "includeDirs" in user_config and isinstance(user_config["includeDirs"], list):
        dirs = list(set(dirs + user_config["includeDirs"]))

    ## All PHP files
    files = ["style.css", "style.min.css", "screenshot.png"]

    ## Add user defined indluded files
    if "includeFiles" in user_config and isinstance(user_config["includeFiles"], list):
        files = list(set(files + user_config["includeFiles"]))

    for f in os.listdir(basedir):
        if f.endswith(".php"):
            path = os.path.join(basedir, f)
            if not path in files:
                files.append(path)

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
