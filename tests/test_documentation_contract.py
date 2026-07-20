"""Keep published LeanIX documentation current and environment-neutral."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRIVATE_IPV4 = re.compile(
    r"\b(?:10(?:\.\d{1,3}){3}|192\.168(?:\.\d{1,3}){2}|"
    r"172\.(?:1[6-9]|2\d|3[01])(?:\.\d{1,3}){2})\b"
)
ENVIRONMENT_DNS = re.compile(r"(?i)\b(?:[A-Za-z0-9-]+\.)+(?:arpa|local)(?=[:/\s\"'])")
MACHINE_HOME = re.compile(
    r"(?i)(?:[A-Z]:[\\/]Users[\\/](?![<%$])[^\\/\s]+|"
    r"/(?:home|Users)/(?![<%$])[^/\s]+|"
    r"/mnt/[A-Z]/Users/(?![<%$])[^/\s]+)"
)


def _pages() -> list[Path]:
    return [ROOT / "README.md", *sorted((ROOT / "docs").rglob("*.md"))]


def test_public_documentation_is_environment_neutral() -> None:
    for page in _pages():
        content = page.read_text(encoding="utf-8")
        assert PRIVATE_IPV4.search(content) is None, page
        assert ENVIRONMENT_DNS.search(content) is None, page
        assert MACHINE_HOME.search(content) is None, page


def test_local_documentation_links_resolve() -> None:
    pattern = re.compile(r"!?\[[^]]*\]\(([^)\n]+)\)")
    for page in _pages():
        for raw in pattern.findall(page.read_text(encoding="utf-8")):
            target = raw.strip().split(maxsplit=1)[0].strip("<>").split("#", 1)[0]
            if not target or "://" in target or target.startswith(("#", "/")):
                continue
            assert (page.parent / target).resolve().exists(), f"{page}: {target}"


def test_readme_documents_current_tool_and_runtime_defaults() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "`intent` default" in readme
    assert "#### Condensed action-routed tools (`MCP_TOOL_MODE=condensed`)" in readme
    assert "docs/mcp.md" not in readme
    assert "docs/agent.md" not in readme
    assert "agent-os-genesis" not in readme
