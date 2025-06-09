"""
Shared fixtures for analysis repositories.
"""
import pytest
from unittest.mock import MagicMock

@pytest.fixture(autouse=True)
def mock_env(monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "test")
    monkeypatch.setenv("BATCH_SIZE", "10")
