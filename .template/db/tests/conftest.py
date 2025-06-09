"""
Shared fixtures for tests
"""
import pytest
from unittest.mock import MagicMock

@pytest.fixture(autouse=True)
def mock_env(monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "test")
    monkeypatch.setenv("POLLING_INTERVAL", "5")
