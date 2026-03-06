##  Examples
### Example 1: Retrieving Surveys
Before (Poll API v2):

```
curl -X GET "https://{SUBDOMAIN}.leanix.net/services/poll/v2/polls?workspaceId=abc123&sort=createdAt-desc"

```



After (Survey API v1):

```
curl -X GET "https://{SUBDOMAIN}.leanix.net/services/survey/v1/polls?sort=-createdAt"

```



### Example 2: Creating a Survey Run
Before (Poll API v2):

```
POST /services/poll/v2/pollRuns?workspaceId=abc123
{
  "status": "STARTED",
  "factsheetIds": ["id1", "id2"],
  "recipientIds": ["user1", "user2"]
}

```



After (Survey API v1):

```
POST /services/survey/v1/pollRuns
{
  "pollId": "poll-uuid",
  "resultView": "NEW"
}

```



### Example 3: Sorting with Multiple Fields
Before (Poll API v2):

```
GET /polls?sort=status-asc,createdAt-desc

```



After (Survey API v1):

```
GET /polls?sort=+status,-createdAt

```



### Example 4: Deleting a Survey
Before (Poll API v2):

```
DELETE /services/poll/v2/polls/{pollId}
# Returns: HTTP 200 OK

```



After (Survey API v1):

```
DELETE /services/survey/v1/polls/{pollId}
# Returns: HTTP 204 No Content

```



