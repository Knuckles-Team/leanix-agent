"""Provider-owned skill discovery and progressive-disclosure contract."""

from __future__ import annotations

import re
from importlib.resources import files
from pathlib import Path

import pytest
import tomllib
import yaml

ROOT = Path(__file__).resolve().parents[1]
DASHBOARD_CONFIG = ROOT / ".github/spec-dashboard.json"
DEVELOPMENT_SKILL = ROOT / "leanix_agent/skills/leanix-agent-development/SKILL.md"

DEVELOPMENT_SKILL_NAME = "leanix-agent-development"
SKILL_NAME = "leanix-enterprise-architecture-operations"
SKILL_NAMES = [
    DEVELOPMENT_SKILL_NAME,
    SKILL_NAME,
    "leanix-factsheet-inventory",
    "leanix-graphql-query",
    "leanix-kg-ingestion",
]


def _frontmatter(document: str) -> dict[str, object]:
    assert document.startswith("---\n")
    _, raw, _ = document.split("---", 2)
    parsed = yaml.safe_load(raw)
    assert isinstance(parsed, dict)
    return parsed


def test_provider_exposes_valid_progressive_disclosure_skills() -> None:
    root = files("leanix_agent.skills")
    skills = sorted(
        child
        for child in root.iterdir()
        if child.is_dir() and child.joinpath("SKILL.md").is_file()
    )

    assert [skill.name for skill in skills] == SKILL_NAMES
    for skill in skills:
        meta = _frontmatter(skill.joinpath("SKILL.md").read_text(encoding="utf-8"))
        assert meta["name"] == skill.name
        assert meta["description"]
    operations = next(skill for skill in skills if skill.name == SKILL_NAME)
    document = operations.joinpath("SKILL.md").read_text(encoding="utf-8")

    references = set(re.findall(r"\]\(references/([^\s)#]+\.md)\)", document))
    assert references == {
        "configuration-and-tls.md",
        "factsheet-inventory.md",
        "knowledge-graph-ingestion.md",
        "pathfinder-graphql.md",
    }
    assert all(
        operations.joinpath("references", reference).is_file()
        for reference in references
    )


def test_skill_metadata_references_the_canonical_name() -> None:
    skill = files("leanix_agent.skills").joinpath(SKILL_NAME)
    metadata = yaml.safe_load(
        skill.joinpath("agents", "openai.yaml").read_text(encoding="utf-8")
    )
    assert metadata["interface"]["default_prompt"].startswith(f"Use ${SKILL_NAME} ")


def _events(workflow: dict) -> dict:
    # YAML 1.1 parsers expose the unquoted `on` key as True.
    events = workflow.get("on", workflow.get(True))
    assert isinstance(events, dict)
    return events


@pytest.mark.spec("PIPE-CONNSPEC-R135.4")
def test_development_skill_has_rapid_contract_and_package_binding() -> None:
    text = DEVELOPMENT_SKILL.read_text(encoding="utf-8")
    frontmatter = text.split("---", 2)[1]
    project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))

    assert DEVELOPMENT_SKILL.is_file()
    assert "name: leanix-agent-development" in frontmatter
    assert "skill_type: skill" in frontmatter
    assert "## Rapid delivery: the 5-minute contract" in text
    for term in (
        "leanix_agent/__init__.py",
        "leanix_agent/auth.py",
        "leanix_agent/mcp/",
        "leanix_agent/instance_sync.py",
        "LEANIX_WORKSPACE",
        "leanix-mcp",
        "mcp_config.json",
        "skills/**",
        "python_pipeline.yml@main",
        "container_pipeline.yml@main",
        "pages_pipeline.yml@main",
        "render_connector: true",
        "uv run --locked --extra test pytest",
    ):
        assert term in text

    assert "verify=False" not in text
    assert "--no-verify" not in text
    package_data = project["tool"]["setuptools"]["package-data"]["leanix_agent"]
    assert "skills/**" in package_data
    assert project["project"]["entry-points"]["agent_connector_sdk.connector"] == {
        "leanix-mcp": "leanix_agent:connector"
    }


def test_pages_dashboard_config_is_canonical() -> None:
    assert DASHBOARD_CONFIG.is_file()
    assert yaml.safe_load(DASHBOARD_CONFIG.read_text(encoding="utf-8")) == {
        "version": 1,
        "sources": [{"glob": "specs/*/status.json", "kind": "spec"}],
    }


def test_legacy_mkdocs_publisher_is_absent() -> None:
    assert not (ROOT / ".github/workflows/docs.yml").exists()
