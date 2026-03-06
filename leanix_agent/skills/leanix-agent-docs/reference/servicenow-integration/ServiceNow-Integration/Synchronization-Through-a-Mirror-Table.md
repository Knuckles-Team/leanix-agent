##  Synchronization Through a Mirror Table
Tables in ServiceNow may contain large volumes of data, which may potentially lead to long synchronization durations or interruptions during synchronization runs. To mitigate these challenges, we’ve implemented synchronization through a mirror table, which significantly enhances the efficiency of processing large volumes of data.
With a mirror table, the synchronization process works as follows:
  1. The target ServiceNow table is replicated into the SAP LeanIX database. This replicated table within SAP LeanIX serves as a mirror table.
  2. Data is synchronized from the mirror table in SAP LeanIX and not directly from the target table in ServiceNow. The integration system transfers and stores only the necessary data into the mirror table. This includes only the fields configured for fact sheet mapping or IDs relevant to mapping tables.


Synchronization through a mirror table is always activated for the aggregation and linkage feature and is applicable to ServiceNow tables that provide software records data (cmdb_sam_sw_install or cmdb_software_instance). To learn more about this feature, see [Aggregation and Linkage of Software Records](https://help.sap.com/docs/leanix/ea/aggregation-and-linkage-of-software-records?locale=en-US&state=PRODUCTION&version=CLOUD "The aggregation and linkage feature allows you to import multiple software records from ServiceNow in an aggregated way while automatically linking consolidated fact sheets to the reference catalog.").
When processing large tables, the system autonomously determines which table will be mapped. Frequently, a mirror table is created for cmdb_rel_ci, which provides data on relations. This approach streamlines the creation of relations between IT components and applications in SAP LeanIX, thereby preventing errors and minimizing processing time.
**Note**
For active ServiceNow configurations, we delete mirror tables that haven’t been used for the last 30 days. For configurations that are deactivated for more than 7 days, we delete all associated data from mirror tables. Deleting a mirror table removes all metadata for maintaining the mirror table, as well as all mirrored ServiceNow items.
The mirroring process is detailed in the synchronization log, in the Sync Logging section of the administration area. Here, you can view the mirroring status and progress, shown in percentage, for specific tables. Here’s an example message for a mirror table in synchronization logs:

```
Table 'cmdb_sam_sw_install' mirror is in sync with ServiceNow 'cmdb_sam_sw_install' table

```



