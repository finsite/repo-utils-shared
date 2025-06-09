"""
Test for queue_handler.py in analysis repositories.
"""
from unittest.mock import patch, MagicMock
from app.queue_handler import consume_messages

@patch("app.queue_handler.config.get_queue_type", return_value="rabbitmq")
@patch("app.queue_handler.pika.BlockingConnection")
def test_consume_messages(mock_pika, mock_config):
    mock_channel = MagicMock()
    mock_pika.return_value.channel.return_value = mock_channel
    consume_messages(lambda batch: None)
    assert mock_channel.basic_consume.called or mock_channel.basic_qos.called
