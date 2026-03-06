##  Limitations
The import feature has the following limitations:
Limitation | Detail
---|---
File type | Only .xlsx files are supported.
File size | Import files can contain up to 10,000 rows.
Limitations while importing subscriptions and relations | Including subscriptions or multiple relations per fact sheet can significantly increase processing time. To mitigate this, it is recommended to import fewer than 500 fact sheets per file when relations or subscriptions are included in the file. We also recommend not to import subscriptions and relations in the same file.
Unsupported data | The following data can not be imported: - Milestones - Comments - Resources - To-Dos
Fact sheet type per import | Only one fact sheet type can be imported per import. Including multiple fact sheet types in a single import file will lead to errors.
Existence of attributes is a prerequisite | Fact sheet attributes must already exist before the values can be successfully added or modified through the import process. New attributes cannot be created by merely adding a column in the spreadsheet. However, tags are an exception to this rule and can be created directly through Excel file import, provided on-the-fly creation is enabled for tags.


The rest of this guide walks you through the process of importing data, covering best practices, formatting rules, and common issues that might cause import errors while also offering solutions for addressing those issues.
