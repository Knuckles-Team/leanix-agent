##  Creating Fact Sheet Relations
To create relations between Fact Sheets, use the updateFactSheet mutation. Apply the add patch operation with a path that identifies the relation attribute. You can create multiple relations with one request.
To get individual error messages for each relation in case of possible errors, add a suffix in the following format /new_1 to the path values. Use a unique suffix for each relation.
Example mutation:

```
mutation ($patches: [Patch]!) {
  updateFactSheet(id: "4d121f64-116b-4ccc-a292-eb4e4f8d1b24", patches: $patches) {
    factSheet {
      id
      name
      ... on Application {
        relApplicationToITComponent {
          edges {
            node {
              id
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
Variables:

```
{
  "patches": [
    {
      "op": "add",
      "path": "/relApplicationToITComponent/new_1",
      "value": "{\"factSheetId\":\"9deb9733-5701-42f1-8c52-c165acaa6487\"}"
    },
    {
      "op": "add",
      "path": "/relApplicationToITComponent/new_2",
      "value": "{\"factSheetId\":\"a8fe4825-42b8-431b-8124-ca12c579c78b\"}"
    }
  ]
}
```



Example response:

```
{
  "data": {
    "updateFactSheet": {
      "factSheet": {
        "id": "4d121f64-116b-4ccc-a292-eb4e4f8d1b24",
        "name": "AC Management Cloud",
        "relApplicationToITComponent": {
          "edges": [
            {
              "node": {
                "id": "41ff8420-05d2-46e8-9912-975a9263f27e"
              }
            },
            {
              "node": {
                "id": "8a039155-774b-4c09-94b1-e221eb0fee1c"
              }
            }
          ]
        }
      }
    }
  }
}
```



The following response contains an example error message that may be returned by the server. The path attribute identifies the corresponding patch operation from the request.
Example error response:

```
{
  "data": {
    "updateFactSheet": null
  },
  "errors": [
    {
      "message": "[FS_VALIDATION_RELATION_NOT_UNIQUE_OUTGOING] Outgoing relation occurred twice! relation name = 'applicationITComponentRelation', from = 'AC Management Cloud', from type = 'Application', to = 'App Maintenance & Support Service', to type = 'ITComponent'",
      "path": [
        "result"
      ],
      "extensions": {
        "entityType": "FACT_SHEET",
        "objectId": "4d121f64-116b-4ccc-a292-eb4e4f8d1b24",
        "objectPath": "/relApplicationToITComponent/fbec0812-ec6b-4c2c-8df2-525d5d3f3121",
        "errorType": "MODEL_COMPLIANT"
      }
    }
  ]
}
```



