##  Get a Fact Sheet by ID
Method | Path | Reference
---|---|---
GET | /factSheets/{id} | [Schema![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fapp.leanix.net%2Fopenapi-explorer%2F%23%2FfactSheets%2FgetFactSheet "https://app.leanix.net/openapi-explorer/#/factSheets/getFactSheet")


REST call:

```
https://{SUBDOMAIN}.leanix.net/services/pathfinder/v1/factSheets/{id}
```



GraphQL query:

```
query {
 factSheet(id: "{id}") {
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
   comments(filter: {status: ACTIVE}) {
     totalCount
     edges {
       node {
         message
       }
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
 }
}
```



To limit the results to only the id and name fields of a fact sheet, use the following query:

```
query {
 factSheet(id:"{id}") {
   id
   name
 }
}
```



