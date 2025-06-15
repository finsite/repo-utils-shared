# TODO for Stock Poller

## 1. Poller Enhancements

- [ ] Add additional pollers (e.g., IEX Cloud, Alpha Vantage, EODHD)
- [ ] Enable dynamic symbol fetching from external service
- [ ] Improve retry/backoff strategy using exponential delay
- [ ] Implement optional circuit breaker pattern for failing APIs

## 2. Queue Enhancements

- [ ] Add batch support for queue_sender
- [ ] Retry on queue publish failure (with `tenacity`)
- [ ] Add metrics tracking (e.g., Prometheus) for send operations
- [ ] Add DLQ fallback or audit logging on message send failure

## 3. Configuration & Security

- [ ] Enforce Vault fallback logic and fail-closed mode
- [ ] Add support for environment-specific config overlays
- [ ] Redact sensitive logs when `REDACT_SENSITIVE_LOGS=true`

## 4. Observability

- [ ] Add tracing hooks (e.g., OpenTelemetry)
- [ ] Ship logs to centralized logging stack (ELK, CloudWatch, etc.)
- [ ] Auto-generate Grafana dashboards for key metrics

## 5. Documentation

- [ ] Finalize per-poller docs and setup examples
- [ ] Add REST endpoint examples for consuming queue data
- [ ] Generate SBOM and include SLSA attestation metadata

## 6. Testing

- [ ] Expand unit test coverage for all pollers
- [ ] Add integration tests for queue delivery
- [ ] Mock rate limiter and symbol list for faster test runs
