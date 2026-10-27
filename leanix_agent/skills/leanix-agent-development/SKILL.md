---
name: leanix-agent-development
domain: development
skill_type: skill
description: >-
  Develop, test, gate, and release the leanix-agent connector. Use this skill
  when changing LeanIX REST or GraphQL mappings, governed MCP tools, enterprise
  architecture ingestion, packaged content, documentation, or repository gates.
license: MIT
tags: [leanix, enterprise-architecture, development, connector, mcp, test, gates]
tier: repository
metadata:
  author: Genius
  version: '0.1.0'
---

# leanix-agent development

This repository owns the LeanIX REST and Pathfinder GraphQL clients, typed
enterprise-architecture models, action-routed MCP tools, source declarations,
knowledge-graph ingestion mappings, and packaged connector content. Shared
connector contracts, transports, TLS profiles, and credential helpers belong to
`agent-connector-sdk`; admission, serving, and durable graph state belong to
their owning repositories. Read `AGENTS.md` before changing code and keep
credentials, private endpoints, tenant values, and customer records out of
source, logs, fixtures, and skill content.

## Rapid delivery: the 5-minute contract

Specs are already designed. Deliver small, reviewable slices and cite the owning
spec row in the commit trailer.

- Find the owning row first with `git grep -n "<term>" -- specs` and extend the
  existing spec before adding requirement text. `PIPE-CONNSPEC-R135.4` is a
  central pipelines criterion; do not invent a local status row for it.
- Reuse the one `Connector` in `leanix_agent/__init__.py`, the API facades in
  `leanix_agent/`, the action-routed tools in `leanix_agent/mcp/`, and the
  existing ingestion boundary in `leanix_agent/instance_sync.py`. Do not create
  a second API, MCP, authentication, transport, or graph-write plane.
- Preserve the `LEANIX_WORKSPACE`, token, and OAuth settings in
  `leanix_agent/auth.py`, the SDK TLS resolution, and the existing REST/GraphQL
  split. Never hardcode a secret, endpoint, tenant, or TLS-verification bypass.
- Keep the source declarations, typed models, ontology mappings, and action
  registrations aligned with the SDK dynamic surface. Keep workspace, tenant,
  and installation data neutral.
- Every delivered requirement needs a bound focused test. Generated
  `specs/*/status.json` files come from the shared hooks; never hand-edit them.
- Keep `leanix_agent/skills/`, ontology, prompts, `mcp_config.json`, and source
  declarations coherent with the existing package-data and `leanix-mcp` entry
  point. One logical change per commit, using `Spec: none (<reason>)` for a
  central criterion with no local requirements row.

## Setup and gates

Use the locked environment, then run the shared gates:

```bash
uv sync --locked
uvx pre-commit run --all-files
uvx pre-commit run --all-files --hook-stage pre-push
```

For focused feedback, run the smallest affected test with the locked
environment:

```bash
uv run --locked --extra test pytest -q tests/test_skill_bundle.py
```

The canonical `.pre-commit-config.yaml` delegates connector-standard, secrets,
spec, tests-fast, and dependency-readiness checks to `Knuckles-Team/pipelines`
at `rev: main`. Do not copy those hooks locally or bypass a failing check.

## Connector-specific checks

- Keep LeanIX REST methods and Pathfinder GraphQL operations behind the existing
  client modules and action-routed MCP registration. Validate response models
  and translate provider failures through the existing SDK boundaries.
- Preserve token exchange, browser-auth fallback, and SDK TLS resolution. Mock
  LeanIX HTTP/GraphQL responses in local tests; never call a live workspace or
  use live credentials in a gate.
- Keep `leanix_agent/skills/`, `leanix_agent/ontology/`,
  `leanix_agent/connectors/`, prompts, and `mcp_config.json` in package data.
  Keep source declarations and ontology mappings explicit and
  installation-neutral.
- Documentation is published by `.github/workflows/pages.yml`, which calls
  `pages_pipeline.yml@main`. The Python release and rendered connector image
  are called by `.github/workflows/pipeline.yml`; do not add a second publisher
  or commit generated Docker artifacts.

## Packaging and publication

`pyproject.toml` declares the `leanix-mcp` entry point and packages `skills/**`,
agent data, ontology, connector content, and `mcp_config.json`. For a packaged
content release, keep the project version, `CHANGELOG.md`, and the editable
`leanix-agent` entry in `uv.lock` coherent, then inspect `uv build` output for
`leanix_agent/skills/leanix-agent-development/SKILL.md`.

The canonical release caller is `.github/workflows/pipeline.yml`: it publishes
the Python connector with `python_pipeline.yml@main`, then builds the rendered
connector container with `container_pipeline.yml@main` and
`render_connector: true`. Do not claim package, container, or Pages publication
from a local build; require exact-source hosted evidence and the public
artifact.

## Delivery discipline

Work in a real Git worktree based on `origin/main`. Inspect the complete diff,
stage only reviewed paths, and verify `git status --short` after every gate. Do
not use `git stash`, `git add -A`, or `git add .`; preserve unrelated working
tree changes. Keep runtime, ontology, source status, and generated artifacts
outside a bounded skill slice unless the owning requirement explicitly requires
them.
