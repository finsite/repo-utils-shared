"""
Unit tests for output_handler.py
"""

from unittest.mock import patch

from app.output_handler import send_to_postgres


@patch("app.output_handler.psycopg2.connect")
def test_send_to_postgres(mock_connect):
    mock_conn = mock_connect.return_value
    send_to_postgres([{"symbol": "AAPL", "price": 123.45}])
    assert mock_conn.cursor.return_value.execute.called
