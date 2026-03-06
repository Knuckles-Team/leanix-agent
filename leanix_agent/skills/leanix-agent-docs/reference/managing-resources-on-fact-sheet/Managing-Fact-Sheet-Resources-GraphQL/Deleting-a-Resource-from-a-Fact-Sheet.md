##  Deleting a Resource from a Fact Sheet
To delete a resource from a fact sheet, use the deleteDocument mutation. id is a required argument for this mutation. To get the resource ID, retrieve all fact sheet resources and copy the id from the response. To learn more, see [Retrieving Fact Sheet Resources](https://help.sap.com/docs/leanix/ea/managing-resources-on-fact-sheet?locale=en-US&state=PRODUCTION&version=CLOUD#loio275aeb7e7a441014b435fc69360fba20__retrieving_fact_sheet_resources).
Example mutation:

```
mutation {
  deleteDocument(id: "a1904f80-f9b8-4fd6-848c-bad1f55192d2") {
    name
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
    "deleteDocument": null
  }
}
```



YesNo
Send
