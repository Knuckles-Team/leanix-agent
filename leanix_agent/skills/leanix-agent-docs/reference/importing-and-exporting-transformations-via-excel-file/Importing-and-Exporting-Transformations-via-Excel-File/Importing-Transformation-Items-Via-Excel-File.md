##  Importing Transformation Items Via Excel File
Though anyone can update and edit the contents of the Excel file, only admins can import it. It ensures admins have the control to prevent accidental or unauthorized bulk changes.
### Limitations
The import feature has the following limitations:
**Limitation** | **Details**
---|---
File type | Only .xlsx files are supported.
File size | Import files can contain up to 10,000 rows.
Impacts of transformations | The changes you make in the Excel file change the impacts. However, you can not explicitly change the impacts of transformation in the Excel file, including custom impacts.
Tags | Tags can't be created, updated, or removed through transformation import.
Executing transformations |  Transformations cannot be executed through the transformation import.  The Status column is read-only.
Creating new fact sheets | You can only mention existing fact sheets and can not create new fact sheets through the import.


### Creating an Import Template
To import transformations via an Excel file, start by generating an Excel file through the export option. The exported file serves as a template for importing data, as it’s properly structured with separate sheets for each transformation type and includes all the required fields as columns. To learn how to export, see [Exporting Transformation Items Via Excel File](https://help.sap.com/docs/leanix/ea/importing-and-exporting-transformations-via-excel-file?locale=en-US&state=PRODUCTION&version=CLOUD#loio01ce04133887432fbdeb104e4b544a95__Exporting-Transformation-Items-Via-Excel-File)
