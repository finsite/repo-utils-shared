# TODO for Stock Data Collector

## 1. Data Pollers

- [ ] Add more poller modules (e.g., fundamentals, news, etc.)
- [ ] Normalize symbol handling across sources
- [ ] Retry on data pull failure with exponential backoff

## 2. Output Handling

- [ ] Add support for output to S3 or file system
- [ ] Validate data structure before sending to queue
- [ ] Add schema validation and type checks

## 3. Configuration

- [ ] Use shared Vault config fallback
- [ ] Add support for `ENVIRONMENT` overlays
- [ ] Handle missing env vars gracefully

## 4. Testing

- [ ] Add unit tests per poller type
- [ ] Mock data input/output for integration tests
- [ ] Add output schema regression checks

## 5. Documentation

- [ ] Document how to add a new poller
- [ ] Add queue structure explanation
- [ ] Link to shared infrastructure setup (RabbitMQ, Vault)

## 6. Security

- [ ] Enable structured logging with redacted secrets
- [ ] Integrate Bandit and CodeQL
- [ ] Provide example Vault secret pathing
