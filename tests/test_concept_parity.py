import os
import re
import subprocess
from pathlib import Path

# Paths
PACKAGE_ROOT = Path(__file__).resolve().parents[1]


def _agent_utilities_root() -> Path:
    common_dir = subprocess.run(
        ["git", "rev-parse", "--path-format=absolute", "--git-common-dir"],
        cwd=PACKAGE_ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    canonical_repository = Path(common_dir).resolve(strict=True).parent
    return canonical_repository.parents[1] / "agent-utilities"


MASTER_OVERVIEW_PATH = _agent_utilities_root() / "docs" / "overview.md"


def extract_concepts_from_overview(filepath):
    """Extracts concepts from the markdown table in the master overview.md"""
    if not os.path.exists(filepath):
        return set()

    concepts = set()
    with open(filepath, encoding="utf-8") as f:
        for line in f:
            if not line.strip().startswith("|"):
                continue
            if "Pillar | Sub-Concept" in line or "|---|" in line:
                continue

            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 5:
                raw_id = parts[1].replace("*", "").strip()
                if re.match(r"^[A-Z]+-\d+(?:\.\d+)?$", raw_id):
                    concepts.add(raw_id)
    return concepts


def extract_concepts_from_codebase(directory):
    """Recursively scans source files in the project for CONCEPT:ID tags."""
    found_concepts = set()
    for root, _, files in os.walk(directory):
        if (
            "node_modules" in root
            or ".venv" in root
            or ".git" in root
            or "__pycache__" in root
        ):
            continue

        for file in files:
            if file.endswith((".py", ".ts", ".tsx", ".md")):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, encoding="utf-8") as f:
                        content = f.read()
                        matches = re.findall(r"CONCEPT:([A-Z]+-\d+(?:\.\d+)?)", content)
                        found_concepts.update(matches)
                except Exception:
                    pass
    return found_concepts


def test_concept_parity():
    """
    Enforces that all concepts documented or used in leanix-agent
    exist in the master agent-utilities registry.
    """
    master_concepts = extract_concepts_from_overview(MASTER_OVERVIEW_PATH)

    # Extract concepts from this project
    local_codebase_concepts = extract_concepts_from_codebase(PACKAGE_ROOT)

    # Only enforce parity for agent-utilities 5-Pillar concepts
    # Project-specific concepts (SX-*, AU-*, CE-*, TP-*, CA-*, etc.) are excluded
    agent_utilities_pillars = ("ORCH-", "KG-", "AHE-", "ECO-", "OS-")
    local_codebase_concepts = {
        c for c in local_codebase_concepts if c.startswith(agent_utilities_pillars)
    }

    # Ignore legacy KG-00x concepts
    local_codebase_concepts = {
        c for c in local_codebase_concepts if not c.startswith("KG-00")
    }

    # Ensure every concept used locally is registered in the master overview.md
    unregistered_concepts = local_codebase_concepts - master_concepts

    assert not unregistered_concepts, (
        f"The following concepts are used in leanix-agent but are NOT registered "
        f"in the master agent-utilities/docs/overview.md registry: {unregistered_concepts}. "
        f"Please register them first."
    )
