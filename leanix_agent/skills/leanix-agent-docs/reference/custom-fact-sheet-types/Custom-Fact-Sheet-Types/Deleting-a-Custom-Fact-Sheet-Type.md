##  Deleting a Custom Fact Sheet Type
If a custom fact sheet type no longer meets your organization’s modeling requirements, you can delete it. Before proceeding, ensure that you have a comprehensive understanding of the potential impacts. Do the following:
  * Identify dependencies: Check if there are any dependencies on this fact sheet type. This could include other fact sheets, reports, or workflows that rely on the information contained in this fact sheet type.
  * Create a backup: Before deletion, make sure to create a backup of your inventory data by exporting it. This will allow you to restore the fact sheet type if you realize later that it was needed. You can export inventory data to an Excel file. For more information, see [Exporting Fact Sheet Data as Excel File](https://help.sap.com/docs/leanix/ea/exporting-fact-sheet-data-as-excel-file?locale=en-US&state=PRODUCTION&version=CLOUD "SAP LeanIX’s export feature allows you to export fact sheet data as an Excel file for bulk updates, easy data manipulation, and offline analysis. The exported file also serves as a template for importing data back into SAP LeanIX.").
  * Plan for data migration: If the data from the fact sheet type will need to be retained, plan how and where this data will be migrated. This could involve creating a new fact sheet type or modifying an existing one to accommodate the data.
  * Communicate with stakeholders: Inform relevant stakeholders about your plans to delete the fact sheet type. This could include teams or individuals who regularly use or rely on the fact sheet type.


**Caution**
Deleting a custom fact sheet type is irreversible. All fact sheets of this type and related data will be permanently deleted. Always proceed with caution and ensure that you've fully assessed the potential impacts before proceeding.
To delete a custom fact sheet type, follow these steps:
  1. In the administration area, navigate to the Meta Model Configuration section.
  2. Hover over the fact sheet type that you want to delete, then click the trash bin icon that appears on the right side.
  3. In the dialog that appears, review the data that will be deleted, then confirm your action and click Delete.


When a fact sheet type is deleted, the following occurs:
  * All fact sheets of this type and their relations are deleted.
  * Reports specific to this fact sheet type are deleted.


**Tip**
To prevent any potential disruptions or negative experiences for workspace users, consider making significant changes to the meta model configuration, such as deleting custom fact sheet types, outside of regular business hours.
