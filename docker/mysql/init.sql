CREATE TABLE files (
    id INT AUTO_INCREMENT PRIMARY KEY,
    file_path TEXT NOT NULL,
    file_hash CHAR(64) NOT NULL,
    last_modified DATETIME NOT NULL,
    last_backup DATETIME NOT NULL,
    UNIQUE KEY unique_file (file_path(255))
);

CREATE TABLE file_versions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    file_id INT NOT NULL,
    backup_path TEXT NOT NULL,
    file_hash CHAR(64) NOT NULL,
    backed_up_at DATETIME NOT NULL,
    FOREIGN KEY (file_id) REFERENCES files(id)
);