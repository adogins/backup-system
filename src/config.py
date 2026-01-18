import os
from dotenv import load_dotenv

load_dotenv()  # loads .env into environmnet variables

WATCH_FOLDER = os.getenv("WATCH_FOLDER")
BACKUP_FOLDER = os.getenv("BACKUP_FOLDER")

if not WATCH_FOLDER or not BACKUP_FOLDER:
    raise RuntimeError("WATCH_FOLDER and BACKUP_FOLDER must be set")

os.makedirs(WATCH_FOLDER, exist_ok=True)
os.makedirs(BACKUP_FOLDER, exist_ok=True)

DB_CONFIG = {
    "host": "localhost",
    "user": os.getenv("MYSQL_USER", "backup_user"),
    "password": os.getenv("MYSQL_PASSWORD", "backup_pass"),
    "database": os.getenv("MYSQL_DATABASE", "backup_system"),
    "port": 3306,
}