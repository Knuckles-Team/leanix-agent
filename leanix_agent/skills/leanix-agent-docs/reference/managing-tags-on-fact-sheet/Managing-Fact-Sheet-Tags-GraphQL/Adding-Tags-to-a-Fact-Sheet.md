##  Adding Tags to a Fact Sheet
To add tags to a fact sheet, use the updateFactSheet mutation. Provide the tag details through the add patch operation.
id is a required argument for this mutation. To learn how to get the ID of a Fact Sheet, see [Retrieving Fact Sheets](https://help.sap.com/docs/leanix/ea/retrieving-fact-sheets?locale=en-US&state=PRODUCTION&version=CLOUD "Example queries for retrieving fact sheets through the GraphQL API.").
### Adding Existing Tags to a Fact Sheet
Before you add existing tags to a fact sheet, get the id of tags. To do that, retrieve all tags using the allTags query and copy the id of the desired tags from the response.
Example query:

```
{
  allTags {
    edges {
      node {
        id
        name
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
    "allTags": {
      "edges": [
        {
          "node": {
            "id": "c26a8509-330e-4d8f-ba48-2defcdc910f7",
            "name": "Europe"
          }
        },
        {
          "node": {
            "id": "7b27fc19-585e-4d95-acae-65891575a42f",
            "name": "Cloud"
          }
        }
      ]
    }
  }
}
```



Once you get the id of tags that you want to add to a Fact Sheet, use the updateFactSheet mutation.
Example mutation:

```
mutation ($patches: [Patch]!) {
  updateFactSheet(id: "2efa37b5-18aa-48d8-9d70-1328c0d856d7", patches: $patches) {
    factSheet {
      id
      name
      tags {
        id
        name
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
      "path": "/tags",
      "value": "[{\"tagId\":\"7b27fc19-585e-4d95-acae-65891575a42f\"}, {\"tagId\":\"c26a8509-330e-4d8f-ba48-2defcdc910f7\"}]"
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
        "id": "2efa37b5-18aa-48d8-9d70-1328c0d856d7",
        "name": "AC Management Cloud",
        "tags": [
          {
            "id": "c26a8509-330e-4d8f-ba48-2defcdc910f7",
            "name": "Europe"
          },
          {
            "id": "7b27fc19-585e-4d95-acae-65891575a42f",
            "name": "Cloud"
          }
        ]
      }
    }
  }
}
```



### Adding New Tags to a Fact Sheet
In the following example, we create two new tags that don't belong to any tag group and add them to a Fact Sheet.
Example mutation:

```
mutation ($patches: [Patch]!) {
  updateFactSheet(id: "2efa37b5-18aa-48d8-9d70-1328c0d856d7", patches: $patches) {
    factSheet {
      id
      name
      tags {
        id
        name
        tagGroup {
          name
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
      "path": "/tags",
      "value": "[{\"tagName\":\"Development\"}, {\"tagName\":\"Demo\"}]"
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
        "id": "2efa37b5-18aa-48d8-9d70-1328c0d856d7",
        "name": "AC Management Cloud",
        "tags": [
          {
            "id": "2ddc9122-4513-40e2-afd8-4b28f41474a4",
            "name": "Demo",
            "tagGroup": null
          },
          {
            "id": "0eb40008-28ac-467c-adc5-5b995ca47769",
            "name": "Development",
            "tagGroup": null
          }
        ]
      }
    }
  }
}
```



