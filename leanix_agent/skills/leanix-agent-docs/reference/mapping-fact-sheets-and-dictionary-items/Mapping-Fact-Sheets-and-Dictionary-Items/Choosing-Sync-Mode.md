##  Choosing Sync Mode
Sync mode determines how data is created, updated, and deleted in the target system. It helps prevent unwanted data loss and manage duplicates. You have the following options:
Direction of Sync | Additive Sync | Conservative Sync | Overwrite Sync
---|---|---|---
SAP LeanIX → SAP Signavio | Dictionary items are only created and updated based on changes in SAP LeanIX. Dictionary items are never deleted, even when fact sheets are archived. It's the safest option, but it can lead to duplicate data if not managed carefully. | (Conservative Sync is not available when SAP LeanIX is the source.) | Dictionary items are created, updated, or deleted based on changes in SAP LeanIX. All dictionary items from a mapped dictionary category that is not associated with the current integration are deleted. Choose this mode only when you want SAP LeanIX to be the sole source of truth for a mapped dictionary category. Otherwise, you risk unintended data deletion.
SAP Signavio → SAP LeanIX | Fact sheets are only created and updated based on changes in SAP Signavio. Fact sheets are never archived, even when dictionary items are deleted. It's the safest option, but it can lead to duplicate data if not managed carefully. | Fact sheets are created, updated, or archived based on changes in SAP Signavio. Only the current integration’s mappings are considered, and changes to dictionary items not related to the current integration don’t affect anything. | Fact sheets are created, updated, or archived based on changes in SAP Signavio. All fact sheets not associated with the current integration, including manually created ones, are deleted. Choose this mode only when you want SAP Signavio to be the sole source of truth for a mapped fact sheet type. Otherwise, you risk unintended data deletion.


**Note**
External ID
All linked fact sheets store the unique ID of dictionary items in an external ID field called Signavio Glossary. This allows for the differentiation of fact sheets and dictionary items related to the current integration from those associated with other integrations or manually created entries.
**Tip**
  * To prevent accidental deletion of fact sheets from other instances of the Signavio integration, the overwrite sync mode is disabled when integrations are set up for multiple SAP Signavio tenants.
  * In overwrite sync mode, it is possible to limit the scope overwrite action to a specific subcategory within the dictionary items.
