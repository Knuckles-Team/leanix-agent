##  Step 3: Get Survey Results
You can get survey results for:
  * All fact sheets included in a survey run
  * A specific fact sheet included in a survey run


### Get Results for All Fact Sheets in a Survey Run
With the survey run ID, you can retrieve results for all fact sheets included in the survey run. To do that, make a GET request to the following endpoint:

```
https://{SUBDOMAIN}.leanix.net/services/survey/v1/pollRuns/{pollRunID}/pollResults
```



Example request:

```
curl -X GET \
--header 'Accept: application/json' \
--header 'Authorization: Bearer {ACCESS_TOKEN}' \
'https://{SUBDOMAIN}.leanix.net/services/survey/v1/pollRuns/ce6a4af8-7060-4adc-5ac8-2daa85efe616/pollResults'
```



The response contains survey results for all fact sheets included in the survey run. Each result is associated with a specific fact sheet and has a unique ID.
Example response:

```
{
  "status": "OK",
  "type": "PollResult",
  "total": 2,
  "data": [
    {
      "id": "10fd7951-1e44-4643-e6g4-ed5db8c44e29",
      "pollRunId": "ce6a4af8-7060-4adc-5ac8-2daa85efe616",
      "status": "DONE",
      "answers": [
        {
          "questionId": "cc2a3670-9d9d-5e41-6g4h-c579cdd89b1c",
          "value": "Users are based in Australia.",
          "type": "TEXT"
        }
      ],
      "users": [
        {
          "id": "user-uuid-3",
          "firstName": "Alice",
          "lastName": "Brown",
          "email": "alice.brown@example.com"
        }
      ],
      "sender": {
        "id": "user-uuid-1",
        "firstName": "Jane",
        "lastName": "Smith",
        "email": "jane.smith@example.com"
      },
      "factSheet": {
        "id": "fs-uuid-1",
        "name": "System A",
        "displayName": "Australian Office Systems",
        "type": "Application"
      }
    },
    {
      "id": "2dff1a8b-33b6-494c-b855-c8604045e333",
      "pollRunId": "ce6a4af8-7060-4adc-5ac8-2daa85efe616",
      "status": "DONE",
      "answers": [
        {
          "questionId": "cc2a3670-9d9d-5e41-6g4h-c579cdd89b1c",
          "value": "Users are based in Brazil.",
          "type": "TEXT"
        }
      ],
      "users": [
        {
          "id": "user-uuid-4",
          "firstName": "Carlos",
          "lastName": "Silva",
          "email": "carlos.silva@example.com"
        }
      ],
      "sender": {
        "id": "user-uuid-1",
        "firstName": "Jane",
        "lastName": "Smith",
        "email": "jane.smith@example.com"
      },
      "factSheet": {
        "id": "fs-uuid-2",
        "name": "System B",
        "displayName": "Brazilian Office Systems",
        "type": "Application"
      }
    }
  ]
}
```



### Get Results for a Specific Fact Sheet in a Survey Run
You can retrieve a result for a specific fact sheet included in a survey run by the result ID. First, retrieve all results and save the id of the desired result from the response.
To retrieve a survey result by ID, make a GET request to the following endpoint:

```
https://{SUBDOMAIN}.leanix.net/services/survey/v1/pollResults/{pollResultID}
```



Example request:

```
curl -X GET \
--header 'Accept: application/json' \
--header 'Authorization: Bearer {ACCESS_TOKEN}' \
'https://{SUBDOMAIN}.leanix.net/services/survey/v1/pollResults/10fd7951-1e44-4643-e6g4-ed5db8c44e29'
```



Example response:

```
{
  "status": "OK",
  "type": "PollResult",
  "total": 1,
  "data": {
    "id": "10fd7951-1e44-4643-e6g4-ed5db8c44e29",
    "pollRunId": "ce6a4af8-7060-4adc-5ac8-2daa85efe616",
    "status": "DONE",
    "answers": [
      {
        "questionId": "cc2a3670-9d9d-5e41-6g4h-c579cdd89b1c",
        "value": "Users are based in Australia.",
        "type": "TEXT"
      }
    ],
    "users": [
      {
        "id": "user-uuid-3",
        "firstName": "Alice",
        "lastName": "Brown",
        "email": "alice.brown@example.com"
      }
    ],
    "sender": {
      "id": "user-uuid-1",
      "firstName": "Jane",
      "lastName": "Smith",
      "email": "jane.smith@example.com"
    },
    "factSheet": {
      "id": "fs-uuid-1",
      "name": "System A",
      "displayName": "Australian Office Systems",
      "type": "Application"
    },
    "requestingUser": {
      "id": "user-uuid-5",
      "firstName": "Admin",
      "lastName": "User",
      "email": "admin@example.com"
    }
  }
}
```



