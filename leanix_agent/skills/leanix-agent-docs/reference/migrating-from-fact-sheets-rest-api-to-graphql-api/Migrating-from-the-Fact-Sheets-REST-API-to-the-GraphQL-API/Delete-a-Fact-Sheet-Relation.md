##  Delete a Fact Sheet Relation
Method | Path | Reference
---|---|---
DELETE | /factSheets/{id}/relations/{relationId} | [Schema![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fapp.leanix.net%2Fopenapi-explorer%2F%23%2FfactSheets%2FdeleteFactSheetRelation "https://app.leanix.net/openapi-explorer/#/factSheets/deleteFactSheetRelation")


REST call:

```
https://{SUBDOMAIN}.leanix.net/services/pathfinder/v1/factSheets/{id}/relations/{relationId}
```



GraphQL mutation:

```
mutation {
 updateFactSheet(id: "{id}", patches: [
   {
   op: remove,
   path: "/relToSuccessor/{relationId}",
   value: ""
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
In the example request, we delete a relation for a fact sheet of the Application type.
