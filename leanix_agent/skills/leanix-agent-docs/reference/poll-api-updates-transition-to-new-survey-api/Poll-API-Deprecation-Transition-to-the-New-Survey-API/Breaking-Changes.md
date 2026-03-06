##  Breaking Changes
### Response Wrappers
The GET /pollRuns response is now wrapped differently:
Poll API v2:

```
{
  "status": "OK",
  "type": "PollRun",
  "total": 5,
  "data": [ { }, { } ]
}

```



Survey API v1:

```
{
  "status": "OK",
  "type": "PollRun",
  "total": 5,
  "data": {
    "pollRuns": [ { }, { } ],
    "count": { "total": 5, "completed": 3, "open": 2 }
  }
}

```



### POST /pollRuns Request Simplified
Field | Poll API v2 | Survey API v1 | Status
---|---|---|---
workspaceId | Required | Not needed | Removed
pollId | N/A | Required | New
users | N/A | Optional (List<User>) | New
resultView | Optional | Optional (default: NEW) | Unchanged


### GET /pollRuns/{id}/recipients Response Restructured
The recipients endpoint now returns data in nested relationship objects instead of flat lists.
### Poll Result Response Enhanced
New fields in the Survey API v1:
  * sender: The user who sent the survey.
  * factSheet: Enhanced fact sheet information.
  * requestingUser: Requesting user information (conditional).
