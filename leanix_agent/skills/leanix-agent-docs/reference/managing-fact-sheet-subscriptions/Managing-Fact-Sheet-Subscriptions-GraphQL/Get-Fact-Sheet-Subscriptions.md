##  Get Fact Sheet Subscriptions
To retrieve all subscriptions for a specific fact sheet, use the factSheet query. id is a required argument for this query. To learn how to get the ID of a fact sheet, see [Retrieving Fact Sheets](https://help.sap.com/docs/leanix/ea/retrieving-fact-sheets?locale=en-US&state=PRODUCTION&version=CLOUD "Example queries for retrieving fact sheets through the GraphQL API.").
Example query:

```
query {
  factSheet(id: "01740698-1ffa-4729-94fa-da6194ebd7cd") {
    id
    subscriptions {
      edges {
        node {
          id
          user {
            id
            email
          }
          type
          roles {
            id
            name
            comment
          }
        }
      }
    }
  }
}
```



Example response:

```
{
  "data": {
    "factSheet": {
      "id": "01740698-1ffa-4729-94fa-da6194ebd7cd",
      "subscriptions": {
        "edges": [
          {
            "node": {
              "id": "abd9ca16-b4a7-4199-a0ad-36e5a6de117b",
              "user": {
                "id": "e45f0d10-c59e-4c80-bd56-56b9e7325gf6",
                "email": "john.doeC@organization.com"
              },
              "type": "RESPONSIBLE",
              "roles": [
                {
                  "id": "b4ccabdc-f0c4-4386-8ff0-b54e0882605f",
                  "name": "Application Manager",
                  "comment": null
                }
              ]
            }
          }
        ]
      }
    }
  }
}
```



