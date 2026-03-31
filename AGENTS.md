# AGENTS.md

## Tech Stack & Architecture
- Language/Version: Python 3.10+
- Core Libraries: `agent-utilities`, `fastmcp`, `pydantic-ai`
- Key principles: Functional patterns, Pydantic for data validation, asynchronous tool execution.
- Architecture:
    - `mcp_server.py`: Main MCP server entry point and tool registration.
    - `agent.py`: Pydantic AI agent definition and logic.
    - `skills/`: Directory containing modular agent skills (if applicable).
    - `agent/`: Internal agent logic and prompt templates.

### Architecture Diagram
```mermaid
graph TD
    User([User/A2A]) --> Server[A2A Server / FastAPI]
    Server --> Agent[Pydantic AI Agent]
    Agent --> Skills[Modular Skills]
    Agent --> MCP[MCP Server / FastMCP]
    MCP --> Client[API Client / Wrapper]
    Client --> ExternalAPI([External Service API])
```

### Workflow Diagram
```mermaid
sequenceDiagram
    participant U as User
    participant S as Server
    participant A as Agent
    participant T as MCP Tool
    participant API as External API

    U->>S: Request
    S->>A: Process Query
    A->>T: Invoke Tool
    T->>API: API Request
    API-->>T: API Response
    T-->>A: Tool Result
    A-->>S: Final Response
    S-->>U: Output
```

## Commands (run these exactly)
# Installation
pip install .[all]

# Quality & Linting (run from project root)
pre-commit run --all-files

# Execution Commands
# leanix-mcp\nleanix_agent.mcp:mcp_server\n# leanix-agent\nleanix_agent.agent:agent_server

## Project Structure Quick Reference
- MCP Entry Point → `mcp_server.py`
- Agent Entry Point → `agent.py`
- Source Code → `leanix_agent/`
- Skills → `skills/` (if exists)

### File Tree
```text
├── .bumpversion.cfg\n├── .dockerignore\n├── .env\n├── .gitattributes\n├── .gitignore\n├── .pre-commit-config.yaml\n├── AGENTS.md\n├── Dockerfile\n├── LICENSE\n├── MANIFEST.in\n├── README.md\n├── compose.yml\n├── debug.Dockerfile\n├── leanix_agent\n│   ├── __init__.py\n│   ├── agent\n│   │   ├── AGENTS.md\n│   │   ├── CRON.md\n│   │   ├── CRON_LOG.md\n│   │   ├── HEARTBEAT.md\n│   │   ├── IDENTITY.md\n│   │   ├── MEMORY.md\n│   │   ├── USER.md\n│   │   └── mcp_config.json\n│   ├── agent.py\n│   ├── ai_inventory_builder_api.py\n│   ├── apptio_connector_api.py\n│   ├── auth.py\n│   ├── automations_api.py\n│   ├── discovery_ai_agents_api.py\n│   ├── discovery_linking_v1_api.py\n│   ├── discovery_linking_v2_api.py\n│   ├── discovery_saas_api.py\n│   ├── discovery_sap_api.py\n│   ├── discovery_sap_extension_api.py\n│   ├── documents_api.py\n│   ├── impacts_api.py\n│   ├── integration_api_api.py\n│   ├── integration_collibra_api.py\n│   ├── integration_servicenow_api.py\n│   ├── integration_signavio_api.py\n│   ├── inventory_data_quality_api.py\n│   ├── leanix_agent_models.py\n│   ├── leanix_api.py\n│   ├── leanix_gql.py\n│   ├── managed_code_execution_api.py\n│   ├── mcp_server.py\n│   ├── metrics_api.py\n│   ├── mtm_api.py\n│   ├── navigation_api.py\n│   ├── pathfinder_api.py\n│   ├── poll_api.py\n│   ├── reference_data_api.py\n│   ├── reference_data_catalog_api.py\n│   ├── skills\n│   │   └── leanix-agent-docs\n│   ├── storage_api.py\n│   ├── survey_api.py\n│   ├── synclog_api.py\n│   ├── technology_discovery_api.py\n│   ├── todo_api.py\n│   ├── tool_tags.json\n│   ├── transformations_api.py\n│   └── webhooks_api.py\n├── leanix_agent.egg-info\n│   ├── PKG-INFO\n│   ├── SOURCES.txt\n│   ├── dependency_links.txt\n│   ├── entry_points.txt\n│   ├── requires.txt\n│   └── top_level.txt\n├── pyproject.toml\n├── requirements.txt\n└── scripts\n    └── generate_leanix.py
```

## Code Style & Conventions
**Always:**
- Use `agent-utilities` for common patterns (e.g., `create_mcp_server`, `create_agent`).
- Define input/output models using Pydantic.
- Include descriptive docstrings for all tools (they are used as tool descriptions for LLMs).
- Check for optional dependencies using `try/except ImportError`.

**Good example:**
```python
from agent_utilities import create_mcp_server
from mcp.server.fastmcp import FastMCP

mcp = create_mcp_server("my-agent")

@mcp.tool()
async def my_tool(param: str) -> str:
    """Description for LLM."""
    return f"Result: {param}"
```

## Dos and Don'ts
**Do:**
- Run `pre-commit` before pushing changes.
- Use existing patterns from `agent-utilities`.
- Keep tools focused and idempotent where possible.

**Don't:**
- Use `cd` commands in scripts; use absolute paths or relative to project root.
- Add new dependencies to `dependencies` in `pyproject.toml` without checking `optional-dependencies` first.
- Hardcode secrets; use environment variables or `.env` files.

## Safety & Boundaries
**Always do:**
- Run lint/test via `pre-commit`.
- Use `agent-utilities` base classes.

**Ask first:**
- Major refactors of `mcp_server.py` or `agent.py`.
- Deleting or renaming public tool functions.

**Never do:**
- Commit `.env` files or secrets.
- Modify `agent-utilities` or `universal-skills` files from within this package.

## When Stuck
- Propose a plan first before making large changes.
- Check `agent-utilities` documentation for existing helpers.


## Graph Architecture

This agent uses `pydantic-graph` orchestration for intelligent routing and optimal context management.

```mermaid
---
title: LeanIX Agent Graph Agent
---
stateDiagram-v2
  [*] --> RouterNode: User Query
  RouterNode --> DomainNode: Classified Domain
  RouterNode --> [*]: Low confidence / Error
  DomainNode --> [*]: Domain Result
```

- **RouterNode**: A fast, lightweight LLM (e.g., `nvidia/nemotron-3-super`) that classifies the user's query into one of the specialized domains.
- **DomainNode**: The executor node. For the selected domain, it dynamically sets environment variables to temporarily enable ONLY the tools relevant to that domain, creating a highly focused sub-agent (e.g., `gpt-4o`) to complete the request. This preserves LLM context and prevents tool hallucination.
