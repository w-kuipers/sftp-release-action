import sys
from src.package import package
from src.clean import clean_dest
from src.utils import validate_arguments, validate_path

def main():
    version, host, port, user, password, path = validate_arguments(sys.argv)
    
    ## The path must be a WordPress theme location
    validate_path(path)

    package(version)
    clean_dest(host, port, user, password, path)

if __name__ == "__main__":
    main()
