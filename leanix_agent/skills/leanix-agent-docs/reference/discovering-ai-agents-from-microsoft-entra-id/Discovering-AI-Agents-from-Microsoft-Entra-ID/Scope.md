##  Scope
  * The integration uses service principals instead of the application endpoint. This enables discovery of agents across different tenants.
  * SAP LeanIX relies on the agent ID to identify AI agents.
Discovered agents are listed under Enterprise apps and can be filtered using the tags field. Specifically, tags that start with power-virtual-agents or are equal to either AgenticInstance or AgenticApp.
  * The SAP LeanIX integration supports two regions: Global and China. API calls are routed to different URLs depending on the region. To learn how to handle region-specific URIs, consult [Authentication for National Clouds](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fentra%2Fidentity-platform%2Fauthentication-national-cloud "https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fentra%2Fidentity-platform%2Fauthentication-national-cloud").
