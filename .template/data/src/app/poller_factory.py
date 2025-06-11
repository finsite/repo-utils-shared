"""Factory to get the appropriate poller."""

from app.config import get_poller_name
from app.pollers.example_poller import ExamplePoller


def get_poller():
    poller_name = get_poller_name()
    if poller_name == "stock_data_example":
        return ExamplePoller()
    raise ValueError(f"Unsupported poller: {poller_name}")
