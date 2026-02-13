import os
from dotenv import load_dotenv # For reading variables from .env

load_dotenv() 

# Get the folder to watch for files to backup
WATCH_FOLDER = os.getenv("WATCH_FOLDER")

# Get the folder that stores backups
BACKUP_FOLDER = os.getenv("BACKUP_FOLDER")

# Ensure that WATCH_FOLDER and BACKIP_FOLDER have their paths set
if not WATCH_FOLDER or not BACKUP_FOLDER:
    raise RuntimeError("WATCH_FOLDER and BACKUP_FOLDER must be set")

# Ensure that WATCH_FOLDER and BACKUP_FOLDER exist
# Create the folders if they don't exist
os.makedirs(WATCH_FOLDER, exist_ok=True)
os.makedirs(BACKUP_FOLDER, exist_ok=True)

# MySQL configuration from .env
DB_CONFIG = {
    "host": "localhost",
    "user": os.getenv("MYSQL_USER", "backup_user"),
    "password": os.getenv("MYSQL_PASSWORD", "backup_pass"),
    "database": os.getenv("MYSQL_DATABASE", "backup_system"),
    "port": 3306,
}