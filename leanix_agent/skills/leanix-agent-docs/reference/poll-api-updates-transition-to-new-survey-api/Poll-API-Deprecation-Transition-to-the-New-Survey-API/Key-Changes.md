##  Key Changes
### Base URL Update
Use the new endpoint for all API calls.
Before:

```
curl -X GET "https://{SUBDOMAIN}.leanix.net/services/poll/v2/polls?workspaceId=a1b2c3d4"

```



After:

```
curl -X GET "https://{SUBDOMAIN}.leanix.net/services/survey/v1/polls"

```



### Removed workspaceId Query Parameter
The workspace is now automatically determined from your authentication token.
Endpoint | Poll API v2 | Survey API v1
---|---|---
Get surveys | GET /polls?workspaceId={id} | GET /polls
Create a survey | POST /polls?workspaceId={id} | POST /polls
Get a survey run | GET /pollRuns/{id}?workspaceId={id} | GET /pollRuns/{id}
Create a survey run | POST /pollRuns?workspaceId={id} | POST /pollRuns


### Sorting Parameter Format Changed (Breaking Change)
The sorting format has been simplified for better usability.
Poll API v2:

```
GET /polls?sort=createdAt-asc
GET /polls?sort=createdAt-desc

```



Survey API v1:

```
GET /polls?sort=+createdAt
GET /polls?sort=-createdAt

```



Use Case | Poll API v2 | Survey API v1
---|---|---
Sort by creation date (newest first) | sort=createdAt-desc | sort=-createdAt
Sort by start time (oldest first) | sort=startTime-asc | sort=+startTime
Sort by title (A-Z) | sort=title-asc | sort=+title
Multiple sorts | sort=status-asc,createdAt-desc | sort=+status,-createdAt


### HTTP Response Codes Changed (Breaking Change)
Some DELETE endpoints now return different HTTP status codes.
Endpoint | Poll API v2 | Survey API v1 | Change
---|---|---|---
DELETE /polls/{pollId} | HTTP 200 | HTTP 204 No Content | Changed
DELETE /pollRuns/{pollRunId} | HTTP 200 | HTTP 204 No Content | Changed


What this means:
  * DELETE operations now return HTTP 204 (No Content) instead of HTTP 200 (OK).
  * HTTP 204 indicates successful deletion with no response body.
  * Update your client code to handle 204 responses on delete operations.
  * Treat both 2xx responses as successful.


Example:

```
// Before (Poll API v2)
DELETE /services/poll/v2/polls/{pollId}
// Returns: HTTP 200 with empty body

// After (Survey API v1)
DELETE /services/survey/v1/polls/{pollId}
// Returns: HTTP 204 No Content

```



### Core Endpoints Available in Both APIs
  * GET/POST /polls
  * GET/PUT /polls/{pollId}
  * DELETE /polls/{pollId}
  * GET/POST /pollRuns
  * GET/PUT /pollRuns/{pollRunId}
  * DELETE /pollRuns/{pollRunId}
  * GET /pollResults
  * GET /pollRuns/{pollRunId}/poll_results
  * GET /pollResults.xlsx
  * GET /pollTemplates
