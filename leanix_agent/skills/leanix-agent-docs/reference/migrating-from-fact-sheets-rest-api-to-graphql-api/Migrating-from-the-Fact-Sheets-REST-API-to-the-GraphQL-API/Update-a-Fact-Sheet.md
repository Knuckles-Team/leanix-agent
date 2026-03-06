##  Update a Fact Sheet
Method | Path | Reference
---|---|---
PUT | /factSheets/{id} | [Schema![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fapp.leanix.net%2Fopenapi-explorer%2F%23%2FfactSheets%2FupdateFactSheet "https://app.leanix.net/openapi-explorer/#/factSheets/updateFactSheet")


In this section, we provide an example of updating the description of a fact sheet.
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
  "name": "TestFactSheet",
  "description": "This is the updated demo fact sheet description.",
  "displayName": "TestFactSheet",
  "fullName": "TestFactSheet"
}
```



GraphQL mutation:

```
mutation {
 updateFactSheet(id: "{id}"
 patches: [
   {
     op: replace
     path: "/description"
     value: "This is the updated description of a demo fact sheet."
   }
 ]) {
   factSheet {
     id
     name
     type
     description
   }
 }
}
```



Unlike the REST endpoint, the GraphQL mutation allows you to update data in a more granular way. You don't need to pass fields that you don't want to modify. In this example, we only update the description.
