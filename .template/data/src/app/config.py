"""Configuration for data pollers."""

from app.config_shared import *


def get_poller_name() -> str:
    return get_config_value("POLLER_NAME", "stock_data_example")


def get_rabbitmq_queue() -> str:
    return get_config_value("RABBITMQ_QUEUE", "stock_data_example_queue")


def get_dlq_name() -> str:
    return get_config_value("DLQ_NAME", "stock_data_example_dlq")
