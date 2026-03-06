##  Mapping Lifecycle and Date Fields
This section provides an overview of the supported methods for syncing lifecycle and date fields between ServiceNow and SAP LeanIX. The following table details each scenario and the required configurations.
Case | Description | Source of Truth | Configuration
---|---|---|---
Case 1 | The current lifecycle phase is pushed from SAP LeanIX to a ServiceNow field. | SAP LeanIX | Use VALUE_MAPPING as the mapping type. In the LeanIX Field list, select the main field lifecycle, not one of the lifecycle phases (such as lifecycle/active or lifecycle/phaseIn). The synced value is not a Date but a String representing the current phase.
Case 2 | Lifecycle date values are pulled from ServiceNow to SAP LeanIX lifecycle phase fields. | ServiceNow | Map each Date field in ServiceNow to a lifecycle phase in SAP LeanIX, such as lifecycle/plan. The input date must be in the format yyyy-mm-dd (for example, 2014-01-01).
Case 3 | Lifecycle phase dates are pulled and pushed from SAP LeanIX to ServiceNow Date fields. | SAP LeanIX | Map each phase in SAP LeanIX, such as lifecycle/plan, to a Date field in ServiceNow.
Case 4 | String fields in SAP LeanIX pull date values from ServiceNow. | ServiceNow | In the fact sheet configuration in SAP LeanIX, create a field of type String which is displayed as Date. In field mappings, you can use the FOREIGN_FIELD mapping type. ![Custom Field Configuration in SAP LeanIX](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274276f77a441014a793bb605eb50388_LowRes.png)
Case 5 | String fields in SAP LeanIX push date values to ServiceNow. | SAP LeanIX | See configuration details for case 4.


