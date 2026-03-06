##  Mapping Multiple Fact Sheet Types to One ServiceNow Table
You can map multiple fact sheet types to the same ServiceNow table in the following cases:
  * ServiceNow is the source of truth for mappings.
  * Filters are set to ensure that there is no overlap in data synchronization.


An example scenario might involve records in ServiceNow that are not yet fully distributed across the appropriate tables, and instead, reside within a single table, such as the cmdb_ci_appl table. In this case, you can link this table to both applications and IT components, making ServiceNow the source of truth. To ensure accurate data synchronization, you also need to set appropriate filters.
![`cmdb_ci_appl` table is linked to both Applications and IT Component Software with ServiceNow as the source of truth and appropriate Filters set.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274321487a44101497cbb492580f3062_LowRes.png)
Mapping Multiple Fact Sheet Types to One ServiceNow Table
