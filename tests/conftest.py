import pytest

@pytest.fixture
def fake_db(monkeypatch):
    class FakeCursor:
        def execute(self, *args, **kwargs):
            pass

        def fetchone(self):
            return [1] # Pretend file_id = 1
        
    class FakeConn:
        def cursor(self):
            return FakeCursor()
        
        def commit(self):
            pass

        def close(self):
            pass
    
    # Patch backup.get_connection to return the fake DB
    monkeypatch.setattr("backup_system.backup.get_connection", lambda: FakeConn())