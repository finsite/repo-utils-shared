# TODO for `repo-utils-shared`

## 1. Shared Template Maintenance

- [x] Centralize `.template/` directories by project type:
  - `.template/poller/`
  - `.template/analysis/`
  - `.template/db/`
  - `.template/ui/`
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

## 4. Documentation

- [x] Add `README.md` with usage overview and sync instructions.
- [ ] Add examples of how to integrate `.template` scaffolding into new repos.
