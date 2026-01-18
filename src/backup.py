import os, shutil
from datetime import datetime
from db import get_connection
from hash import hash_file
from config import BACKUP_FOLDER

def backup_file(path):
    name = os.path.basename(path)
    ts = datetime.now().strftime("%Y%m%d%H%M%S")
    dest = os.path.join(BACKUP_FOLDER, f"{ts}_{name}")
    shutil.copy2(path, dest)

    file_hash = hash_file(path)
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO files (file_path, file_hash, last_modified, last_backup)
        VALUES (%s, %s, NOW(), NOW())
        ON DUPLICATE KEY UPDATE file_hash=%s, last_backup=NOW()
    """, (path, file_hash, file_hash))

    cursor.execute("SELECT id FROM files WHERE file_path=%s", (path,))
    file_id = cursor.fetchone()[0]

    cursor.execute("""
        INSERT INTO file_versions (file_id, backup_path, file_hash, backed_up_at)
        VALUES (%s, %s, %s, NOW())
    """, (file_id, dest, file_hash))

    conn.commit()
    conn.close()