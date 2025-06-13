# TODO for `repo-utils-shared`

## 1. Shared Template Maintenance

- [x] Centralize `.template/` directories by project type:
  - `.template/poller/`
  - `.template/analysis/`
  - `.template/db/`
  - `.template/ui/`
  - `.template/crypto/`
  - `.template/backtest/`
  - `.template/data/`
- [x] Finalize reusable `Makefile`, `.pre-commit-config.yaml`, and `pyproject.toml` fragments.
- [x] Fix all existing pre-commit hook issues across templates.
- [x] Add synced `.gitattributes`, `.gitignore`, `.dockerignore` files.

## 2. Pre-commit Enhancements

- [x] Enable strict formatting, linting, and type checking.
- [x] Resolve `pip-compile` and dependency resolver behavior.
- [x] Disable `check-pyproject` due to incompatible constraints.
- [x] Finalize Ruff, Black, Bandit, Pyright, and Pip Audit configuration.
- [x] Add `check-version-consistency` to ensure changelog and version sync.

### 🆕 Optional Enterprise-Grade Enhancements (to be implemented)

- [ ] Add REUSE license header compliance (`reuse lint`)
- [ ] Add advanced secret scanning (`detect-secrets`)
- [ ] Add SBOM generation + validation (`cyclonedx-bom`, `syft`)
- [ ] Add advanced static analysis (`semgrep`)
- [ ] Add Markdown linting (`markdownlint-cli`)
- [ ] Re-enable `pytest` and `pytest-cov` hooks with coverage enforcement
- [ ] Mirror all pre-commit checks in GitHub Actions CI

## 3. Scripts and Sync Utilities

- [x] Create `sync.py` with `--apply` and `sync.log` functionality.
- [x] Add `check-version-consistency.py` for version syncing.
- [x] Ensure scripts are executable and documented in README.
- [x] Ensure `template_python` receives correct `.template/base/src` sync
- [ ] Add `.template/crypto/`, `.template/backtest/`, and `.template/data/` sync logic
- [ ] Update `sync.py` to assign proper types to crypto, backtest, and data repositories
- [ ] Add test method to detect if synced `src/` or `tests/` content changes are correctly applied

## 4. Documentation

- [x] Add `README.md` with usage overview and sync instructions.
- [ ] Add examples of how to integrate `.template` scaffolding into new repos.
- [ ] Ensure all `README.md` and `TODO.md` files are synced and type-specific
- [ ] Add centralized README/TODO sync rules per repo type (poller, db, analysis, sentiment, crypto, backtest, data)

## 5. Repository Readiness and Coverage

- [ ] Create missing `stock-crypto-*` repositories:
  - `stock-crypto-prices`
  - `stock-crypto-news`
  - `stock-crypto-metrics`
  - `stock-crypto-sentiment`
  - `stock-crypto-arbitrage`
- [ ] Create missing `stock-backtest-*` repositories:
  - `stock-backtest-engine`
  - `stock-backtest-strategies`
- [ ] Create missing `stock-data-*` repositories:
  - `stock-data-cleanser`
  - `stock-data-transformer`
- [ ] Create missing `stock-db-*` repositories:
  - `stock-db-migration`
  - `stock-db-writer-test`
- [ ] Ensure `template_python` is populated and validated
- [ ] Add unit tests per repo under `tests/app/` with Pytest support
- [ ] Ensure all `main.py` scripts run without error and provide structured logging
- [ ] Validate each `config.py` contains shared config hooks and poller-specific logic
- [ ] Confirm logging to file or stdout, JSON logging where relevant
- [ ] Ensure metrics are exposed for Prometheus
- [ ] Add DLQ handlers per queue type
- [ ] Validate that test processors and main pipelines support batch and single-message operation
- [ ] Ensure all `types.py` and `processor.py` files are production-grade and validated
- [ ] Ensure `stock-backtest-*`, `stock-data-*`, and `stock-crypto-*` repos inherit correct scaffolding and logging/test infra

## 6. Infrastructure Production Readiness

- [ ] Add Helm chart scaffolding for all app types (poller, db, analysis, crypto, ui, data, backtest)
- [ ] Create ArgoCD app manifests per repository for GitOps deployment
- [ ] Confirm RabbitMQ config matches queue/exchange setup from Docker Compose
- [ ] Validate PostgreSQL/InfluxDB schemas with full initialization logic
- [ ] Include monitoring stack (Prometheus + Grafana) with service dashboards
- [ ] Implement health checks and readiness probes in Kubernetes templates
- [ ] Add Vault secret injection via Kubernetes sidecar or CSI provider
- [ ] Ensure all Helm charts include ingress, autoscaling, persistence, and toleration options
- [ ] Add GitOps tooling and CI/CD checks for drift, Helm diff, and Argo sync status
- [ ] Add secrets + config sync logic via SOPS or Vault for staging/production

## 7. Final Verification

- [ ] Run `sync.py` and verify no diffs
- [ ] Validate `pre-commit` hooks pass in every repo
- [ ] Ensure one integration test runs per repo type (poller, db, analysis, crypto, ui, data, backtest)
- [ ] Confirm monitoring dashboards are functional for all critical services
- [ ] Ensure all production deployments can be built via Helm + ArgoCD end-to-end
- [ ] Add staging namespace verification and smoke tests
