"""
Unit tests for vault_client.py
"""

from unittest.mock import patch

from app.utils.vault_client import get_secret_from_vault


@patch("app.utils.vault_client.requests.get")
def test_get_secret_from_vault(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"data": {"data": {"API_KEY": "123"}}}
    secret = get_secret_from_vault("my/path")
    assert secret["API_KEY"] == "123"
