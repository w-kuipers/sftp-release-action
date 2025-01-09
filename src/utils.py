import os
import shutil


def copydir(src: str):
    if os.path.isdir(src):
        shutil.copytree(src, os.path.join("./package", src))


def copyfile(src: str):
    if os.path.isfile(src):
        shutil.copyfile(src, os.path.join("./package", src))


def validate_arguments(args):
    if len(args) != 9:  # Including script name
        raise Exception(
            "Invalid number of arguments. Usage:\npython main.py <version> <host> <port> <user> <password> <path> <build> <protocol>"
        )

    _, build, protocol, version, host, port, user, password, path = args

    if not (version.startswith("p") or version.startswith("s")) or len(version) < 2:
        raise Exception(
            "Invalid version. Ensure the version starts with 'p' (e.g., v1.0.0)."
        )

    if not host:
        raise Exception(
            "Invalid host IP. Provide a valid IPv4 address (e.g., 192.168.1.1) or a URL"
        )

    if not port:
        raise Exception("Invalid port. Provide a valid integer")

    if not port.isnumeric():
        raise Exception("Invalid port. Provide a valid integer")

    if not user:
        raise Exception("Invalid user. Provide a valid SSH username.")

    if not password:
        raise Exception("Invalid password. Provide a valid SSH password.")

    if not path:
        raise Exception("Invalid path. Provide a valid distribution path.")

    if not protocol in ["ftp", "sftp"]:
        raise Exception("Protocol must be either 'ftp' or 'sftp'.")

    build = True if build == "--build" else False

    return build, protocol, version, host, int(port), user, password, path


def validate_path(path: str):

    p = os.path.normpath(path).split("/")

    if not p[-2] == "themes":
        raise Exception("This path does not seem to be a WordPess theme!")

    if not p[-3] == "wp-content":
        raise Exception("This path does not seem to be a WordPess theme!")
