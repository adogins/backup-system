# Hashing detects changes through exact content comparison
import hashlib

def hash_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:  # reads in binary mode to ensure exact bytes get hashed
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()