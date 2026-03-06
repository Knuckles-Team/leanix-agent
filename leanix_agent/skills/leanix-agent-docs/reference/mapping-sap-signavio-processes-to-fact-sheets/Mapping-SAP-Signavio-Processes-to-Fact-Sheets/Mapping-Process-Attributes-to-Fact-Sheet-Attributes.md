##  Mapping Process Attributes to Fact Sheet Attributes
You map the process attributes to fact sheet attributes using field mapping settings. In the Actions column, click the field mapping icon next to the delete button to open the field mapping modal.
![Click the Field Mapping Icon to Open the Settings](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274770467a4410149d11c2878ad5f6eb_LowRes.png)
Click the Field Mapping Icon to Open the Settings
Based on best practice data from SAP LeanIX, field mapping suggestions are given at the top. You can simply select a suggestion to add it to your list of field mappings. Additionally, you can manually define mappings by clicking Add and choosing fact sheet attributes and corresponding SAP Signavio process attributes from the respective drop-down lists.
![Field Mapping Settings](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27490f607a441014bd71c21e3dcf7bd8_LowRes.png)
Field Mapping Settings
The list of attributes in the drop-down list depends on the selected mapping type. The following mapping types are available:
  * Simple: allows you to choose from a list of process attributes from SAP Signavio and map them to target fields in SAP LeanIX fact sheets. For SAP LeanIX fact sheets, the available attributes include:
    * Scalar fields (e.g., text, number)
    * Single-select fields
    * Multi-select fields
    * Date fields
    * Subscriptions and subscription roles
    * Tags and tag groups
For SAP Signavio processes, you can select from:
    * Fields on dictionary items
    * Scalar fields (e.g., text, number, date)
    * Single-select and multi-select fields
  * Static Text: lets you enter a static text into a text field in the SAP LeanIX fact sheet
  * Expression: lets you use technical expressions to reference a field in SAP Signavio and map it to a corresponding field in SAP LeanIX


**Note**
The integration supports the synchronization of the diagram-level attributes. The synchronization of shape-level attributes is not supported.
