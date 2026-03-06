##  Core Concepts
For synchronization purposes, every mapping between tables in both systems defines the following:
![FS Type / ServiceNow Table Mapping](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27501bf57a4410148a16c406a936bfdc_LowRes.png)
Mapping Between Fact Sheet Types and ServiceNow Tables
Parameter | Description
---|---
Fact Sheet Type | SAP LeanIX Fact Sheet Type - e.g. Application, IT Component (Software), etc.
Direction/ Source | Defined Direction and Source of Truth - e.g. SAP LeanIX or ServiceNow
ServiceNow Table | Name of the table in ServiceNow with its logical table name. For example Business Application - cmdb_ci_business_app
Sync Mode | Defines how to deal with objects on the target that have no corresponding one the source system. See [Sync Mode](https://help.sap.com/docs/leanix/ea/servicenow-integration?locale=en-US&state=PRODUCTION&version=CLOUD#loio275cad557a441014a42ef5e0f9d2887f__sync_mode)
Filter/ Constraints | Whether there are any synchronization constraints, e.g. only synchronizing applications with a specific lifecycle status or only synchronizing software product models which are installed on a server belonging to a managed business application


Within each mapping type described above, it is possible to configure the field-level mapping between the two systems.
![Field-level mapping keys between SAP LeanIX and ServiceNow](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27487a187a441014a3f69804902e1359_LowRes.png)
Field-level mapping keys between SAP LeanIX and ServiceNow
The following parameters are available for field mappings:
  * The type of field mapping (Further explained, in the setup in SAP LeanIX documentation).
  * The name of the field in SAP LeanIX (if applicable).
  * The direction of synchronization.
  * The name of the field in ServiceNow (if applicable).
  * Whether the attribute is to be synced from the defined source of truth or the opposite of the defined source.
  * How values are being mapped.


Both standard and custom attributes are supported by the integration. The integration synchronizes in-scope data from one system to another as specified in the configuration.
