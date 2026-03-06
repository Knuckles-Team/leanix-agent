##  Get All Relations of a Fact Sheet
Method | Path | Reference
---|---|---
GET | /factSheets/{id}/relations | [Schema![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fapp.leanix.net%2Fopenapi-explorer%2F%23%2FfactSheets%2FgetFactSheetRelations "https://app.leanix.net/openapi-explorer/#/factSheets/getFactSheetRelations")


In this section, we retrieve all relations of a fact sheet with the specified {id}.
REST call:

```
https://{SUBDOMAIN}.leanix.net/services/pathfinder/v1/factSheets/{id}/relations
```



GraphQL query:

```
query {
 factSheet(id: "{id}") {
   ... on Application {
     relToChild {
       edges {
         node {
           factSheet {
             id
             name
           }
         }
       }
     }
     relApplicationToITComponent {
       edges {
         node {
           factSheet {
             id
             name
           }
         }
       }
     }
     relToSuccessor {
       edges {
         node {
           factSheet {
             id
             name
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
In the example request, we retrieve the following relations of a fact sheet: relToChild, relApplicationToITComponent, and relToSuccessor. For the target fact sheet, we only fetch the id and name fields.
While the REST endpoint provides all possible fields and data in a single call, GraphQL requires you to add all the required relations and fields of the target fact sheet to your query.
