##  Error Handling in SAP LeanIX GraphQL
When an error occurs in SAP LeanIX GraphQL, the response includes an errors array in the JSON payload. Each error object in the array contains a message field that describes the error. It may also contain a locations field that provides additional information.
Example GraphQL error response:

```
{
  "data": null,
  "errors": [
    {
      "message": "Validation error of type FieldUndefined: Field nonExistenField is undefined",
      "locations": [
        {
          "line": 6,
          "column": 9
        }
      ]
    }
  ]
}
```



