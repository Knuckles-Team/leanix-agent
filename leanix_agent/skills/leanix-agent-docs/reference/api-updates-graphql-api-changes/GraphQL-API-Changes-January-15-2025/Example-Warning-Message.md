##  Example Warning Message
For invalid requests, a warning message is returned in the response, as shown in the following example. The warning message and relevant details are returned in extensions, which is a new element introduced in responses. Review the details provided in reasons and adjust your queries as necessary.

```
{
  "data": { ... },
  "extensions": {
    "warnings": [
      {
        "message": "Your request contains elements that will be considered invalid after January 15, 2025 due to stricter GraphQL API validation rules. Please review and update your request as necessary.",
        "reasons": [
          "Invalid syntax encountered. There are extra tokens in the text that have not been consumed. Offending token '}' at line 10 column 1"
        ]
      }
    ]
  }
}
```



