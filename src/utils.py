import shutil
import os

def copydir(src: str):
    if os.path.isdir(src):
        shutil.copytree(src, os.path.join("./package", src))

def copyfile(src: str):
    if os.path.isfile(src):
        shutil.copyfile(src, os.path.join("./package", src))

def validate_arguments(args):
    if len(args) != 8:  # Including script name
        print("Invalid number of arguments. Usage:")
        print("python main.py <version> <host> <port> <user> <password> <path> <--build>")
        exit(1)

    _, version, host, port, user, password, path, build = args


    if not version.startswith("p") or len(version) < 2:
        print("Invalid version. Ensure the version starts with 'p' (e.g., v1.0.0).")
        exit(1)

    if not host:
        print("Invalid host IP. Provide a valid IPv4 address (e.g., 192.168.1.1) or a URL")
        exit(1)

    if not port:
        print("Invalid port. Provide a valid integer")
        exit(1)

    if not user:
        print("Invalid user. Provide a valid SSH username.")
        exit(1)

    if not password:
        print("Invalid password. Provide a valid SSH password.")
        exit(1)

    if not path:
        print("Invalid path. Provide a valid distribution path.")
        exit(1)

    build = True if build == "--build" else False

    return version, host, port, user, password, path, build

def validate_path(path: str):

    p = os.path.normpath(path).split("/")

    if not p[-2] == "themes":
        raise Exception("This path does not seem to be a WordPess theme!")

    if not p[-3] == "wp-content":
        raise Exception("This path does not seem to be a WordPess theme!")

