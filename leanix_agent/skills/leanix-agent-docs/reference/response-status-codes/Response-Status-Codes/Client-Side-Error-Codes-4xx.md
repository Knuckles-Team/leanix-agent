##  Client-Side Error Codes (4xx)
4xx status codes indicate errors originating from the client side, such as invalid requests or missing parameters. They provide actionable information for identifying and rectifying the problem before retrying the request. These error codes adhere to the guidelines specified in [Section 6.5 of RFC 7231![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fdatatracker.ietf.org%2Fdoc%2Fhtml%2Frfc7231%23section-6.5 "https://datatracker.ietf.org/doc/html/rfc7231#section-6.5"), the Internet Standards Track document issued by IETF.
Code | Meaning
---|---
400 (Bad Request) | The request was malformed or invalid.
401 (Unauthorized) | The request requires authentication.
403 (Forbidden) | The request is not authorized to access the resource.
404 (Not Found) | The resource does not exist.
405 (Method Not Allowed) | The requested method is not supported for the specified resource.
409 (Conflict) | The request could not be completed due to a conflict with the current state of the target resource.
410 (Gone) | The requested resource is no longer available.
422 (Validation Error) | The request was syntactically valid but semantically invalid, meaning that the data provided does not meet the specified validation rules.
429 (Too Many Requests) | The request rate exceeds the allowed limit. For more information, see [Rate Limiting](https://help.sap.com/docs/leanix/ea/rate-limiting?locale=en-US&state=PRODUCTION&version=CLOUD "Learn how our rate limiting in SAP LeanIX APIs works.").


