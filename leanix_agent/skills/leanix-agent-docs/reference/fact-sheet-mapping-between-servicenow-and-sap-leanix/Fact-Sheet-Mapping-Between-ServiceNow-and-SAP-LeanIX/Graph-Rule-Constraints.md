##  Graph Rule Constraints
A Graph Rule Constraint controls whether a record is synchronized at all based on a connection found on the ServiceNow side. Depending on the ServiceNow table used in a mapping from ServiceNow to SAP LeanIX, different or no Graph Rule Constraint might be applicable.
The configuration dialog for Sync Constraints is opened when ServiceNow is the Source, the configured ServiceNow Table supports the Graph Rules, and the 'Constraints' button is pressed.
![Adding a Graph Rule Constraint](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2745e39d7a441014bd24f21d4c1eced3_LowRes.png)
Adding a Graph Rule Constraint
Various types of Graph Rules are explained as follows -
Graph Rule | Definition | Required Active Mapping and Plugin
---|---|---
APPLICATION_SAM_CONNECTION or APPLICATION_SAM_PRO_CONNECTION | Synchronize this Software Product Model or Hardware Product Model, if a connection to an Application mapped table exists that can be found via the SAM module. Further filtering can be done while using this Graph Constraint. For more information, see [Graph Rule Constraints](https://help.sap.com/docs/leanix/ea/fact-sheet-mapping-between-servicenow-and-sap-leanix?locale=en-US&state=PRODUCTION&version=CLOUD#loio275ca5f57a4410149871ec89426715ea__graph_rule_constraints). |
  * for APPLICATION_SAM_CONNECTION: SAM + Discovery Service
  * for APPLICATION_SAM_PRO_CONNECTION: SAM PRO + Discovery Service
  * IT Component - Software/Hardware
    * cmdb_software_product_modelor
    * cmdb_hardware_product_model


IN_USE_SAM_CONNECTION or IN_USE_SAM_PRO_CONNECTION | Synchronize this Software Product Model or Hardware Product Model, if a connection to Hardware exists that can be found via the SAM module. |
  * for APPLICATION_SAM_CONNECTION: SAM + Discovery Service
  * for APPLICATION_SAM_PRO_CONNECTION: SAM PRO + Discovery Service
  * IT Component - Software/Hardware
    * cmdb_software_product_modelor
    * cmdb_hardware_product_model


MODEL_CATEGORY | Synchronize this Product Model, if a connection to a Model Category exists in SN. |
  * IT Component - Software - cmdb_software_product_model
  * Technical Categories - cmdb_model_category


APPLICATION_HARDWARE_CONNECTION | Synchronize this Hardware Product Model, if a connection to a Business Application exists. Tip - Check the Additional Information tab for further filter options on this Graph Constraint. |
  * IT Component - Hardware - cmdb_hardware_product_model
  * Application - cmdb_ci_business_app


IN_USE_HARDWARE_CONNECTION | Synchronize this Hardware Product Model, if a connection to a Hardware exists. |
  * IT Component - Hardware - cmdb_hardware_product_model


APPLICATION_SOFTWARE_MANAGEMENT_MODEL_CONNECTION | Synchronize this Software Product Model, if a connection to a Business Application exists that can be found via the Software Management module. |  Only supported when legacy configuration is in use, see [Legacy Configuration](https://help.sap.com/docs/leanix/ea/servicenow-integration?locale=en-US&state=PRODUCTION&version=CLOUD#loio275cad557a441014a42ef5e0f9d2887f__legacy_configuration)
  * IT Component - Software - cmdb_software_product_model
  * Application - cmdb_ci_business_app


IN_USE_SOFTWARE_MANAGEMENT_MODEL_CONNECTION | Synchronize this Software Product Model, if a connection to a Hardware exists that can be found via the Software Management module. |  Only supported when legacy configuration is in use, see [Legacy Configuration](https://help.sap.com/docs/leanix/ea/servicenow-integration?locale=en-US&state=PRODUCTION&version=CLOUD#loio275cad557a441014a42ef5e0f9d2887f__legacy_configuration)
  * IT Component - Software - cmdb_software_product_model




The relations between applications and IT components are discovered in ServiceNow using Graph Rule Constraints. This information is abstracted by the integration, and only the abstracted information is pulled into SAP LeanIX. Then the relations between applications and IT components can be fetched using the GRAPH_RULE_CONSTRAINT relation. For more information, see [GRAPH_RULE_CONSTRAINT](https://help.sap.com/docs/leanix/ea/relation-mapping-between-servicenow-and-sap-leanix?locale=en-US&state=PRODUCTION&version=CLOUD#loio275ca9ca7a4410148b008ed7c66f1cfe__graph_rule_constraint).
