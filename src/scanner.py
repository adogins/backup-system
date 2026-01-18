import os
from backup import backup_file
from config import WATCH_FOLDER

def scan():
    for root, _, files in os.walk(WATCH_FOLDER):
        for f in files:
            backup_file(os.path.join(root, f))

if __name__ == "__main__":
    scan()