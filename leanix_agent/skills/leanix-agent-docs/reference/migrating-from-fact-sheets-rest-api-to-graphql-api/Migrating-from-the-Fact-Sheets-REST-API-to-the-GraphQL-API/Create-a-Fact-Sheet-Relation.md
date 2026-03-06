##  Create a Fact Sheet Relation
Method | Path | Reference
---|---|---
POST | /factSheets/{id}/relations | [Schema![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fapp.leanix.net%2Fopenapi-explorer%2F%23%2FfactSheets%2FcreateFactSheetRelation "https://app.leanix.net/openapi-explorer/#/factSheets/createFactSheetRelation")


REST call:

```
https://{SUBDOMAIN}.leanix.net/services/pathfinder/v1/factSheets/{id}/relations
```



Example request body:

```
{
  "displayNameToFS": "TestRelation",
  "typeFromFS": "relToPredecessor",
  "typeToFS": "relToSuccessor",
  "activeFrom": "2023-11-29",
  "activeUntil": "2024-11-29",
  "constrainingRelations": [],
  "idsOfConstrainingRelations": [],
  "status": "ACTIVE",
  "fromId": "{id}",
  "toId": "{targetId}"
}
```



GraphQL mutation:

```
mutation {
 updateFactSheet(id: "{id}", patches: [
   {
   op: add,
   path: "/relToSuccessor/new_{id}",
   value: "{\"factSheetId\":\"{targetId}\",\"activeFrom\":\"2023-11-29\",\"activeUntil\":\"2024-11-29\"}"
       }
 ]) {
   factSheet {
     id
     name
     type
   }
 }
}
```



