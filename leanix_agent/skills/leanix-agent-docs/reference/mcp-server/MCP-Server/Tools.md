##  Tools
The MCP server exposes API capabilities as discoverable tools that AI applications can invoke. Each tool includes structured metadata that describes inputs, outputs, and usage. The availability of tools depends on user permissions. For more details, see [API Token Permissions](https://help.sap.com/docs/leanix/ea/connecting-to-mcp-server?locale=en-US&state=PRODUCTION&version=CLOUD#loio19c0723e588e43519756d8bebf163048__section_by2_sh4_2hc).
### Base AI Capabilities
To use tools with AI features, you need to activate base AI capabilities in your workspace. The MCP server doesn't include built-in AI functionality. Instead, it integrates with existing base AI capabilities in SAP LeanIX to offer enhanced features. For more details, see [Base AI Capabilities](https://help.sap.com/docs/leanix/ea/base-ai-capabilities?locale=en-US&state=PRODUCTION&version=CLOUD "SAP LeanIX base AI capabilities make enterprise architecture data more accessible and actionable, offering natural language queries, AI-assisted text generation, contextual insights, and translation support.").
### Toolsets
The MCP server supports enabling or filtering specific groups of functionalities through the toolsets query parameter. This allows you to control which tools are available to the LLM for a given request. When no toolsets parameter is provided, all available tools are returned by default.
### Using Toolsets
Append the toolsets query parameter to your request URL, as shown in the example:

```
https://{SUBDOMAIN}.leanix.net/services/mcp-server/v1/mcp?toolsets=inventory
```



To use multiple toolsets, add them as a comma-separated list, as shown in the example:

```
https://{SUBDOMAIN}.leanix.net/services/mcp-server/v1/mcp?toolsets=inventory,surveys
```



Any other data type for toolsets will result in the filtering logic returning an error.
### Available Toolsets
The toolsets listed below are predefined. You can't customize or extend them. However, you can combine multiple toolsets in a single request.
A tool is included in the response if it has at least one tag that matches one of the requested toolsets. If you provide an invalid or misspelled toolset name, the system returns an error.
Available Toolsets Toolset | Description
---|---
inventory | Get fact sheet information.
report_diagrams | Get report information.
roadmap_planning | Get initiatives and transformation information.
surveys | Create or get survey information.
architecture_decisions | Create or get architecture decision information.
self_built_software | Create or get self-built software discovery information. For more details, see [Using the MCP Server for Tech Stack Management](https://help.sap.com/docs/leanix/ea/using-mcp-server-for-tech-stack-management?locale=en-US&state=PRODUCTION&version=CLOUD "Manage tech stack data programmatically through the MCP server.").


### Limitations
  * You can list up to 10 toolsets in a single query. Exceeding this limit will result in a TooManyToolsetsError error.
  * Each toolset name must not exceed 50 characters. Longer names will trigger a ToolsetTooLongError error.
