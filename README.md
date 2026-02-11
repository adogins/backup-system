# Backup System

A simple Python-based backup system that automatically backs up files from a specified folder, calculates file hashed, adn stores metadata in a MYSQL database. Supports versioning of files.

---

## **Features**

- Watches a folder for files (manual scans currently)
- Creates timestamped backups of files
- Calculates SHA-256 hashed to track changes
- Stored file metadata and backup history in MySQL
- Supports Dockerized MySQL for easy setup

---

## **Folder Structure**

```
backup-system/
├─ src/
│ ├─ backup.py          # Logic to copy files and store metadata
│ ├─ scanner.py         # Main script to scan the watch folder
│ ├─ hasher.py          # Computes SHA-256 hashes
│ ├─ db.py              # MySQL database connection
│ └─ config.py          # Configuration (paths & DB)
├─ .env                 # Environment variables (ignored by git)
├─ requirements.txt     # Python dependencies
├─ docker-compose.yml   # Docker configuration for MySQL
├─ init.sql             # SQL schema for database
└─ README.md
```

---

## **Setup Instructions**

### 1. Clone the repository

git clone <your-repo-url>
cd backup-system

### 2. Create a .env file

# Folder to watch

WATCH_FOLDER=/path/to/watch

# Folder to backups

BACKUP_FOLDER=/path/to/backup

# MYSQL credentials

MYSQL_USER=backup_user
MYSQL_PASSWORD=backup_pass
MYSQL_DATABASE=backup_system

### 3. Install dependencies

pip install -r requirements.txt
of
pip3 install -r requirements.txt

### 4. Setup MYSQL with Docker

docker-compose up -d

### 5. Run the backup system

python src/scanner.py
or
python3 src/scanner.py
