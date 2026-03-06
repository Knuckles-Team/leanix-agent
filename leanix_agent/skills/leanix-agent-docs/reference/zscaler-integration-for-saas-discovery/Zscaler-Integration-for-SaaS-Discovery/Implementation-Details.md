##  Implementation Details
SAP LeanIX uses Zscaler's ZIA API to discover SaaS application activity. The integration relies on the Shadow IT report, which provides detailed information on the applications being used across your corporate network and the extent of their usage. For usage adoption metrics, the total active unique users in Zscaler are calculated based on the user count of the past 7 days.
After setting up the integration, to cross-check the discovered services in the Zscaler Admin portal, hover over Analytics in the left-side pane and select Applications under the SaaS Security section.
Integration Categories | Authentication Mechanism | API Endpoints Used | Zscaler Resource
---|---|---|---
Cloud Access Security Brokers (CASB) | REST API - API token auth |  For API authentication: /api/v1/authenticatedSession For SaaS discovery:
  * /api/v1/cloudApplications/lite
  * /api/v1/shadowIT/applications/export

|  [Shadow IT Report![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fhelp.zscaler.com%2Fzia%2Fshadow-it-report-api%23%2FshadowIT%2Fapplications%2Fexport-post "https://help.zscaler.com/zia/shadow-it-report-api#/shadowIT/applications/export-post")


