# Package leanix_agent.mcp

from leanix_agent.mcp.mcp_graphql import register_graphql_tools
from leanix_agent.mcp.mcp_instance_graph import register_instance_graph_tools
from leanix_agent.mcp.mcp_pathfinder import register_leanix_pathfinder_tools
from leanix_agent.mcp.mcp_universal_api import register_universal_api_tools

__all__ = [
    "register_graphql_tools",
    "register_instance_graph_tools",
    "register_leanix_pathfinder_tools",
    "register_universal_api_tools",
]
