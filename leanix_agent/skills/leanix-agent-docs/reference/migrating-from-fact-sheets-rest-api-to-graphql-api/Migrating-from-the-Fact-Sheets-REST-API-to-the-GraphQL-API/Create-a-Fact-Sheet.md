##  Create a Fact Sheet
Method | Path | Reference
---|---|---
POST | /factSheets | [Schema![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fapp.leanix.net%2Fopenapi-explorer%2F%23%2FfactSheets%2FcreateFactSheet "https://app.leanix.net/openapi-explorer/#/factSheets/createFactSheet")


REST call:

```
https://{SUBDOMAIN}.leanix.net/services/pathfinder/v1/factSheets
```



Example request body:

```
{
  "name": "TestFactSheet",
  "description": "This is a demo fact sheet.",
  "type": "Application"
}
```



GraphQL mutation:

```
mutation {
 createFactSheet(input: {
   name: "TestFactSheet"
   type: Application
 }
 patches: [
   {
     op: add
     path: "/description"
     value: "This is a demo fact sheet."
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
To update the description field, use a Patch operation.
