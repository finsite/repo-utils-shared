import os

import pytest

from app import config_shared


def test_get_config_value_default(monkeypatch):
    assert config_shared.get_config_value("NON_EXISTENT_KEY", "default") == "default"


def test_get_config_bool_true(monkeypatch):
    monkeypatch.setenv("TEST_BOOL", "true")
    assert config_shared.get_config_bool("TEST_BOOL", False) is True


def test_get_config_bool_false(monkeypatch):
    monkeypatch.setenv("TEST_BOOL", "false")
    assert config_shared.get_config_bool("TEST_BOOL", True) is False
