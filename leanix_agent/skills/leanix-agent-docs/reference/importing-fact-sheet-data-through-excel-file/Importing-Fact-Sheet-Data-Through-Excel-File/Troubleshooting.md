##  Troubleshooting
Errors can occur at different stages, as listed in the table below:
Type |  Description |  Possible Errors
---|---|---
File upload error | The selected file doesn't comply with the supported file type or size and cannot be opened. | File format other than .xlsx Files with more than 10k rows
Parsing error | The file is not formatted according to the formatting rules and cannot be parsed. | The file is missing the required columns: fact sheet ID, fact sheet type, and name. The column title does not contain the right technical key and translations.
Inline errors | The file could be opened and parsed, but there are invalid entries at the row or cell level. | Values do not follow general formatting rules Referring to non-existent fact sheets and relations Mistakenly using translations instead of technical keys for single-select or multi-select values
Post confirmation errors | In very rare cases, errors can occur after the Import button is clicked. The error message will tell you the cause of the error. | Invalid entries in subscription role columns


**Tip**
Requesting Support: If you cannot resolve the error yourself, contact support using the support functionality on the screen. Alternatively, you can reach out through this link: [SAP LeanIX Support![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fwww.leanix.net%2Fsupport "https://www.leanix.net/support"). If you're an SAP customer, submit a request from the [SAP for Me![Information published on SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/sap_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fme.sap.com%2F "https://me.sap.com/") portal.
Make the necessary changes in the import file, then upload it again after resolving the errors. Click Import to finish the process.
