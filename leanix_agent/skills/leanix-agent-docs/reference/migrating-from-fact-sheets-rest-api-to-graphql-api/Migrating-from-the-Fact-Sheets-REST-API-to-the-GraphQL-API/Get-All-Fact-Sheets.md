##  Get All Fact Sheets
Method | Path | Reference
---|---|---
GET | /factSheets | [Schema![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fapp.leanix.net%2Fopenapi-explorer%2F%23%2FfactSheets%2FgetFactSheets "https://app.leanix.net/openapi-explorer/#/factSheets/getFactSheets")


In this section, we provide an example of retrieving all fact sheets of the Application type and its relations to fact sheets of the ITComponent type.
REST call:

```
https://{SUBDOMAIN}.leanix.net/services/pathfinder/v1/factSheets?relationTypes=relApplicationToITComponent&type=Application
```



GraphQL query:

```
query {
 allFactSheets(filter: {responseOptions: {maxFacetDepth: 5}, facetFilters: [
   {facetKey: "FactSheetTypes",
     keys:["Application"],
     operator: OR
   }
 ]}, sort: [{key: "displayName", order: asc}]) {
   totalCount
   edges {
     node {
       id
       displayName
       description
       rev
       type
       permissions {
         create
         read
         update
         delete
         self
       }
       qualitySeal
       lxState
       updatedAt
       completion {
         percentage
       }
       tags {
         id
         name
         description
         color
         tagGroup {
           id
           name
           shortName
           mode
         }
       }
       subscriptions(filter: {userId: "{userId}"}) {
         edges {
           node {
             id
             user {
               id
               firstName
               lastName
               email
             }
             type
             roles {
               id
               comment
             }
           }
         }
       }
       status
       level
       category
       ... on Application {
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
       }
     }
   }
 }
}
```



In the example request, we retrieve all fact sheets of the Application type, including their default fields, completion, tags, subscriptions, and more. For related fact sheets of the ITComponent type, we only fetch their id and name.
