##  Update a Fact Sheet Relation
Method | Path | Reference
---|---|---
PUT | /factSheets/{id}/relations/{relationId} | [Schema![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fapp.leanix.net%2Fopenapi-explorer%2F%23%2FfactSheets%2FupdateFactSheetRelation "https://app.leanix.net/openapi-explorer/#/factSheets/updateFactSheetRelation")


REST call:

```
https://{SUBDOMAIN}.leanix.net/services/pathfinder/v1/factSheets/{id}/relations/{relationId}
```



Example request body:

```
{
  "id": "{relationId}",
  "displayNameToFS": "TestApp",
  "typeFromFS": "Application",
  "typeToFS": "Application",
  "permittedReadACL": [],
  "activeFrom": "2023-11-29",
  "activeUntil": "2025-11-29",
  "constrainingRelations": [],
  "fields": [],
  "status": "ACTIVE",
  "fromId": "{id}",
  "toId": "{targetFactSheetId}",
  "naFields": [],
  "type": "relToSuccessor"
}
```



GraphQL mutation:

```
mutation updateRelation {
 updateFactSheet(id: "{id}", patches: [
   {
   op: replace,
   path: "/relToSuccessor/{relationId}",
   value: "{\"description\":\"This is a test description.\",\"factSheetId\":\"{targetFactSheetId}\",\"activeFrom\":\"2023-11-29\",\"activeUntil\":\"2026-11-29\"}"
}
 ]) {
   factSheet {
     id
     name
     type
     ... on Application {
       relToSuccessor {
         edges {
           node {
             id
             activeFrom
             activeUntil
             description
               factSheet {
               fullName
             }
           }
         }
       }
     }
   }
 }
}
```



In the example request, we update a relation for a fact sheet of the Application type.
