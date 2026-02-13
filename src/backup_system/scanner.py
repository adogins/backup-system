import os
from backup_system.backup import backup_file
from backup_system.config import WATCH_FOLDER

def scan():
    """
    Scan the WATCH_FOLDER for files and back them up.

    Steps:
    1. Recursively scan through the files in WATCH_FOLDER
    2. Call backup_files() for each file
    """


    for root, _, files in os.walk(WATCH_FOLDER):
        for f in files:
            backup_file(os.path.join(root, f)) #  Make the path to the file and make a backup

if __name__ == "__main__":
    scan()