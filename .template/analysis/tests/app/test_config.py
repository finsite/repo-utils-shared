"""
Test for config.py in analysis repositories.
"""


def test_get_batch_size(monkeypatch):
    from app import config

    monkeypatch.setenv("BATCH_SIZE", "20")
    assert config.get_batch_size() == 20
