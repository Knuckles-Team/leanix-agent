##  Creating Synchronization Mappings
**Note**
You can only map text fields from your fact sheets. These correspond with the SAP LeanIX field type "string," including fields like name, description, or alias. Read more about field types in the article [Fact Sheet Fields](https://help.sap.com/docs/leanix/ea/fact-sheet-fields?locale=en-US&state=PRODUCTION&version=CLOUD "Fact sheet fields are designed for storing information on specific data points. You can configure existing fields and create custom ones.").
Synchronization mappings allow you to synchronize Jira with your SAP LeanIX meta model. You can sync each fact sheet type with one Jira issue type. However, a single Jira issue type can be synced with multiple fact sheet types.
To create a synchronization mapping, follow these steps:
  1. In the top navigation bar in Jira, go to Apps > SAP LeanIX Synchronization Mappings.
  2. Choose Add project.
  3. Search the name of the project you want to sync and select it.
  4. Choose Add to sync a new fact sheet type and issue type.
    1. Select the fact sheet type (for example, project) and the issue type (for example, epic).
    2. Choose Add Field Mapping.
    3. Select the SAP LeanIX text field (for example, name).
    4. Select the direction (for example, bidirectional).
    5. Select the Jira issue type (for example, summary).
  5. Repeat these steps for all text fields that you want to sync and choose Add. The synchronized fact sheet type will appear in the synchronization mappings list.


To display the details of a synchronization mapping, choose the expand arrow.
**Tip**
To delete a synchronization mapping, choose Delete. This removes all synced fact sheets from the corresponding Jira issues. This can’t be undone.
**Note**
Only Jira admins can create synchronization mappings.
