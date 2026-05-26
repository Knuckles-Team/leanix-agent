from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import get_graphql_client


def register_graphql_tools(mcp: FastMCP):

    @mcp.tool(tags={"graphql"})
    async def leanix_graphql(
        query: str = Field(
            description="The raw GraphQL query or mutation string to execute against the LeanIX Pathfinder API."
        ),
        variables: str = Field(
            default="{}",
            description="JSON string of variables to pass along with the query.",
        ),
        operation_name: str | None = Field(
            default=None,
            description="Optional operation name if executing a specific query within the document.",
        ),
        client=Depends(get_graphql_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Execute raw GraphQL queries and mutations natively on LeanIX Pathfinder API."""
        if ctx:
            await ctx.info("Executing LeanIX GraphQL query...")
        import json

        try:
            vars_dict = json.loads(variables) if variables else None
        except Exception as e:
            return {"error": f"Invalid variables JSON: {e}"}

        try:
            return client.execute_gql(
                query_str=query, variables=vars_dict, operation_name=operation_name
            )
        except Exception as e:
            return {"error": f"GraphQL execution failed: {str(e)}"}
