##  Teams
In the teams section within the manifest file, you can define the teams that own the microservice. Team is a subtype of organization fact sheets. For additional information about subtypes, see [Organizations Fact Sheet Subtypes](https://help.sap.com/docs/leanix/ea/organization-modeling-guidelines?locale=en-US&state=PRODUCTION&version=CLOUD "Learn how to model organizations. This includes best practices and applicable use cases, and common antipatterns.").
Attribute | Required | Description
---|---|---
factSheetId | Required if name is not provided | The IDs of team fact sheets, showing the owning teams.
name | Required if factSheetId is not provided | The names of team fact sheets, corresponding to the full names.
externalId | Required if factSheetId and name are not provided | The externalId of team fact sheets.


**Note**
If you provide the factSheetId, name, and externalId attributes, the system prioritizes them in this order: factSheetId first, followed by externalId, and then name.
