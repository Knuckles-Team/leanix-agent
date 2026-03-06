##  Fact Sheet Mapping Parameters
For each mapping, you can define the rules for syncing specific fields between SAP LeanIX fact sheets and ServiceNow tables.
![Fact Sheet Mapping](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2744d2c27a441014b9ab9190bd2b9bd3_LowRes.png)
Fact Sheet Mapping
The table below lists fact sheet mapping parameters.
Parameter | Description
---|---
Fact Sheet Type | The type or subtype of a fact sheet in SAP LeanIX, such as application, business capability, or tech category. This includes all fact sheets configured in your workspace's meta model, encompassing both standard and custom types and subtypes.
Direction / Source | The direction of data synchronization: from ServiceNow to SAP LeanIX or the other way around.
ServiceNow Table | The name of the table in ServiceNow with its logical table name, for example, Business Application - cmdb_ci_business_app.
Sync Mode | The mode of synchronization defining how to handle objects in the target system that have no corresponding items in the source system. For detailed information, see [Sync Mode](https://help.sap.com/docs/leanix/ea/servicenow-integration?locale=en-US&state=PRODUCTION&version=CLOUD#loio275cad557a441014a42ef5e0f9d2887f__sync_mode).
Filter (Constraints) | Optional filters that establish synchronization constraints. Examples include synchronizing applications with a particular lifecycle status or synchronizing only those software product models installed on a server tied to a managed business application. For detailed information, see [Synchronization Filters](https://help.sap.com/docs/leanix/ea/fact-sheet-mapping-between-servicenow-and-sap-leanix?locale=en-US&state=PRODUCTION&version=CLOUD#loio275ca5f57a4410149871ec89426715ea__synchronization_filters).
Field Mapping | The mappings between specific fields within SAP LeanIX fact sheets and ServiceNow tables. For detailed information, see [Configuring Field Mappings](https://help.sap.com/docs/leanix/ea/fact-sheet-mapping-between-servicenow-and-sap-leanix?locale=en-US&state=PRODUCTION&version=CLOUD#loio275ca5f57a4410149871ec89426715ea__configuring_field_mappings).


