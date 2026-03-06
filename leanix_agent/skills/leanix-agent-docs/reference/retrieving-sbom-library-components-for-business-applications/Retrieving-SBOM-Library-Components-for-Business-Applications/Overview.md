##  Overview
Use the /applications/{factSheetId}/components endpoint in the [Self-Built Software Discovery API![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fapp.leanix.net%2Fopenapi-explorer%2F%23%2FSBOM%2FgetComponentsByApplication "https://app.leanix.net/openapi-explorer/#/SBOM/getComponentsByApplication") to retrieve all discovered SBOM library components for a specific business application. You can access this endpoint through the REST API or the MCP server.
With this endpoint, you can:
  * Retrieve library components by application fact sheet ID
  * Access package details, including package URL (PURL), name, version, package manager, namespace, and licenses
  * Paginate through large component lists using cursor-based pagination
  * Integrate with AI agents through MCP for automated workflows
