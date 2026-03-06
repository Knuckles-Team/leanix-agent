##  Get a Fact Sheet Hierarchy by Root ID
Method | Path | Reference
---|---|---
GET | /factSheets/hierarchy/{rootId} | [Schema![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fapp.leanix.net%2Fopenapi-explorer%2F%23%2FfactSheets%2FgetFactSheetHierarchy "https://app.leanix.net/openapi-explorer/#/factSheets/getFactSheetHierarchy")


You can retrieve all fact sheets equal to or below a specific root fact sheet.
REST call:

```
https://{SUBDOMAIN}.leanix.net/services/pathfinder/v1/factSheets/hierarchy/{rootId}
```



GraphQL query:

```
query {
 allFactSheets(hierarchy: {mode: FULL_TREE} filter: {ids: ["{rootId}"]}) {
   edges {
     node {
       id
       displayName
     }
   }
 }
}
```



