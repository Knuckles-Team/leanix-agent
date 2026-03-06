##  Synchronization Details
Here's how synchronization works within the scope of the aggregation and linkage feature:
  * Fact sheet type: Only software records can be imported from ServiceNow in an aggregated way. In SAP LeanIX, software is a subtype of IT component fact sheets. To learn more about this fact sheet type, see [IT Component Modeling Guidelines](https://help.sap.com/docs/leanix/ea/it-component-modeling-guidelines?locale=en-US&state=PRODUCTION&version=CLOUD "Learn how to model IT components. This includes best practices and applicable use cases, and common antipatterns.").
  * Synchronization direction: Data is sent from ServiceNow to SAP LeanIX.
  * ServiceNow tables: Data can be sourced from the following ServiceNow tables:
    * Software Discovery Model (cmdb_sam_sw_discovery_model) — applicable only if the SAM module is enabled in ServiceNow
    * Software package (cmdb_ci_spkg)
  * Synchronization modes: You can select the mode of synchronization, similar to standard fact sheet mappings. To learn more about available modes, see [Sync Mode](https://help.sap.com/docs/leanix/ea/servicenow-integration?locale=en-US&state=PRODUCTION&version=CLOUD#loio275cad557a441014a42ef5e0f9d2887f__sync_mode).
  * Import scope: By default, all software records detected on hardware are aggregated and imported from ServiceNow. You can set a constraint to only import software records detected on hardware attached to an application. This enables you to focus on software records that impact your applications.
