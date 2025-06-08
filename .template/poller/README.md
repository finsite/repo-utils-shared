# Stock Data Poller

This repository collects raw stock-related data from various sources and publishes it to a message queue for downstream analysis or storage.

## Features

- Modular poller architecture
- Pluggable data source integrations (e.g., APIs, web scraping)
- Configurable polling intervals, rate limits, and batching
- Secure configuration via environment variables or Vault
- Queue publishing with support for RabbitMQ and AWS SQS
- Production-ready Docker + Kubernetes deployment
- Centralized structured logging

## Project Structure

```
src/
├── app/
│   ├── config.py               # Configuration loader
│   ├── main.py                 # Entry point
│   ├── poller_factory.py       # Dynamically loads the appropriate poller
│   ├── queue_sender.py         # Publishes messages to RabbitMQ or SQS
│   ├── utils/                  # Shared utilities
│   └── pollers/                # Source-specific pollers
```

## Usage

```bash
make install
make run
```

## Environment Variables

| Variable               | Description                         |
|------------------------|-------------------------------------|
| `QUEUE_TYPE`           | Either `rabbitmq` or `sqs`          |
| `RABBITMQ_URL`         | URL for RabbitMQ                    |
| `SQS_QUEUE_URL`        | AWS SQS queue URL                   |
| `VAULT_ADDR`           | Vault server address                |
| `VAULT_TOKEN`          | Vault token or AppRole auth config  |
| `POLLING_INTERVAL`     | How often to poll (in seconds)      |

## Development

```bash
make lint        # Run linters
make test        # Run tests
make build       # Build Docker image
```

## License

Apache License 2.0
