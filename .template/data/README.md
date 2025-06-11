# stock-data-<source>

This repository polls data from a specific provider and publishes it to a
message queue.

## Usage

```bash
python -m app.main
```

## Structure

- `pollers/`: Contains poller logic per provider
- `poller_factory.py`: Chooses correct poller based on config

## Requirements

- Python 3.11+
- RabbitMQ or SQS configured
