##  Data Linking and Mapping
Should mapping be also done on the ServiceNow side?
You should configure mapping in SAP LeanIX. For more information, see [Fact Sheet Mapping Between ServiceNow and SAP LeanIX](https://help.sap.com/docs/leanix/ea/fact-sheet-mapping-between-servicenow-and-sap-leanix?locale=en-US&state=PRODUCTION&version=CLOUD "Configure mappings between specific fields in SAP LeanIX fact sheets and ServiceNow tables.").
How can I link a business process to an application to get an overview of data mastered in SAP LeanIX and ServiceNow? For example, can I view business processes that rely on end-of-life IT components?
The integration can read and model existing relations for an application in SAP LeanIX, so the link is created automatically. You can view this data in the following reports:
  * Application Landscape Report clustered by processes, using the Obsolescence Aggregated Risk view
  * Application Matrix Report with Processes on the Y axis, IT components in the drill-down, and the Obsolescence Aggregated Risk view selected


Do you recommend any best practices for managing specific attributes in ServiceNow and SAP LeanIX? Where can I view the data model and data mapping?
The default mapping available in the configuration is based on best practices. To view the data model and data mapping, see [Default Mapping](https://help.sap.com/docs/leanix/ea/servicenow-integration?locale=en-US&state=PRODUCTION&version=CLOUD#loio275cad557a441014a42ef5e0f9d2887f__default_mapping). You can also view the mapping matrix as an Excel file ([Download a copy of the Excel file![Information published on SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/sap_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fd.dam.sap.com%2Fa%2FR5iKkB9%3Frc%3D10%26doi%3DSAP1226473 "https://d.dam.sap.com/a/R5iKkB9?rc=10&doi=SAP1226473")), which includes best practices for mapping additional fields.
Does the integration also include the relationships ServiceNow may have in Service Mapping?
The relationships available in the cmdb_rel_ci table are used for automatic mapping of applications to IT components. Custom relationship mapping is supported from reference fields and custom tables, including the cmdb_rel_ci table.
