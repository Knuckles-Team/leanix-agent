##  Stricter Validation of Invalid Tokens
Another upcoming API change involves stricter validation to catch requests with invalid syntax and unexpected tokens. Under the new validation rules, malformed requests will be flagged as invalid and will fail validation.
### What You Need to Do
  * Ensure that there are no incorrectly escaped characters within your request data.
  * Ensure that your development environment and tools are configured to use the correct character encoding.
  * Examine specific warning messages returned by our API to identify the location and nature of the syntax issue.


### Example Query and Warning Message
Under the new validation rules, the following example request would fail.
Example query with invalid tokens:

```
{
  ��factSheet(id: "28fe4aa2-6e46-41a1-a131-72afb3acf256") {
  ����displayName
  ��������... on Application {
  ������relApplicationToUserGroup {
  ��������edges {
  ����������node {
  ������������id
  ������usageType
  ������factSheet {
  ��������������level
  ��������������id
  ��������������name
  ��������������displayName
  ������������}
  ����������}
  ��������}
  ������}
  ����}
  ��}
  }
```



Example warning message:

```
[
      {
        "message": "Your request contains elements that will be considered invalid after January 15, 2025 due to stricter GraphQL API validation rules. Please review and update your request as necessary.",
        "reasons": [
          "Invalid syntax with ANTLR error 'token recognition error at: '�'' at line 2 column 3"
        ]
      }
]
```



