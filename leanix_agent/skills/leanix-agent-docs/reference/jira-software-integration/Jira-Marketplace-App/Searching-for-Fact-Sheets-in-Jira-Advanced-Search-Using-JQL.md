##  Searching for Fact Sheets in Jira Advanced Search Using JQL
SAP LeanIX for Jira adds some properties to Jira issues that let you filter with JQL. You can use the following properties:
  * factSheetCount
  * linkedFactSheetCount
  * syncedFactSheetCount
  * syncFactSheetId
  * syncFactSheetType


You can use these properties in JQL queries to extract specific information about fact sheets and related Jira issues. Here are some examples:
Query Purpose | JQL Statement
---|---
Identify the Jira issues in the “Rocket” project that are synchronized with fact sheets labeled as “Epic.” | project = "Rocket" AND syncFactSheetType = Epic
Identify Jira issues that have at least one fact sheet linked in the “Rocket” project. | project = "Rocket" AND linkedFactSheetCount > 0


