#!/usr/bin/env python3
"""Fail when legacy numeric-pillar ``CONCEPT:`` markers remain."""

from __future__ import annotations

import re
import sys
from pathlib import Path

_LEGACY_RE = re.compile(r"CONCEPT:[A-Z]+-[0-9]")
_EXTENSIONS = {".py", ".rs", ".md"}
_SKIP_DIRS = {"__pycache__", ".git", ".venv", "node_modules", "target", "build", "dist"}
_SKIP_FILES = {
    "check_no_legacy_markers.py",
    "CHANGELOG.md",
    "concept_map.md",
    "concepts.yaml",
    "concept_reservations.yaml",
}


def scan(root: Path) -> list[str]:
    """Return bounded, location-only evidence for legacy markers below ``root``."""
    hits: list[str] = []
    for path in root.rglob("*"):
        if (
            path.suffix not in _EXTENSIONS
            or path.name in _SKIP_FILES
            or any(part in _SKIP_DIRS for part in path.parts)
        ):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for line_number, line in enumerate(text.splitlines(), 1):
            if _LEGACY_RE.search(line):
                hits.append(f"{path.relative_to(root)}:{line_number}")
    return hits


def main(arguments: list[str]) -> int:
    """Scan supplied roots, or the current directory when none are supplied."""
    hits = [hit for value in arguments or ["."] for hit in scan(Path(value))]
    if not hits:
        print("OK: no legacy CONCEPT markers remain.")
        return 0
    print(f"FAIL: {len(hits)} legacy CONCEPT marker(s) remain:")
    for hit in hits[:60]:
        print(f"  {hit}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
