##  Error Handling for Batch Mutations
When multiple mutations are included in a request and at least one mutation is invalid, none of the mutations are executed. The data and errors attributes provide details about the failed mutation.
In the example request below, the mutation m2 for updating a fact sheet includes an invalid field: descriptio.
Example request:

```
mutation {
  m1: updateFactSheet(
    id: "d9506c79-5d4e-4661-9297-b3b84bd17b79"
    patches: [{ op: replace, path: "/description", value: "first description" }]
  ) {
    factSheet {
      id
      description
    }
  }
  m2: updateFactSheet(
    id: "3b2f5b03-8cff-4aa1-a619-38aa7e90d456"
    patches: [
      { op: replace, path: "/descriptio", value: "invalid field description" }
    ]
  ) {
    factSheet {
      id
      description
    }
  }
  m3: updateFactSheet(
    id: "351ee5ff-c851-48c5-92e6-3d373c6483ce"
    patches: [
      { op: replace, path: "/description", value: "third description" }
    ]
  ) {
    factSheet {
      id
      description
    }
  }
}
```



In the response, the data attribute returns null. The errors attribute provides details about the failed mutation. An error message indicates that the entire request hasn't been executed and none of the mutations have been applied.
Example response:

```
{
  "data" : null,
  "errors" : [ {
    "message" : "The path '/descriptio' is invalid in FactSheet schema Application.",
    "path" : [ "m2" ],
    "extensions" : {
      "errorType" : "BUSINESS_LOGIC"
    }
  }, {
    "message" : "Error in Request. Transaction is rolled back!",
    "path" : [ ],
    "extensions" : {
      "errorType" : "BUSINESS_LOGIC"
    }
  } ]
}
```



