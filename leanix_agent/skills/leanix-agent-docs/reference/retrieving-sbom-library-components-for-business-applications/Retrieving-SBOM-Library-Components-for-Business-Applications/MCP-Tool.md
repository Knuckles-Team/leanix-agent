##  MCP Tool
The /applications/{factSheetId}/components endpoint is also available as an MCP tool, enabling AI agents to retrieve component data directly through the MCP protocol. To learn how to get started with the MCP server, see [MCP Server](https://help.sap.com/docs/leanix/ea/mcp-server?locale=en-US&state=PRODUCTION&version=CLOUD "Connect external AI applications to SAP LeanIX using the Model Context Protocol \(MCP\) server to securely access enterprise architecture data.").
Tool name: get_application_components
Input Parameters Parameter | Type | Required | Description
---|---|---|---
factSheetId | String | Yes | The unique identifier of the business application fact sheet.
cursor | String | No | Pagination cursor for retrieving the next page of results.
limit | Integer | No | Number of components to return per page. Valid values: 1 to 100. Default: 50.


The MCP tool returns the same component and license data as the REST endpoint.
