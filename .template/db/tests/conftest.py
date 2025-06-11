"""
Shared fixtures for tests
"""

from unittest.mock import MagicMock

import pytest


@pytest.fixture(autouse=True)
def mock_env(monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "test")
    monkeypatch.setenv("POLLING_INTERVAL", "5")
