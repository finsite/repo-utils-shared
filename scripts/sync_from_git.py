#!/usr/bin/env python3
"""Sync project version and changelog with the latest Git tag.

This script updates pyproject.toml and __init__.py with the latest Git tag,
generates a categorized changelog section for the tag, and inserts it if missing.
"""

import re
import subprocess
from collections import defaultdict
from datetime import datetime
from pathlib import Path

# --- File paths ---
PYPROJECT = Path("pyproject.toml")
INIT = Path("src/app/__init__.py")
CHANGELOG = Path("CHANGELOG.md")


# --- Helpers ---
def run(cmd: list[str]) -> str:
    """Run a shell command and return the output as string."""
    return subprocess.check_output(cmd, text=True).strip()


def get_tags_sorted() -> list[str]:
    """Return a list of Git tags sorted by creation date."""
    return run(["git", "tag", "--sort=creatordate"]).splitlines()


def get_latest_and_previous_tags() -> tuple[str, str | None]:
    """Return the latest and previous Git tags."""
    tags = get_tags_sorted()
    return tags[-1], tags[-2] if len(tags) > 1 else (tags[-1], None)


def strip_v(tag: str) -> str:
    """Remove leading 'v' from a tag if present."""
    return tag[1:] if tag.startswith("v") else tag


def get_commits_between(prev: str | None, latest: str) -> list[str]:
    """Return commit messages between two Git tags."""
    range_expr = f"{prev}..{latest}" if prev else latest
    return run(["git", "log", range_expr, "--pretty=format:%s"]).splitlines()


def categorize_commits(commits: list[str]) -> dict[str, list[str]]:
    """Categorize commits into changelog sections based on prefixes."""
    sections = defaultdict(list)
    for msg in commits:
        lower = msg.lower()
        if lower.startswith("feat"):
            sections["Added"].append(msg)
        elif lower.startswith("fix"):
            sections["Fixed"].append(msg)
        elif lower.startswith(("refactor", "chore", "perf")):
            sections["Changed"].append(msg)
        elif lower.startswith("docs"):
            sections["Documentation"].append(msg)
        else:
            sections["Miscellaneous"].append(msg)
    return sections


def update_pyproject(version: str) -> None:
    """Update the version in pyproject.toml."""
    content = PYPROJECT.read_text(encoding="utf-8")
    updated = re.sub(r'version\s*=\s*".+?"', f'version = "{version}"', content)
    PYPROJECT.write_text(updated, encoding="utf-8")


def update_init(version: str) -> None:
    """Update the __version__ value in __init__.py."""
    content = INIT.read_text(encoding="utf-8")
    updated = re.sub(r'__version__\s*=\s*["\'].*?["\']', f'__version__ = "{version}"', content)
    INIT.write_text(updated, encoding="utf-8")


def insert_changelog_entry(tag: str, version: str, sections: dict[str, list[str]]) -> None:
    """Insert a new changelog entry for the tag if it does not already exist."""
    today = datetime.today().strftime("%Y-%m-%d")
    lines = [f"## {tag} ({today})\n"]
    for section in ["Added", "Fixed", "Changed", "Documentation", "Miscellaneous"]:
        if section in sections:
            lines.append(f"### {section}\n")
            lines.extend([f"- {entry}" for entry in sections[section]])
            lines.append("")

    entry_text = "\n".join(lines)

    content = CHANGELOG.read_text(encoding="utf-8")
    if tag in content:
        print(f"✅ Changelog already has entry for {tag}")
        return

    if "## [Unreleased]" in content:
        new_content = content.replace("## [Unreleased]", f"## [Unreleased]\n\n{entry_text}")
    else:
        new_content = f"{entry_text}\n\n{content}"

    CHANGELOG.write_text(new_content, encoding="utf-8")
    print(f"✅ Inserted changelog entry for {tag}")


# --- Main workflow ---
def sync_versions_and_changelog():
    """Sync version metadata and changelog based on Git tags."""
    latest_tag, previous_tag = get_latest_and_previous_tags()
    version = strip_v(latest_tag)
    print(f"🔁 Syncing version: {version} from tag: {latest_tag}")

    update_pyproject(version)
    update_init(version)

    if not CHANGELOG.exists():
        CHANGELOG.write_text("# Changelog\n\n## [Unreleased]\n", encoding="utf-8")

    commits = get_commits_between(previous_tag, latest_tag)
    sections = categorize_commits(commits)
    insert_changelog_entry(latest_tag, version, sections)

    print("✅ pyproject.toml and __init__.py updated.")


if __name__ == "__main__":
    sync_versions_and_changelog()
