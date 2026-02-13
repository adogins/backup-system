import os, shutil
from datetime import datetime
from backup_system.hash import hash_file
from backup_system.db import get_connection
from backup_system.config import BACKUP_FOLDER

def backup_file(path):
    """
    Back up a single file to the backup folder and update the database.

    Steps:
    1. Generate a timestamped backup file name
    2. Copy the original file into the backup folder
    3. Calculate SHA-256 has of the file
    4. Insert or update metadata in the files table
    5. Inser backup record in file_versions table
    """

    # Get filename from the path
    name = os.path.basename(path)

    # Get a timestamp for the backup file
    ts = datetime.now().strftime("%m%d%Y%H%M%S")

    # Make a destination path in the backup folder
    dest = os.path.join(BACKUP_FOLDER, f"{ts}_{name}")

    # Copy the file to the backup folder and preserve metadata
    shutil.copy2(path, dest)

    # Compute SHA-256 hash to detect changes in the file
    file_hash = hash_file(path)

    # Connect to database
    conn = get_connection()
    cursor = conn.cursor()

    # Insert or update file metadata in files table
    cursor.execute("""
        INSERT INTO files (file_path, file_hash, last_modified, last_backup)
        VALUES (%s, %s, NOW(), NOW())
        ON DUPLICATE KEY UPDATE file_hash=%s, last_backup=NOW()
    """, (path, file_hash, file_hash))

    # Get file_id
    cursor.execute("SELECT id FROM files WHERE file_path=%s", (path,))
    file_id = cursor.fetchone()[0]

    # Determine version number
    cursor.execute("SELECT COUNT(*) FROM file_versions WHERE file_id=%s", (file_id,))
    version = cursor.fetchone()[0] + 1

    # build backup filename: <filename>_<MMDDYYYY>_v<version>
    date_str = datetime.now().strftime("%m%d%Y")
    backup_name = f"{name}_{date_str}_v{version}"
    dest = os.path.join(BACKUP_FOLDER, backup_name)

    # Copy file to backup folder
    shutil.copy2(path, dest)

    # Insert version record
    cursor.execute("""
        INSERT INTO file_versions (file_id, backup_path, file_hash, backed_up_at)
        VALUES (%s, %s, %s, NOW())
    """, (file_id, dest, file_hash))

    # Commit changes to database
    conn.commit()

    # Close database connection
    conn.close()