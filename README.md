# 🛠 repo-utils-shared

Shared scaffolding and automation for all `stock-*` repositories. Includes:

- `.template/` folder by project type (`poller/`, `db/`, `ui/`, etc.)
- Hardened `.pre-commit-config.yaml` for enterprise-grade validation
- Reusable Makefile
- Version consistency and changelog tooling
- Dependency sync and audit hooks

## 📁 Template Structure

```bash
.template/
├── poller/
├── db/
├── ui/
└── analysis/
Each template folder contains standardized configs, utilities, and src/ scaffolding.

🧪 Pre-commit
Includes:

Ruff, Black, Isort, Pyright, Pylint

Bandit, Pip Audit, Deptry, Codespell

Commitizen changelog validation

Pip compile and dependency verification

To install and run:

bash
Copy
Edit
pre-commit install
pre-commit run --all-files
🔁 Sync Utilities
bash
Copy
Edit
# Preview changes
python sync.py

# Apply changes to all repositories and log results
python sync.py --apply
📦 Version Tools
bash
Copy
Edit
# Check that pyproject.toml, __init__.py, and CHANGELOG.md are in sync with the latest Git tag
python .hooks/check-version-consistency.py
📋 TODO Highlights
 Add REUSE and SBOM tooling

 Add Semgrep, Markdown lint, and advanced secret scanning

 Re-enable tests once implemented

