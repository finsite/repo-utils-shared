# 📌 Project TODO: Stock-\* Poller & Analysis Engine

This TODO list outlines the remaining work to finalize the `stock-*`
repositories, ensuring all pollers and processors are production-grade,
consistent, and maintainable.

---

## ✅ Core Functionality

- [ ] Ensure poller loads:
  - [ ] Symbols from configuration
  - [ ] API keys from Vault or environment
  - [ ] Correct poller/processor module for the strategy
- [ ] Add CLI flags or health check endpoints
- [ ] Add dry-run/test mode for output verification

---

## 🔐 Vault Integration

- [ ] Auto-initialize Vault secrets in dev/staging
- [ ] One policy per poller/processor
- [ ] Vault fallback to env vars (with warnings)
- [ ] Log all failed or missing Vault lookups

---

## 📨 Messaging (RabbitMQ / SQS)

- [ ] Ensure all pollers:
  - [ ] Use `queue_sender.py` + `queue_handler.py`
  - [ ] Use `get_queue_type()` and RabbitMQ/SQS fallback logic
- [ ] Add retry logic + exponential backoff
- [ ] Add metrics for:
  - [ ] Publish latency
  - [ ] Queue delivery success/fail
- [ ] Validate metrics hooks (`track_polling_metrics`, `track_request_metrics`)

---

## ⚙️ Configuration Standardization

- [ ] Use `config.py` in all repos with:
  - [ ] `get_polling_interval()`
  - [ ] `get_batch_size()`
  - [ ] `get_rabbitmq_queue()` and routing helpers
- [ ] Log missing or defaulted config keys
- [ ] Validate config with test runner
- [ ] Support JSON/INI overrides optionally

---

## 🧪 Testing & Validation

- [ ] Test coverage >90%:
  - [ ] Poller startup + shutdown
  - [ ] Message parsing
  - [ ] Vault + config fallbacks
- [ ] Add `tests/integration/` runner
- [ ] Mock API calls for:
  - [ ] Rate limits
  - [ ] Timeout handling
  - [ ] Malformed response handling
- [ ] Validate structured logging format in tests
- [ ] Add test cases for Vault fallback behavior
- [ ] Add fuzz tests for malformed API responses
- [ ] Add coverage reports to CI with threshold enforcement

---

## 🧠 Caching & Optimization

- [ ] Enable LRU caching for symbol configs
- [ ] Consider Redis or in-memory cache where useful
- [ ] Use batch API requests where supported
- [ ] Profile slow pollers (e.g., using `cProfile` or `pyinstrument`)

---

## 🔊 Logging Enhancements

- [ ] Add `LOG_LEVEL` via environment
- [ ] Add structured logging (`loguru`, `structlog`)
- [ ] Optionally log to file
- [ ] Validate all logs include symbol, timestamp, and context
- [ ] Redact sensitive data in logs (API keys, symbols)
- [ ] Add `REDACT_SENSITIVE_LOGS` flag to logger

---

## 📈 Metrics

- [ ] Poller metrics (stdout or Prometheus-ready)
  - [ ] Request durations
  - [ ] Queue send latency
  - [ ] Poll success/failure counts
- [ ] Standardize:
  - [ ] `track_polling_metrics()`
  - [ ] `track_request_metrics()`
- [ ] Include metrics for Vault lookups and config loading

---

## 💬 Slack Integration (Optional)

- [ ] Add Slack notifier module
- [ ] Send alert on critical failure or threshold
- [ ] Send daily summary if `ENABLE_SLACK_ALERTS=true`

---

## 🧹 Code & Repo Hygiene

- [ ] Validate all:
  - [ ] Type annotations
  - [ ] Function/class/module docstrings
- [ ] Remove unused imports
- [ ] Ensure consistent folder structure (`src/app`)
- [ ] Lint all code using `ruff`, `black`, `mypy`, `yamlfix`
- [ ] Ensure all shared files come from `.template/poller/`
- [ ] Validate `pyproject.toml` via `check-pyproject`
- [ ] Enforce `known_first_party = ["app"]`
- [ ] Confirm `src/app/__init__.py` includes `__version__`, public API exports

---

## 🔄 CI/CD + Tooling

- [ ] GitHub Actions:
  - [ ] Linting (black, ruff, mypy)
  - [ ] Tests with coverage
  - [ ] Pre-commit enforcement
- [ ] Add support for:
  - [ ] Version bumping via Commitizen
  - [ ] SBOM and provenance (SLSA, Cosign)
  - [ ] Bandit, `pip-audit`, `semgrep`, `cyclonedx-bom`
- [ ] Publish Docker image (optional)

---

## 📝 Documentation

- [ ] Add README badges: build, test, coverage
- [ ] Expand README with:
  - [ ] Setup instructions
  - [ ] Example usage
- [ ] Add CONTRIBUTING.md
- [ ] Ensure LICENSE (Apache 2.0 or MIT) exists

---

## ✅ GitHub Public Repository Hardening Checklist

- [ ] Enable CodeQL scanning
- [ ] Enable secret scanning (with push protection)
- [ ] Enable Dependabot alerts (and updates if desired)
- [ ] Add branch protection rules:
  - Require PR reviews
  - Require status checks (lint, tests, audit)
  - Require signed commits (optional)
- [ ] Add `SECURITY.md` to `.github/`
- [ ] Disable unused features (Wiki, Projects)
- [ ] Configure license and metadata in `pyproject.toml`
- [ ] Add `.pre-commit-config.yaml` with security hooks

---

## 🔁 Resilience & Runtime Enhancements

- [ ] Retry on queue publish failures using `tenacity`
- [ ] Retry on API/network errors with exponential backoff
- [ ] Graceful shutdown (e.g., SIGINT/SIGTERM)
- [ ] Healthcheck endpoint or CLI for liveness probe
- [ ] Heartbeat or uptime metric per poller

---

## 🧩 Optional Enhancements

- [ ] Add support for REST/S3/DB as alternative output targets
- [ ] Support async pollers for high-throughput APIs
- [ ] Add caching or fallback for symbol list config
- [ ] Add OAuth2 token refresh for APIs that require it
