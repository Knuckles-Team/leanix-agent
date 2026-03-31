"""LeanIX graph configuration — tag prompts and env var mappings.

This is the only file needed to enable graph mode for this agent.
Provides TAG_PROMPTS and TAG_ENV_VARS for create_graph_agent_server().
"""

TAG_PROMPTS: dict[str, str] = {
    "graphql": (
        "You are a LeanIX Graphql specialist. Help users manage and interact with Graphql functionality using the available tools."
    ),
    "leanix_ai_inventory_builder": (
        "You are a LeanIX Leanix Ai Inventory Builder specialist. Help users manage and interact with Leanix Ai Inventory Builder functionality using the available tools."
    ),
    "leanix_apptio_connector": (
        "You are a LeanIX Leanix Apptio Connector specialist. Help users manage and interact with Leanix Apptio Connector functionality using the available tools."
    ),
    "leanix_automations": (
        "You are a LeanIX Leanix Automations specialist. Help users manage and interact with Leanix Automations functionality using the available tools."
    ),
    "leanix_discovery_ai_agents": (
        "You are a LeanIX Leanix Discovery Ai Agents specialist. Help users manage and interact with Leanix Discovery Ai Agents functionality using the available tools."
    ),
    "leanix_discovery_linking_v1": (
        "You are a LeanIX Leanix Discovery Linking V1 specialist. Help users manage and interact with Leanix Discovery Linking V1 functionality using the available tools."
    ),
    "leanix_discovery_linking_v2": (
        "You are a LeanIX Leanix Discovery Linking V2 specialist. Help users manage and interact with Leanix Discovery Linking V2 functionality using the available tools."
    ),
    "leanix_discovery_saas": (
        "You are a LeanIX Leanix Discovery Saas specialist. Help users manage and interact with Leanix Discovery Saas functionality using the available tools."
    ),
    "leanix_discovery_sap": (
        "You are a LeanIX Leanix Discovery Sap specialist. Help users manage and interact with Leanix Discovery Sap functionality using the available tools."
    ),
    "leanix_discovery_sap_extension": (
        "You are a LeanIX Leanix Discovery Sap Extension specialist. Help users manage and interact with Leanix Discovery Sap Extension functionality using the available tools."
    ),
    "leanix_documents": (
        "You are a LeanIX Leanix Documents specialist. Help users manage and interact with Leanix Documents functionality using the available tools."
    ),
    "leanix_impacts": (
        "You are a LeanIX Leanix Impacts specialist. Help users manage and interact with Leanix Impacts functionality using the available tools."
    ),
    "leanix_integration_api": (
        "You are a LeanIX Leanix Integration Api specialist. Help users manage and interact with Leanix Integration Api functionality using the available tools."
    ),
    "leanix_integration_collibra": (
        "You are a LeanIX Leanix Integration Collibra specialist. Help users manage and interact with Leanix Integration Collibra functionality using the available tools."
    ),
    "leanix_integration_servicenow": (
        "You are a LeanIX Leanix Integration Servicenow specialist. Help users manage and interact with Leanix Integration Servicenow functionality using the available tools."
    ),
    "leanix_integration_signavio": (
        "You are a LeanIX Leanix Integration Signavio specialist. Help users manage and interact with Leanix Integration Signavio functionality using the available tools."
    ),
    "leanix_inventory_data_quality": (
        "You are a LeanIX Leanix Inventory Data Quality specialist. Help users manage and interact with Leanix Inventory Data Quality functionality using the available tools."
    ),
    "leanix_managed_code_execution": (
        "You are a LeanIX Leanix Managed Code Execution specialist. Help users manage and interact with Leanix Managed Code Execution functionality using the available tools."
    ),
    "leanix_metrics": (
        "You are a LeanIX Leanix Metrics specialist. Help users manage and interact with Leanix Metrics functionality using the available tools."
    ),
    "leanix_mtm": (
        "You are a LeanIX Leanix Mtm specialist. Help users manage and interact with Leanix Mtm functionality using the available tools."
    ),
    "leanix_navigation": (
        "You are a LeanIX Leanix Navigation specialist. Help users manage and interact with Leanix Navigation functionality using the available tools."
    ),
    "leanix_pathfinder": (
        "You are a LeanIX Leanix Pathfinder specialist. Help users manage and interact with Leanix Pathfinder functionality using the available tools."
    ),
    "leanix_poll": (
        "You are a LeanIX Leanix Poll specialist. Help users manage and interact with Leanix Poll functionality using the available tools."
    ),
    "leanix_reference_data": (
        "You are a LeanIX Leanix Reference Data specialist. Help users manage and interact with Leanix Reference Data functionality using the available tools."
    ),
    "leanix_reference_data_catalog": (
        "You are a LeanIX Leanix Reference Data Catalog specialist. Help users manage and interact with Leanix Reference Data Catalog functionality using the available tools."
    ),
    "leanix_storage": (
        "You are a LeanIX Leanix Storage specialist. Help users manage and interact with Leanix Storage functionality using the available tools."
    ),
    "leanix_survey": (
        "You are a LeanIX Leanix Survey specialist. Help users manage and interact with Leanix Survey functionality using the available tools."
    ),
    "leanix_synclog": (
        "You are a LeanIX Leanix Synclog specialist. Help users manage and interact with Leanix Synclog functionality using the available tools."
    ),
    "leanix_technology_discovery": (
        "You are a LeanIX Leanix Technology Discovery specialist. Help users manage and interact with Leanix Technology Discovery functionality using the available tools."
    ),
    "leanix_todo": (
        "You are a LeanIX Leanix Todo specialist. Help users manage and interact with Leanix Todo functionality using the available tools."
    ),
    "leanix_transformations": (
        "You are a LeanIX Leanix Transformations specialist. Help users manage and interact with Leanix Transformations functionality using the available tools."
    ),
    "leanix_webhooks": (
        "You are a LeanIX Leanix Webhooks specialist. Help users manage and interact with Leanix Webhooks functionality using the available tools."
    ),
}


TAG_ENV_VARS: dict[str, str] = {
    "graphql": "GRAPHQLTOOL",
    "leanix_ai_inventory_builder": "LEANIX_AI_INVENTORY_BUILDERTOOL",
    "leanix_apptio_connector": "LEANIX_APPTIO_CONNECTORTOOL",
    "leanix_automations": "LEANIX_AUTOMATIONSTOOL",
    "leanix_discovery_ai_agents": "LEANIX_DISCOVERY_AI_AGENTSTOOL",
    "leanix_discovery_linking_v1": "LEANIX_DISCOVERY_LINKING_V1TOOL",
    "leanix_discovery_linking_v2": "LEANIX_DISCOVERY_LINKING_V2TOOL",
    "leanix_discovery_saas": "LEANIX_DISCOVERY_SAASTOOL",
    "leanix_discovery_sap": "LEANIX_DISCOVERY_SAPTOOL",
    "leanix_discovery_sap_extension": "LEANIX_DISCOVERY_SAP_EXTENSIONTOOL",
    "leanix_documents": "LEANIX_DOCUMENTSTOOL",
    "leanix_impacts": "LEANIX_IMPACTSTOOL",
    "leanix_integration_api": "LEANIX_INTEGRATION_APITOOL",
    "leanix_integration_collibra": "LEANIX_INTEGRATION_COLLIBRATOOL",
    "leanix_integration_servicenow": "LEANIX_INTEGRATION_SERVICENOWTOOL",
    "leanix_integration_signavio": "LEANIX_INTEGRATION_SIGNAVIOTOOL",
    "leanix_inventory_data_quality": "LEANIX_INVENTORY_DATA_QUALITYTOOL",
    "leanix_managed_code_execution": "LEANIX_MANAGED_CODE_EXECUTIONTOOL",
    "leanix_metrics": "LEANIX_METRICSTOOL",
    "leanix_mtm": "LEANIX_MTMTOOL",
    "leanix_navigation": "LEANIX_NAVIGATIONTOOL",
    "leanix_pathfinder": "LEANIX_PATHFINDERTOOL",
    "leanix_poll": "LEANIX_POLLTOOL",
    "leanix_reference_data": "LEANIX_REFERENCE_DATATOOL",
    "leanix_reference_data_catalog": "LEANIX_REFERENCE_DATA_CATALOGTOOL",
    "leanix_storage": "LEANIX_STORAGETOOL",
    "leanix_survey": "LEANIX_SURVEYTOOL",
    "leanix_synclog": "LEANIX_SYNCLOGTOOL",
    "leanix_technology_discovery": "LEANIX_TECHNOLOGY_DISCOVERYTOOL",
    "leanix_todo": "LEANIX_TODOTOOL",
    "leanix_transformations": "LEANIX_TRANSFORMATIONSTOOL",
    "leanix_webhooks": "LEANIX_WEBHOOKSTOOL",
}
