from backup_system.scanner import scan

def test_scan_calls_backup_file(tmp_path, monkeypatch):
    # Create fake watch folder
    watch = tmp_path / "watch"
    watch.mkdir()
    (watch / "a.txt").write_text("Alice")
    (watch / "b.txt").write_text("Bob")

    monkeypatch.setattr("backup_system.scanner.WATCH_FOLDER", str(watch))

    # Track calls to back_file
    called = []
    
    def fake_backup(path):
        called.append(path)
    
    monkeypatch.setattr("backup_system.scanner.backup_file", fake_backup)

    scan()

    assert len(called) == 2
    assert all(path.endswith(".txt") for path in called)