"""
Shared fixtures for analysis repositories.
"""

from unittest.mock import MagicMock

import pytest


@pytest.fixture(autouse=True)
def mock_env(monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "test")
    monkeypatch.setenv("BATCH_SIZE", "10")
