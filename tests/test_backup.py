from backup_system.backup import backup_file

def test_backup_creates_file(tmp_path, monkeypatch, fake_db):
    # Create fake backup folder
    backup_dir = tmp_path / "backups"
    backup_dir.mkdir()

    # Patch BACKUP_FOLDER to point to the fake folder
    monkeypatch.setattr("backup_system.backup.BACKUP_FOLDER", str(backup_dir))

    # Create a file to backup
    file = tmp_path / "a.txt"
    file.write_text("hello")

    backup_file(str(file))

    # Ensure exactly one backup file exists
    files = list(backup_dir.iterdir())
    assert len(files) == 1
    assert files[0].name.endswith("_a.txt")