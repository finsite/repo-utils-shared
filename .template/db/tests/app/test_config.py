"""
Unit tests for config.py
"""
def test_get_polling_interval(monkeypatch):
    from app import config
    monkeypatch.setenv("POLLING_INTERVAL", "10")
    assert config.get_polling_interval() == 10
