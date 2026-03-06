##  Updating the Data in the Spreadsheet
You can add, remove, or update the contents of the Excel file. Once you import the file, changes made in the file are reflected in the workspace. Follow the formatting rules given in this guide to avoid import errors.
In the Excel file, the 000-Readme sheet provides an overview of transformation types and the number of transformation items of each type, and formatting rules.
Each sheet corresponds to a transformation type (based on the transformation template), the rows represent individual transformation items, and the columns represent the fields of the transformation template.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio07e34e1ca22d4e21a9083bcc5b513dbd_LowRes.png)
Exported Excel File
Desired Outcome | Action
---|---
Update transformation values | Change the values of a row
Create a new transformation | Add a new row without filling the ID column
Move the transformation to a different initiative |  Change the name of the fact sheet under the Fact Sheet column to a different fact sheet.  However, if a milestone is used for the completion date of a transformation, the transformation can only be moved between parent and child fact sheets, as milestones can only be cross-referenced within the same parent-child hierarchy. To learn more, see [Lifecycle and Cross-Project Referencing of Milestones](https://help.sap.com/docs/leanix/ea/milestones?locale=en-US&state=PRODUCTION&version=CLOUD#loio275e267f7a441014bcb8ac6ea7daa952__lifecycle_and_cross-project_referencing_of_milestones)
Delete transformation | In the Action column, select Delete from the drop-down option.


### Formating Rules
Rule | Details
---|---
Character encoding | Supports UTF-8 character encoding.
Date format | Enter dates as: yyyy-mm-dd
Number format |  Use points (“.”) for decimals (Example: 1.7 = one point seven). Use no delimiters for thousands (Example: 27351).
Case sensitivity | Values are case-sensitive, so ensure the correct case.
< (less than) ; (semicolon)  | Values can not contain the character < (less than) or the list separator ; (semicolon) as part of them.
List  |  Separate different values with a ; (semicolon). Do not add space before or after the semicolon. For example: Corporate Services;HR;Recruiting;Finance
Single-select and multi-select fields |  Ensure you enter the exact technical keys of the values for a successful import.  Technical keys of the values can be found in the fact sheet configuration. To learn more, see [Configuring Fields](https://help.sap.com/docs/leanix/ea/fact-sheet-fields?locale=en-US&state=PRODUCTION&version=CLOUD#loio2759fb817a44101492ded5b080b9f10c__configuring_fields). Since multi-select fields are lists, make sure the values are separated with a ; (semicolon). Do not add space before or after the semicolon.
Fact sheet naming convention |  The display name of a fact sheet consists of the full names of the parent fact sheets, separated by a / (forward slash), followed by the full name of the child fact sheet. Make sure to **include spaces** before and after the slash. For details, see [Fact Sheet Naming Convention](https://help.sap.com/docs/leanix/ea/creating-fact-sheets?locale=en-US&state=PRODUCTION&version=CLOUD#loio2759925e7a441014a7e9e6f502b4cd21__fact_sheet_naming_convention) If you need to use a / (forward slash)in the name of a fact sheet itself, you can use the /without a space before
Milestone naming convention |  The display name of a milestone consists of the display name of the fact sheet, separated by a / (forward slash), followed by the name of the milestone. Make sure to **include spaces** before and after the slash. However, note that milestones can be cross-referenced only within the same parent-child hierarchy.
Completion date |  To update the completion date, first enter the keywords exactDate or milestone in the Completion date Type column.  Then, fill in the corresponding cell in either the Completion date column or the Milestone column. ![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio080743dd361346468d1dea72722f1b93_LowRes.png)
Predecessor handling |  For transformation types ‘Introduce new Application’ and 'Introduce new Interface you can specify predecessor handling in the Predecessor Handling column using one of the following values:
  * no handling
  * decommission
  * dicontinue

Decommissioning sets the lifecycle to phase out at the completion date. Discontinue sets the lifecycle to end-of-life at the completion date


### Overwrite Principle
In general, the import feature follows the overwrite principle, meaning existing data is always replaced with the data provided in the import file. Hence, for fields with multiple values, such as multi-select fields or fact sheets, make sure you include both existing and new values in the import file to keep the existing data while updating or adding new data.
