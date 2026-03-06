##  Stricter Validation of Unconsumed Tokens
One of the upcoming API changes addresses the issue of unconsumed tokens in the request body. Previously, our validation might have allowed requests containing extra tokens (for example, }) at the end of the payload to pass through. Under the new validation rules, such requests will be flagged as malformed and will fail validation.
### What You Need to Do
Review the payloads of your GraphQL API requests for any extraneous characters following the intended data. To ensure successful calls after the grace period, you should modify your code or tools to construct requests that strictly adhere to the documented syntax, avoiding any extraneous characters after defined parameters.
### Example Query and Warning Message
Under the new validation rules, the following example request would fail.
Example query with unconsumed tokens:

```
{
  allFactSheets(first: 10, factSheetType: Application) {
    totalCount
    edges {
      node {
        id
        name
        type
      }
    }
  }
}}
```



Example warning message:

```
    "warnings": [
      {
        "message": "Your request contains elements that will be considered invalid after January 15, 2025 due to stricter GraphQL API validation rules. Please review and update your request as necessary.",
        "reasons": [
          "Invalid syntax encountered. There are extra tokens in the text that have not been consumed. Offending token '}' at line 12 column 2"
        ]
      }
    ]
  }
```



