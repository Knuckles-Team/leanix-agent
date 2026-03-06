##  Reviewing Upload Status and Error Handling
Once the upload is complete, in the Excel Import & Export tab of the transformations administration, you can check the status of the upload under the Status column. It can be one of the following:
  * Imported: The import was successful without errors.
  * Imported with errors: The import was completed except for a few rows, which had some errors.
  * Error: The import has failed.
  * ![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loiob764d24eabac4fdd986a0bde9fa44f9a_LowRes.png)
Checking Upload Status
To download and review the detailed status of the upload, hover over the import log list and click on Summary Report. In the downloaded summary report, the 000-Errors sheet summarizes all the errors in one place. It also allows you to navigate to specific worksheets where you need to make the corrections. In each worksheet, the Result column at the beginning shows the details of the upload status for each row.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loiob194ad0b5fb8475f9ccfc00ce25c4f64_LowRes.png)
Reviewing Errors in the Result Column
**Tip**
You can upload the summary report file itself after making corrections.
Apply filters to the Result column to isolate the rows with errors. Review the error description to understand the issue and correct the errors in the same file. Finally, upload the file for a successful import.


### Possible Errors
Errors can occur at different stages, as listed in the table below:
Error Type | Description | Possible Cause
---|---|---
File upload error | The selected file doesn't comply with the supported file type or size and cannot be opened. |
  * File format other than .xlsx
  * File with more than 10k rows


Parsing error (per worksheet) | A worksheet is not formatted according to the formatting rules and cannot be parsed. |  A worksheet is missing the required columns for a specific transformation type. This can happen if a configured transformation type was updated after the export. An error message will be shown at the top of the relevant column in the summary report. ![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio6d641a8d3df54589bf62fa6597d7cd38_LowRes.png)
Inline errors (per worksheet) | The file could be opened and parsed, but there are invalid entries at the row or cell level. |
  * Values of a worksheet do not follow general formatting rules
  * Referring to non-existent fact sheets
  * Mistakenly using translations instead of technical keys for single-select or multi-select values

You can find the cause of the error in the Result column of the summary report.


