##  Working with Discovered Flows
Once discovered flows appear in your SAP discovery inbox, follow these steps:
  1. Choose a discovered flow item to see full details.
For example, “SF OnBoarding EMEA Prod to SF HCM EMEA Prod”.
![LeanIX interface showing discovered SAP flows and detailed information for a selected flow.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio9fd3983e7c0746dbb544d377cd6fd545_LowRes.png)
  2. To decide whether to model this as a point-to-point interface, part of a hub-and-spoke model, or to filter it out, review the integration type and involved systems.
For example, “IDOC_MESSAGES”.
  3. Create a new interface fact sheet from the discovered flow, or link the discovered flow to an existing interface fact sheet.
  4. After linking the discovered flow, complete these tasks:
     * Give the interface a meaningful, business-relevant name.
     * Set properties such as direction, type, and protocol.
     * Maintain relations to applications and IT components.
     * Use visualization to understand dependencies and impact.


A flow may not appear if the integration can't resolve referenced systems through internal Cloud ALM APIs or can't map systems to supported types (such as application or IT component).
