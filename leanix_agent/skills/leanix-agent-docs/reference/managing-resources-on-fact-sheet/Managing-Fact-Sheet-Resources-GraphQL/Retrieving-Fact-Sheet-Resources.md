##  Retrieving Fact Sheet Resources
To retrieve resources stored on a specific fact sheet, use the factSheet query. The fact sheet id is a required argument for this query.
Example query:

```
{
  factSheet(id: "4d121f64-116b-4ccc-a292-eb4e4f8d1b24") {
    id
    name
    documents {
      edges {
        node {
          origin
          url
          name
          id
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
      "id": "4d121f64-116b-4ccc-a292-eb4e4f8d1b24",
      "name": "AC Management Cloud",
      "documents": {
        "edges": [
          {
            "node": {
              "origin": "CUSTOM_LINK",
              "url": "https://www.leanix.net/",
              "name": "Website link",
              "id": "22b9ed8f-5dea-48e8-b9c4-d7db97a811e4"
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
