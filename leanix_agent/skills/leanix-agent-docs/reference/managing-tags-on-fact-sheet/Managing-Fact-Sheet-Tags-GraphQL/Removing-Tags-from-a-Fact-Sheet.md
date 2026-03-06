##  Removing Tags from a Fact Sheet
Before you remove tags from a Fact Sheet, get the id of tags. To do that, retrieve all tags using the allTags query and copy the id of the desired tags from the response.
**Note**
Removing a tag from a Fact Sheet does not delete the tag from your workspace.
To remove tags from a Fact Sheet, use the updateFactSheet mutation and apply the remove patch operation.
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
      "op": "remove",
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
        "tags": []
      }
    }
  }
}
```



