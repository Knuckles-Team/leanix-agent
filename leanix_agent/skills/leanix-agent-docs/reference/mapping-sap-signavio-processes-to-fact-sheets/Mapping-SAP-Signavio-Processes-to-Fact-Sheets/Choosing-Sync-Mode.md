##  Choosing Sync Mode
Sync mode in process mapping determines how process data is created, updated, and deleted in SAP LeanIX. It helps prevent unwanted data loss and manage duplicates. You have the following options:
Additive Sync | Conservative Sync | Overwrite Sync
---|---|---
Fact sheets are only created or updated based on changes in SAP Signavio. Fact sheets are never archived, even when processes are deleted. It's the safest option, but it can lead to duplicate data if not managed carefully. | Fact sheets are created, updated, or archived based on changes in SAP Signavio. Only the current integration’s mappings are considered, and fact sheets created by other instances of the Signavio integration, or different integrations such as Collibra or those created manually, are not affected and will remain intact. | Fact sheets are created, updated, or archived based on changes in SAP Signavio. All fact sheets not associated with the current integration, including manually created ones, are deleted. Choose this mode only when you want SAP Signavio to be the sole source of truth for the processes. Otherwise, you risk unintended data deletion.


**Note**
External ID
All linked fact sheets store the unique ID of the SAP Signavio processes in an external ID field called Signavio Process. This allows for the differentiation of fact sheets related to the current integration from those associated with other integrations and manually created entries.
**Note**
To prevent accidental deletion of fact sheets from other instances of the Signavio integration, the overwrite sync mode is automatically disabled when integrations are set up for multiple SAP Signavio tenants.
