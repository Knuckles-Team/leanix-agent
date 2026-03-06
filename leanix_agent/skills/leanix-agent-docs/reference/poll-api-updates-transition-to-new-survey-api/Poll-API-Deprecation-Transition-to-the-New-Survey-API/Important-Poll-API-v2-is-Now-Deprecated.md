##  Important: Poll API v2 is Now Deprecated
As of January 20, 2026, all responses from the legacy Poll API v2 include deprecation headers indicating that this API is no longer recommended for use. Check for these headers in your code to detect deprecated endpoints automatically.
Response headers added:

```
X-SAP-stateInfo: {"state": "deprecated"}
X-API-Warn: 'poll/v2' is a deprecated API. Please use 'survey/v1'.

```



What this means:
  * The Poll API v2 is officially deprecated and will be discontinued at the end of March 2027.
  * Use the Survey API v1 for all integrations.
  * If you use existing integrations, plan to migrate them now.
  * Deprecation headers appear on every response from Poll API v2 endpoints.


Example response headers:

```
HTTP/1.1 200 OK
X-SAP-stateInfo: {"state": "deprecated"}
X-API-Warn: 'poll/v2' is a deprecated API. Please use 'survey/v1'.
Content-Type: application/json

{...response body...}

```



