##  Archive a Fact Sheet
Method | Path | Reference
---|---|---
DELETE | /factSheets/{id} | [Schema![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fapp.leanix.net%2Fopenapi-explorer%2F%23%2FfactSheets%2FarchiveFactSheet "https://app.leanix.net/openapi-explorer/#/factSheets/archiveFactSheet")


REST call:

```
https://{SUBDOMAIN}.leanix.net/services/pathfinder/v1/factSheets/{id}
```



Example request body:

```
{
  "comment": "This is a test archive."
}
```



GraphQL mutation:

```
mutation {
 updateFactSheet(id: "{id}",
   comment: "This is a test archive.",
   patches: [{op: add, path: "/status", value: "ARCHIVED"}]) {
     factSheet {
       id
       name
       type
       description
       status
     }
 }
}
```



