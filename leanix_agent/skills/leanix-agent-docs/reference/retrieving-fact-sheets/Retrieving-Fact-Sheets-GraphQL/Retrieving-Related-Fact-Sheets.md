##  Retrieving Related Fact Sheets
You can retrieve related fact sheets for a specific fact sheet using an inline fragment.
In the example, we retrieve the following data for a specific fact sheet of the IT component type:
  * All related fact sheets of the tech category type, referred to as TechnicalStack in the GraphQL API
  * All child fact sheets and their related fact sheets of the tech category type


Example query:

```
{
  factSheet(id: "afd31c81-3fff-4367-9d90-458eecb3efa7") {
    name
    type
    ... on ITComponent {
      relITComponentToTechnologyStack {
        edges {
          node {
            id
            factSheet {
              name
            }
          }
        }
      }
      relToChild {
        edges {
          node {
            id
            factSheet {
              name
              type
              ... on ITComponent {
                relITComponentToTechnologyStack {
                  edges {
                    node {
                      id
                      factSheet {
                        name
                        type
                      }
                    }
                  }
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
Example response:

```
{
  "data": {
    "factSheet": {
      "name": "Application Hosting",
      "type": "ITComponent",
      "relITComponentToTechnologyStack": {
        "edges": [
          {
            "node": {
              "id": "5628093c-6106-4ead-a02d-86d5e7e21a3a",
              "factSheet": {
                "name": "Hosting"
              }
            }
          }
        ]
      },
      "relToChild": {
        "edges": [
          {
            "node": {
              "id": "08bde56f-ea78-438c-975a-7667a4be7caf",
              "factSheet": {
                "name": "Application Development",
                "type": "ITComponent",
                "relITComponentToTechnologyStack": {
                  "edges": [
                    {
                      "node": {
                        "id": "8834a6a8-c73e-4c79-91ea-a3aed3bc9b59",
                        "factSheet": {
                          "name": "Design & Development",
                          "type": "TechnicalStack"
                        }
                      }
                    }
                  ]
                }
              }
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
YesNo
Send
