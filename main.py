import sys

from src.clean import clean_dest_ftp, clean_dest_sftp
from src.package import package
from src.upload import upload_source
from src.utils import validate_arguments, validate_path


def main():
    print(sys.argv)
    build, protocol, version, host, port, user, password, path = validate_arguments(
        sys.argv
    )

    ## The path must be a WordPress theme location
    validate_path(path)

    package(version, build)
    # if protocol == "ftp":
    #     clean_dest_ftp(host, port, user, password, path)
    # else:
    clean_dest_sftp(host, port, user, password, path)

    upload_source("./package", path, host, port, user, password)


if __name__ == "__main__":
    main()
