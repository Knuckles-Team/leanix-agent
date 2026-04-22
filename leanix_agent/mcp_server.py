#!/usr/bin/python
import warnings

# Filter RequestsDependencyWarning early to prevent log spam
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    try:
        from requests.exceptions import RequestsDependencyWarning

        warnings.filterwarnings("ignore", category=RequestsDependencyWarning)
    except ImportError:
        pass

# General urllib3/chardet mismatch warnings
warnings.filterwarnings("ignore", message=".*urllib3.*or chardet.*")
warnings.filterwarnings("ignore", message=".*urllib3.*or charset_normalizer.*")

import inspect
import json
import logging
import os
import sys
from pathlib import Path
from typing import Any, Optional

from agent_utilities.base_utilities import to_boolean
from agent_utilities.mcp_utilities import (
    create_mcp_server,
)
from dotenv import find_dotenv, load_dotenv
from fastmcp import FastMCP
from fastmcp.utilities.logging import get_logger
from pydantic import Field
from starlette.requests import Request
from starlette.responses import JSONResponse

from leanix_agent.ai_inventory_builder_api import Api as AiInventoryBuilderApi
from leanix_agent.apptio_connector_api import Api as ApptioConnectorApi
from leanix_agent.auth import get_client
from leanix_agent.automations_api import Api as AutomationsApi
from leanix_agent.discovery_ai_agents_api import Api as DiscoveryAiAgentsApi
from leanix_agent.discovery_linking_v1_api import Api as DiscoveryLinkingV1Api
from leanix_agent.discovery_linking_v2_api import Api as DiscoveryLinkingV2Api
from leanix_agent.discovery_saas_api import Api as DiscoverySaasApi
from leanix_agent.discovery_sap_api import Api as DiscoverySapApi
from leanix_agent.discovery_sap_extension_api import Api as DiscoverySapExtensionApi
from leanix_agent.documents_api import Api as DocumentsApi
from leanix_agent.impacts_api import Api as ImpactsApi
from leanix_agent.integration_api_api import Api as IntegrationApiApi
from leanix_agent.integration_collibra_api import Api as IntegrationCollibraApi
from leanix_agent.integration_servicenow_api import Api as IntegrationServicenowApi
from leanix_agent.integration_signavio_api import Api as IntegrationSignavioApi
from leanix_agent.inventory_data_quality_api import Api as InventoryDataQualityApi
from leanix_agent.leanix_gql import GraphQL
from leanix_agent.managed_code_execution_api import Api as ManagedCodeExecutionApi
from leanix_agent.metrics_api import Api as MetricsApi
from leanix_agent.mtm_api import Api as MtmApi
from leanix_agent.navigation_api import Api as NavigationApi
from leanix_agent.pathfinder_api import Api as PathfinderApi
from leanix_agent.poll_api import Api as PollApi
from leanix_agent.reference_data_api import Api as ReferenceDataApi
from leanix_agent.reference_data_catalog_api import Api as ReferenceDataCatalogApi
from leanix_agent.storage_api import Api as StorageApi
from leanix_agent.survey_api import Api as SurveyApi
from leanix_agent.synclog_api import Api as SynclogApi
from leanix_agent.technology_discovery_api import Api as TechnologyDiscoveryApi
from leanix_agent.todo_api import Api as TodoApi
from leanix_agent.transformations_api import Api as TransformationsApi
from leanix_agent.webhooks_api import Api as WebhooksApi

__version__ = "0.1.29"

logger = get_logger(name="LeanixMCP")
logger.setLevel(logging.INFO)

API_CLASSES = {
    "ai_inventory_builder": AiInventoryBuilderApi,
    "apptio_connector": ApptioConnectorApi,
    "automations": AutomationsApi,
    "reference_data_catalog": ReferenceDataCatalogApi,
    "discovery_ai_agents": DiscoveryAiAgentsApi,
    "discovery_linking_v1": DiscoveryLinkingV1Api,
    "discovery_linking_v2": DiscoveryLinkingV2Api,
    "discovery_sap_extension": DiscoverySapExtensionApi,
    "discovery_saas": DiscoverySaasApi,
    "documents": DocumentsApi,
    "impacts": ImpactsApi,
    "integration_api": IntegrationApiApi,
    "integration_collibra": IntegrationCollibraApi,
    "integration_servicenow": IntegrationServicenowApi,
    "integration_signavio": IntegrationSignavioApi,
    "inventory_data_quality": InventoryDataQualityApi,
    "mtm": MtmApi,
    "managed_code_execution": ManagedCodeExecutionApi,
    "metrics": MetricsApi,
    "navigation": NavigationApi,
    "pathfinder": PathfinderApi,
    "poll": PollApi,
    "reference_data": ReferenceDataApi,
    "discovery_sap": DiscoverySapApi,
    "technology_discovery": TechnologyDiscoveryApi,
    "storage": StorageApi,
    "survey": SurveyApi,
    "synclog": SynclogApi,
    "todo": TodoApi,
    "transformations": TransformationsApi,
    "webhooks": WebhooksApi,
}


def load_tool_config() -> dict[str, dict[str, str]]:
    """Load tool tag mappings mapping."""
    config_path = Path(__file__).parent / "tool_tags.json"
    if not config_path.exists():
        logger.error(f"Missing {config_path}")
        return {}
    with open(config_path, encoding="utf-8") as f:
        return json.load(f)


def _generate_dynamic_tool(
    service: str, method_name: str, tag: str, api_class: type
) -> Any | None:
    method = getattr(api_class, method_name)
    sig = inspect.signature(method)
    docstring = method.__doc__ or f"Call {service} {method_name}"

    params_code = []
    call_args = []

    for name, param in list(sig.parameters.items())[1:]:
        if name == "kwargs":
            continue
        try:
            type_str = str(param.annotation).replace("typing.", "")
            if "class" in type_str:
                type_str = param.annotation.__name__
        except Exception:
            type_str = "Any"

        if param.default is inspect.Parameter.empty:
            field_def = f"Field(..., description='{name}')"
        else:
            field_def = f"Field(default={repr(param.default)}, description='{name}')"

        params_code.append(f"    {name}: {type_str} = {field_def}")
        call_args.append(f"{name}={name}")

    params_str = ",\n".join(params_code)
    call_args_str = ", ".join(call_args)
    if params_str:
        params_str += ",\n"
    tool_name = f"{service}_{method_name}"
    func_source = f'''
async def {tool_name}(
{params_str}
    base_url: str = Field(default=os.environ.get("LEANIX_URL", None), description="Base URL"),
    api_token: Optional[str] = Field(default=os.environ.get("LEANIX_TOKEN", None), description="API Key"),
    verify: bool = Field(default=to_boolean(os.environ.get("LEANIX_VERIFY", "False")), description="Verify SSL")
) -> Dict:
    """{docstring}"""
    client = api_class(
        base_url=base_url,
        token=api_token,
        verify=verify
    )
    return client.{method_name}({call_args_str})
'''

    local_env = {}
    global_env = {
        "os": os,
        "Field": Field,
        "Optional": Optional,
        "Dict": dict,
        "List": list,
        "Any": Any,
        "to_boolean": to_boolean,
        "api_class": api_class,
    }

    try:
        exec(func_source, global_env, local_env)
        wrapper_func = local_env[tool_name]
        return wrapper_func
    except Exception as e:
        logger.error(f"Failed to compile dynamic tool {service}.{method_name}: {e}")
        return None


def register_dynamic_tools(
    mcp: FastMCP, filter_tags: list[str] | None = None
) -> list[str]:
    tool_config = load_tool_config()
    registered_tags = set()

    if not hasattr(register_dynamic_tools, "_registered_tool_names"):
        register_dynamic_tools._registered_tool_names = set()

    for service, methods in tool_config.items():
        if service not in API_CLASSES:
            continue

        api_class = API_CLASSES[service]

        for method_name, tag in methods.items():
            if filter_tags and tag not in filter_tags:
                continue

            tool_name = f"{service}_{method_name}"
            if tool_name in register_dynamic_tools._registered_tool_names:
                continue

            wrapper_func = _generate_dynamic_tool(service, method_name, tag, api_class)
            if wrapper_func:
                mcp.tool(
                    name=wrapper_func.__name__,
                    description=wrapper_func.__doc__,
                    tags={tag},
                )(wrapper_func)
                register_dynamic_tools._registered_tool_names.add(tool_name)
                registered_tags.add(tag)

    return sorted(list(registered_tags))


def register_graphql_tools(mcp: FastMCP):
    @mcp.tool(
        name="graphql_query",
        description="Execute a GraphQL query against LeanIX Enterprise Architecture Management.",
        tags={"graphql"},
    )
    def graphql_query_tool(
        query: str = Field(..., description="The GraphQL query string."),
    ) -> Any:
        """Execute a GraphQL query."""
        api = get_client()
        gql_client = GraphQL(
            url=api.base_url, token=api.access_token, verify=api.verify
        )
        return gql_client.query(query_str=query)


def get_mcp_instance() -> tuple[Any, Any, Any, Any]:
    """Initialize and return the MCP instance, args, and middlewares."""
    load_dotenv(find_dotenv())
    args, mcp, middlewares = create_mcp_server(
        name="LeanIX Agent MCP",
        version=__version__,
        instructions="LeanIX Agent MCP Server - Dynamic generation for dozens of LeanIX services.",
    )

    @mcp.custom_route("/health", methods=["GET"])
    async def health_check(request: Request) -> JSONResponse:
        return JSONResponse({"status": "OK"})

    registered_tags = []

    DEFAULT_LEANIX_AI_INVENTORY_BUILDERTOOL = to_boolean(
        os.getenv("LEANIX_AI_INVENTORY_BUILDERTOOL", "True")
    )
    if DEFAULT_LEANIX_AI_INVENTORY_BUILDERTOOL:
        registered_tags.extend(
            register_dynamic_tools(mcp, filter_tags=["leanix-ai-inventory-builder"])
        )

    DEFAULT_LEANIX_APPTIO_CONNECTORTOOL = to_boolean(
        os.getenv("LEANIX_APPTIO_CONNECTORTOOL", "True")
    )
    if DEFAULT_LEANIX_APPTIO_CONNECTORTOOL:
        registered_tags.extend(
            register_dynamic_tools(mcp, filter_tags=["leanix-apptio-connector"])
        )

    DEFAULT_LEANIX_AUTOMATIONSTOOL = to_boolean(
        os.getenv("LEANIX_AUTOMATIONSTOOL", "True")
    )
    if DEFAULT_LEANIX_AUTOMATIONSTOOL:
        registered_tags.extend(
            register_dynamic_tools(mcp, filter_tags=["leanix-automations"])
        )

    DEFAULT_LEANIX_DISCOVERY_AI_AGENTSTOOL = to_boolean(
        os.getenv("LEANIX_DISCOVERY_AI_AGENTSTOOL", "True")
    )
    if DEFAULT_LEANIX_DISCOVERY_AI_AGENTSTOOL:
        registered_tags.extend(
            register_dynamic_tools(mcp, filter_tags=["leanix-discovery-ai-agents"])
        )

    DEFAULT_LEANIX_DISCOVERY_LINKING_V1TOOL = to_boolean(
        os.getenv("LEANIX_DISCOVERY_LINKING_V1TOOL", "True")
    )
    if DEFAULT_LEANIX_DISCOVERY_LINKING_V1TOOL:
        registered_tags.extend(
            register_dynamic_tools(mcp, filter_tags=["leanix-discovery-linking-v1"])
        )

    DEFAULT_LEANIX_DISCOVERY_LINKING_V2TOOL = to_boolean(
        os.getenv("LEANIX_DISCOVERY_LINKING_V2TOOL", "True")
    )
    if DEFAULT_LEANIX_DISCOVERY_LINKING_V2TOOL:
        registered_tags.extend(
            register_dynamic_tools(mcp, filter_tags=["leanix-discovery-linking-v2"])
        )

    DEFAULT_LEANIX_DISCOVERY_SAASTOOL = to_boolean(
        os.getenv("LEANIX_DISCOVERY_SAASTOOL", "True")
    )
    if DEFAULT_LEANIX_DISCOVERY_SAASTOOL:
        registered_tags.extend(
            register_dynamic_tools(mcp, filter_tags=["leanix-discovery-saas"])
        )

    DEFAULT_LEANIX_DISCOVERY_SAPTOOL = to_boolean(
        os.getenv("LEANIX_DISCOVERY_SAPTOOL", "True")
    )
    if DEFAULT_LEANIX_DISCOVERY_SAPTOOL:
        registered_tags.extend(
            register_dynamic_tools(mcp, filter_tags=["leanix-discovery-sap"])
        )

    DEFAULT_LEANIX_DISCOVERY_SAP_EXTENSIONTOOL = to_boolean(
        os.getenv("LEANIX_DISCOVERY_SAP_EXTENSIONTOOL", "True")
    )
    if DEFAULT_LEANIX_DISCOVERY_SAP_EXTENSIONTOOL:
        registered_tags.extend(
            register_dynamic_tools(mcp, filter_tags=["leanix-discovery-sap-extension"])
        )

    DEFAULT_LEANIX_DOCUMENTSTOOL = to_boolean(os.getenv("LEANIX_DOCUMENTSTOOL", "True"))
    if DEFAULT_LEANIX_DOCUMENTSTOOL:
        registered_tags.extend(
            register_dynamic_tools(mcp, filter_tags=["leanix-documents"])
        )

    DEFAULT_LEANIX_IMPACTSTOOL = to_boolean(os.getenv("LEANIX_IMPACTSTOOL", "True"))
    if DEFAULT_LEANIX_IMPACTSTOOL:
        registered_tags.extend(
            register_dynamic_tools(mcp, filter_tags=["leanix-impacts"])
        )

    DEFAULT_LEANIX_INTEGRATION_APITOOL = to_boolean(
        os.getenv("LEANIX_INTEGRATION_APITOOL", "True")
    )
    if DEFAULT_LEANIX_INTEGRATION_APITOOL:
        registered_tags.extend(
            register_dynamic_tools(mcp, filter_tags=["leanix-integration-api"])
        )

    DEFAULT_LEANIX_INTEGRATION_COLLIBRATOOL = to_boolean(
        os.getenv("LEANIX_INTEGRATION_COLLIBRATOOL", "True")
    )
    if DEFAULT_LEANIX_INTEGRATION_COLLIBRATOOL:
        registered_tags.extend(
            register_dynamic_tools(mcp, filter_tags=["leanix-integration-collibra"])
        )

    DEFAULT_LEANIX_INTEGRATION_SERVICENOWTOOL = to_boolean(
        os.getenv("LEANIX_INTEGRATION_SERVICENOWTOOL", "True")
    )
    if DEFAULT_LEANIX_INTEGRATION_SERVICENOWTOOL:
        registered_tags.extend(
            register_dynamic_tools(mcp, filter_tags=["leanix-integration-servicenow"])
        )

    DEFAULT_LEANIX_INTEGRATION_SIGNAVIOTOOL = to_boolean(
        os.getenv("LEANIX_INTEGRATION_SIGNAVIOTOOL", "True")
    )
    if DEFAULT_LEANIX_INTEGRATION_SIGNAVIOTOOL:
        registered_tags.extend(
            register_dynamic_tools(mcp, filter_tags=["leanix-integration-signavio"])
        )

    DEFAULT_LEANIX_INVENTORY_DATA_QUALITYTOOL = to_boolean(
        os.getenv("LEANIX_INVENTORY_DATA_QUALITYTOOL", "True")
    )
    if DEFAULT_LEANIX_INVENTORY_DATA_QUALITYTOOL:
        registered_tags.extend(
            register_dynamic_tools(mcp, filter_tags=["leanix-inventory-data-quality"])
        )

    DEFAULT_LEANIX_MANAGED_CODE_EXECUTIONTOOL = to_boolean(
        os.getenv("LEANIX_MANAGED_CODE_EXECUTIONTOOL", "True")
    )
    if DEFAULT_LEANIX_MANAGED_CODE_EXECUTIONTOOL:
        registered_tags.extend(
            register_dynamic_tools(mcp, filter_tags=["leanix-managed-code-execution"])
        )

    DEFAULT_LEANIX_METRICSTOOL = to_boolean(os.getenv("LEANIX_METRICSTOOL", "True"))
    if DEFAULT_LEANIX_METRICSTOOL:
        registered_tags.extend(
            register_dynamic_tools(mcp, filter_tags=["leanix-metrics"])
        )

    DEFAULT_LEANIX_MTMTOOL = to_boolean(os.getenv("LEANIX_MTMTOOL", "True"))
    if DEFAULT_LEANIX_MTMTOOL:
        registered_tags.extend(register_dynamic_tools(mcp, filter_tags=["leanix-mtm"]))

    DEFAULT_LEANIX_NAVIGATIONTOOL = to_boolean(
        os.getenv("LEANIX_NAVIGATIONTOOL", "True")
    )
    if DEFAULT_LEANIX_NAVIGATIONTOOL:
        registered_tags.extend(
            register_dynamic_tools(mcp, filter_tags=["leanix-navigation"])
        )

    DEFAULT_LEANIX_PATHFINDERTOOL = to_boolean(
        os.getenv("LEANIX_PATHFINDERTOOL", "True")
    )
    if DEFAULT_LEANIX_PATHFINDERTOOL:
        registered_tags.extend(
            register_dynamic_tools(mcp, filter_tags=["leanix-pathfinder"])
        )

    DEFAULT_LEANIX_POLLTOOL = to_boolean(os.getenv("LEANIX_POLLTOOL", "True"))
    if DEFAULT_LEANIX_POLLTOOL:
        registered_tags.extend(register_dynamic_tools(mcp, filter_tags=["leanix-poll"]))

    DEFAULT_LEANIX_REFERENCE_DATATOOL = to_boolean(
        os.getenv("LEANIX_REFERENCE_DATATOOL", "True")
    )
    if DEFAULT_LEANIX_REFERENCE_DATATOOL:
        registered_tags.extend(
            register_dynamic_tools(mcp, filter_tags=["leanix-reference-data"])
        )

    DEFAULT_LEANIX_REFERENCE_DATA_CATALOGTOOL = to_boolean(
        os.getenv("LEANIX_REFERENCE_DATA_CATALOGTOOL", "True")
    )
    if DEFAULT_LEANIX_REFERENCE_DATA_CATALOGTOOL:
        registered_tags.extend(
            register_dynamic_tools(mcp, filter_tags=["leanix-reference-data-catalog"])
        )

    DEFAULT_LEANIX_STORAGETOOL = to_boolean(os.getenv("LEANIX_STORAGETOOL", "True"))
    if DEFAULT_LEANIX_STORAGETOOL:
        registered_tags.extend(
            register_dynamic_tools(mcp, filter_tags=["leanix-storage"])
        )

    DEFAULT_LEANIX_SURVEYTOOL = to_boolean(os.getenv("LEANIX_SURVEYTOOL", "True"))
    if DEFAULT_LEANIX_SURVEYTOOL:
        registered_tags.extend(
            register_dynamic_tools(mcp, filter_tags=["leanix-survey"])
        )

    DEFAULT_LEANIX_SYNCLOGTOOL = to_boolean(os.getenv("LEANIX_SYNCLOGTOOL", "True"))
    if DEFAULT_LEANIX_SYNCLOGTOOL:
        registered_tags.extend(
            register_dynamic_tools(mcp, filter_tags=["leanix-synclog"])
        )

    DEFAULT_LEANIX_TECHNOLOGY_DISCOVERYTOOL = to_boolean(
        os.getenv("LEANIX_TECHNOLOGY_DISCOVERYTOOL", "True")
    )
    if DEFAULT_LEANIX_TECHNOLOGY_DISCOVERYTOOL:
        registered_tags.extend(
            register_dynamic_tools(mcp, filter_tags=["leanix-technology-discovery"])
        )

    DEFAULT_LEANIX_TODOTOOL = to_boolean(os.getenv("LEANIX_TODOTOOL", "True"))
    if DEFAULT_LEANIX_TODOTOOL:
        registered_tags.extend(register_dynamic_tools(mcp, filter_tags=["leanix-todo"]))

    DEFAULT_LEANIX_TRANSFORMATIONSTOOL = to_boolean(
        os.getenv("LEANIX_TRANSFORMATIONSTOOL", "True")
    )
    if DEFAULT_LEANIX_TRANSFORMATIONSTOOL:
        registered_tags.extend(
            register_dynamic_tools(mcp, filter_tags=["leanix-transformations"])
        )

    DEFAULT_LEANIX_WEBHOOKSTOOL = to_boolean(os.getenv("LEANIX_WEBHOOKSTOOL", "True"))
    if DEFAULT_LEANIX_WEBHOOKSTOOL:
        registered_tags.extend(
            register_dynamic_tools(mcp, filter_tags=["leanix-webhooks"])
        )

    DEFAULT_GRAPHQLTOOL = to_boolean(os.getenv("GRAPHQLTOOL", "True"))
    if DEFAULT_GRAPHQLTOOL:
        register_graphql_tools(mcp)
        registered_tags.append("graphql")

    for mw in middlewares:
        mcp.add_middleware(mw)
    return mcp, args, middlewares, registered_tags


def mcp_server() -> None:
    mcp, args, middlewares, registered_tags = get_mcp_instance()
    print(f"{'leanix-agent'} MCP v{__version__}", file=sys.stderr)
    print("\nStarting MCP Server", file=sys.stderr)
    print(f"  Transport: {args.transport.upper()}", file=sys.stderr)
    print(f"  Auth: {args.auth_type}", file=sys.stderr)
    print(f"  Dynamic Tags Loaded: {len(set(registered_tags))}", file=sys.stderr)

    if args.transport == "stdio":
        mcp.run(transport="stdio")
    elif args.transport == "streamable-http":
        mcp.run(transport="streamable-http", host=args.host, port=args.port)
    elif args.transport == "sse":
        mcp.run(transport="sse", host=args.host, port=args.port)
    else:
        logger.error("Invalid transport", extra={"transport": args.transport})
        sys.exit(1)


if __name__ == "__main__":
    mcp_server()
