##  Step 1: Prepare Data
The Integration API supports the LDIF format for processing data. To import data, you should first convert it into this format. In this tutorial, we convert a CSV file into LDIF format using a Python script.
Prepare a CSV file with links that you want to import to application fact sheets. The file should contain the following columns:
  * type: The type of the fact sheet. In this tutorial, we only import application fact sheets.
  * id: The ID of the fact sheet.
  * name: The name of the link to be added to the fact sheet as a resource.
  * url: The link URL to be added to the fact sheet as a resource.


You can retrieve application fact sheets and their IDs in the following ways:
  * By using the GraphQL API. For more information, see [Filtering Fact Sheets by Type](https://help.sap.com/docs/leanix/ea/filtering-fact-sheets?locale=en-US&state=PRODUCTION&version=CLOUD#loio275a2b637a441014adeab270bff0d72e__filtering_fact_sheets_by_type).
  * By exporting data in XLSX format in the application UI. To learn more, see [Export Your Data via Excel](https://help.sap.com/docs/leanix/ea/exporting-fact-sheet-data-as-excel-file?locale=en-US&state=PRODUCTION&version=CLOUD "SAP LeanIX’s export feature allows you to export fact sheet data as an Excel file for bulk updates, easy data manipulation, and offline analysis. The exported file also serves as a template for importing data back into SAP LeanIX."). Once you've downloaded the file, convert it into CSV format.


Here's an example CSV file with the required columns.
type | id | name | url
---|---|---|---
Application |  28fe4aa2-6e46-41a1-....-72afb3acf256 | Technical documentation |  https://docs.example.net/
Application |  2efa37b5-18aa-48d8-....-1328c0d856d7 | Vendor's website |  https://www.example-vendor.net/


**Note**
You can import multiple links to a single fact sheet.
