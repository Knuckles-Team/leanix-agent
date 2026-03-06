##  Updating a Resource on a Fact Sheet
To update a resource on a fact sheet, use the updateDocument mutation. id is a required argument for this mutation. To get the resource ID, retrieve all fact sheet resources and copy the id from the response. To learn more, see [Retrieving Fact Sheet Resources](https://help.sap.com/docs/leanix/ea/managing-resources-on-fact-sheet?locale=en-US&state=PRODUCTION&version=CLOUD#loio275aeb7e7a441014b435fc69360fba20__retrieving_fact_sheet_resources).
To update specific fields on a resource, apply patch operations. In the example, we change the link URL using the replace patch operation.
Example mutation:

```
mutation updateDocument($patches: [Patch]!) {
  updateDocument(
    id: "22b9ed8f-5dea-48e8-b9c4-d7db97a811e4"
    patches: $patches
  ) {
    id
    name
    url
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
      "op": "replace",
      "path": "/url",
      "value": "https://www.leanix.net/de/"
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
    "updateDocument": {
      "id": "22b9ed8f-5dea-48e8-b9c4-d7db97a811e4",
      "name": "Website link",
      "url": "https://www.leanix.net/de/"
    }
  }
}
```



