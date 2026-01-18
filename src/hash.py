# Hashing detects changes through exact content comparison
import hashlib

# Compute and return SHA-256 hash of a file
# Args: path (str): Full path to the file
def hash_file(path):
    h = hashlib.sha256()  
    with open(path, "rb") as f:  # reads in binary mode to ensure exact bytes get hashed
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk) # Update hash with current chunk
    return h.hexdigest() # Return the final hash as a hexadecimal string