from backup_system.hash import hash_file
import pytest

def test_hash_changes_when_file_changes(tmp_path):
    file = tmp_path / "a.txt"
    file.write_text("hello")
    h1 = hash_file(str(file))

    file.write_text("hello world")
    h2 = hash_file(str(file))

    assert h1 != h2

def tets_hash_same_content_same_hash(tmp_path):
    file1 = tmp_path / "a.txt"
    file2 = tmp_path / "b.txt"

    file1.write_text("This is some text")
    file2.write_text("This is some text")

    assert hash_file(str(file1)) == hash_file(str(file2))

def test_hash_missing_file_raises():
    with pytest.raises(FileNotFoundError):
        hash_file("dne.txt")