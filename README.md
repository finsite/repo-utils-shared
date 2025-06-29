# Stock Poller

This repository implements a modular polling service that collects stock data
from external APIs and pushes the results to a message queue for downstream
processing.

## ✅ Features

- Pluggable poller system for various stock data providers
- RabbitMQ and AWS SQS support via a unified queue interface
- Vault integration for secure secret management
- Environment-driven and Vault-overridable configuration
- Configurable polling interval, rate limiting, and retry behavior
- Structured logging with optional JSON output
- Production-ready Docker and Kubernetes deployment

## 🗂️ Project Structure

```
src/
├── app/
│   ├── main.py                 # Main polling loop
│   ├── config.py               # Per-repo overrides
│   ├── config_shared.py        # Shared Vault/ENV logic
│   ├── poller_factory.py       # Instantiates appropriate poller
│   ├── queue_sender.py         # Sends to RabbitMQ/SQS
│   ├── pollers/                # Source-specific pollers
│   └── utils/
│       ├── rate_limit.py       # Token bucket rate limiter
│       ├── setup_logger.py     # Logging setup
│       ├── types.py            # Shared types and enums
│       └── vault_client.py     # Vault AppRole client
```

## 🛠️ Usage

```bash
make install
make run
```

Or run directly:

```bash
python -m app.main
```

## ⚙️ Environment Variables

| Variable             | Description                                   |
| -------------------- | --------------------------------------------- |
| `QUEUE_TYPE`         | `rabbitmq` or `sqs`                           |
| `SYMBOLS`            | Comma-separated list of stock symbols         |
| `POLLING_INTERVAL`   | Interval between poll cycles (seconds)        |
| `RATE_LIMIT`         | Requests per second                           |
| `RETRY_DELAY`        | Delay before retry on failure (seconds)       |
| `STRUCTURED_LOGGING` | Enable JSON-formatted logs (`true` / `false`) |
| `VAULT_ADDR`         | Vault server address                          |
| `VAULT_TOKEN`        | Vault token (or AppRole credentials)          |

## 🧪 Development

```bash
make lint
make test
make build
make preflight
```

## 🔐 Security

- Logs redact sensitive values if `REDACT_SENSITIVE_LOGS=true`
- Vault AppRole authentication with KV v2 secret support
- CodeQL and Bandit integrated for secure coding practices

## 📦 Deployment

```bash
docker build -t stock-poller .
docker run --env-file .env stock-poller
```

For Kubernetes:

```bash
make k8s
```

## 📝 License

Licensed under the
[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
