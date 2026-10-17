"""Provider-owned skill discovery and progressive-disclosure contract."""

from __future__ import annotations

import re
from importlib.resources import files

import yaml

SKILL_NAME = "leanix-enterprise-architecture-operations"
SKILL_NAMES = [
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
    document = skills[0].joinpath("SKILL.md").read_text(encoding="utf-8")

    references = set(re.findall(r"\]\(references/([^\s)#]+\.md)\)", document))
    assert references == {
        "configuration-and-tls.md",
        "factsheet-inventory.md",
        "knowledge-graph-ingestion.md",
        "pathfinder-graphql.md",
    }
    assert all(
        skills[0].joinpath("references", reference).is_file()
        for reference in references
    )


def test_skill_metadata_references_the_canonical_name() -> None:
    skill = files("leanix_agent.skills").joinpath(SKILL_NAME)
    metadata = yaml.safe_load(
        skill.joinpath("agents", "openai.yaml").read_text(encoding="utf-8")
    )
    assert metadata["interface"]["default_prompt"].startswith(f"Use ${SKILL_NAME} ")
