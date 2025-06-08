# TODO — Stock Data Poller

## 🧩 Missing Features

- [ ] Add support for new data sources (e.g., paid APIs, ETFs, commodities)
- [ ] Implement retry with exponential backoff on poller failure
- [ ] Add API quota awareness (track usage)
- [ ] Support time-window-based polling (e.g., last 5m, hourly rollups)

## 🛠️ Infrastructure Enhancements

- [ ] Add support for Vault secret rotation
- [ ] Parameterize queue naming convention
- [ ] Add DLQ (dead letter queue) routing and handling
- [ ] Make polling interval dynamically adjustable at runtime

## 📈 Monitoring & Logging

- [ ] Integrate Prometheus metrics (poll success/failure, duration)
- [ ] Add structured JSON logging (`loguru` or `structlog`)
- [ ] Log output message summary for observability

## ✅ Security & Compliance

- [ ] Add Bandit + Safety to CI for security linting
- [ ] Generate SBOM (`cyclonedx-bom` or `syft`)
- [ ] Enable Cosign for image signing
- [ ] Add REUSE license header validation
- [ ] Enable Semgrep for static analysis

## 🧪 Testing & CI

- [ ] Add test coverage for each poller module
- [ ] Use `pytest-cov` for coverage metrics
- [ ] Add smoke tests for startup/config validation
- [ ] Mirror all pre-commit checks in CI workflow

## 🧹 Code Hygiene

- [ ] Migrate all imports to absolute paths
- [ ] Remove unused dependencies with `deptry`
- [ ] Enforce version bump validation via `Commitizen`

## 🪄 Optional Enhancements

- [ ] Add REST endpoint to trigger on-demand polling
- [ ] Allow polling from config-defined lists of symbols
