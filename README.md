# Backup System

A simple Python-based backup system that automatically backs up files from a specified folder, calculates file hashed, and stores metadata in a MySQL database. Supports versioning of files and includes tests.

---

## **Features**

- Scans a watch folder for new or modified files (manual scans for now)
- Creates timestamped backups of files
- Calculates SHA-256 hashed to detect changes
- Stores file metadata and backup history in MySQL
- Includes Dockerized MySQL for easy setup
- Makefile for running and testing
- Fully tested with 'pytest'

---

## **Project Structure**

```
backup-system/
│
├── src/
│   └── backup_system/
│       ├── __init__.py
│       ├── backup.py
│       ├── scanner.py
│       ├── hasher.py
│       ├── db.py
│       └── config.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_hash.py
│   ├── test_backup.py
│   └── test_scanner.py
│
├── Makefile
├── pytest.ini
├── requirements.txt
├── docker-compose.yml
├── init.sql
├── .env
└── README.md

```

---

## **Setup Instructions**

### 1. Clone the repository

git clone <your-repo-url>
cd backup-system

### 2. Create a .env file

#### Folder to watch

WATCH_FOLDER=/path/to/watch

#### Folder to backups

BACKUP_FOLDER=/path/to/backup

#### MySQL credentials

MYSQL_USER=backup_user
MYSQL_PASSWORD=backup_pass
MYSQL_DATABASE=backup_system

### 3. Install dependencies

pip install -r requirements.txt
or
pip3 install -r requirements.txt

### 4. Setup MySQL with Docker

docker-compose up -d

### 5. Run the backup system

make run

### 6. Run the tests

make test
