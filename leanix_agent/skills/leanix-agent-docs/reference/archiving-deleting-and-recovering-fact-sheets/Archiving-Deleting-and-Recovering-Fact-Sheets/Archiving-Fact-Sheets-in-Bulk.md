##  Archiving Fact Sheets in Bulk
You can archive multiple fact sheets in one go by exporting and importing fact sheets as Excel files. Following instructions tells you how to do it on a high level. For a detailed guide on importing and exporting fact sheets, see [Importing Fact Sheet Data Through Excel Files](https://help.sap.com/docs/leanix/ea/importing-fact-sheet-data-through-excel-file?locale=en-US&state=PRODUCTION&version=CLOUD "SAP LeanIX’s import feature enables efficient bulk updates, including adding, updating, and archiving fact sheets. This guide provides formatting rules, error handling, and step-by-step guidance for importing data through an Excel file.").
  1. In the inventory, list the fact sheets you want to export by applying the necessary filters.
  2. Switch to table view mode, and from the right side panel, select Export.
  3. In the exported Excel file, add a column with action as the technical key in the first row and Action as the translation in the second row.
  4. Populate the action column cells with 'archive' as the value for each fact sheet to be archived.
  5. Import the file, using the import action button in the right side panel of the inventory.


Each archived fact sheet will now automatically have a comment set to 'archived by Excel import.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2755461b7a441014bc9dd55e0bbace65_LowRes.png)
Archiving Fact Sheets in Bulk
