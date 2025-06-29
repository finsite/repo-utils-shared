# Stock Data Collector

This repository gathers raw stock-related data from various sources for further
analysis or processing.

## ✅ Features

- Modular data collection with pluggable sources
- Flexible symbol list configuration (manual or dynamic)
- RabbitMQ/SQS publisher support
- Optional output to local storage or databases
- Dockerized for consistent deployment

## 🗂️ Project Structure

```
src/
└── app/
    ├── main.py               # Entry point for data polling
    ├── config.py             # Custom repo configuration
    ├── poller_factory.py     # Loads appropriate data poller
    ├── pollers/              # Source-specific pollers
    └── utils/                # Logging, retry, etc.
```

## 🧪 Development

```bash
make install
make run
make lint
make test
```

## 📦 Deployment

```bash
docker build -t stock-data .
docker run --env-file .env stock-data
```

## 📝 License

Apache License 2.0
