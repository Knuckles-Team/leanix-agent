#!/usr/bin/python
import logging
import os
import sys
import warnings

from agent_utilities import create_agent_parser, create_agent_server

__version__ = "1.0.1"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


DEFAULT_AGENT_NAME = os.getenv("DEFAULT_AGENT_NAME", "LeanIX Agent")
DEFAULT_AGENT_DESCRIPTION = os.getenv(
    "AGENT_DESCRIPTION",
    "Agent package for communicating with LeanIX Enterprise Architecture Management via REST APIs and GraphQL.",
)
DEFAULT_AGENT_SYSTEM_PROMPT = os.getenv("AGENT_SYSTEM_PROMPT", "")


def _initialize_agent_identity() -> None:
    """Load workspace identity only after CLI argument parsing has completed."""
    global DEFAULT_AGENT_DESCRIPTION, DEFAULT_AGENT_NAME, DEFAULT_AGENT_SYSTEM_PROMPT

    from agent_utilities import (
        build_system_prompt_from_workspace,
        initialize_workspace,
        load_identity,
    )

    initialize_workspace()
    meta = load_identity()
    DEFAULT_AGENT_NAME = os.getenv(
        "DEFAULT_AGENT_NAME", meta.get("name", DEFAULT_AGENT_NAME)
    )
    DEFAULT_AGENT_DESCRIPTION = os.getenv(
        "AGENT_DESCRIPTION", meta.get("description", DEFAULT_AGENT_DESCRIPTION)
    )
    DEFAULT_AGENT_SYSTEM_PROMPT = os.getenv(
        "AGENT_SYSTEM_PROMPT",
        meta.get("content") or build_system_prompt_from_workspace(),
    )


def agent_server():
    """Bootstrapper and entry point for starting the LeanIX Agent service and CLI.

    Configures and spawns the Pydantic AI Graph Agent server and links integrated MCP tools.

    CONCEPT:AU-ORCH.execution.inject-signal-board-observations
    CONCEPT:AU-ORCH.planning.legal-automation-roadmap
    """
    warnings.filterwarnings("ignore", message=".*urllib3.*or chardet.*")
    warnings.filterwarnings("ignore", category=DeprecationWarning, module="fastmcp")

    parser = create_agent_parser()
    args = parser.parse_args()
    _initialize_agent_identity()
    print(f"{DEFAULT_AGENT_NAME} v{__version__}", file=sys.stderr)

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.debug("Debug mode enabled")

    # Start server using the auto-discovery pattern (from mcp_config.json)
    create_agent_server(
        mcp_url=args.mcp_url,
        mcp_config=args.mcp_config or "mcp_config.json",
        host=args.host,
        port=args.port,
        provider=args.provider,
        model_id=args.model_id,
        router_model=args.model_id,
        agent_model=args.model_id,
        base_url=args.base_url,
        api_key=args.api_key,
        custom_skills_directory=args.custom_skills_directory,
        enable_web_ui=args.web,
        enable_otel=args.otel,
        otel_endpoint=args.otel_endpoint,
        otel_headers=args.otel_headers,
        otel_public_key=args.otel_public_key,
        otel_secret_key=args.otel_secret_key,
        otel_protocol=args.otel_protocol,
        debug=args.debug,
    )


if __name__ == "__main__":
    agent_server()
