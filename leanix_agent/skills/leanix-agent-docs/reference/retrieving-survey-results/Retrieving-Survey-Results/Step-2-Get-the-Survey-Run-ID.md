##  Step 2: Get the Survey Run ID
Now that you have the id of the survey, retrieve all runs for this survey. To do that, make a GET request to the following endpoint:

```
https://{SUBDOMAIN}.leanix.net/services/survey/v1/polls/{id}/pollRuns
```



Example request:

```
curl -X GET \
--header 'Accept: application/json' \
--header 'Authorization: Bearer {ACCESS_TOKEN}' \
'https://{SUBDOMAIN}.leanix.net/services/survey/v1/polls/0b62781b-4266-4020-g87h-4cacb7947ba8/pollRuns?page=1&size=500&sort=-startTime'
```



Example response:

```
{
  "status": "OK",
  "type": "PollRun",
  "total": 2,
  "data": [
    {
      "id": "ce6a4af8-7060-4adc-5ac8-2daa85efe616",
      "poll": {
        "id": "0b62781b-4266-4020-g87h-4cacb7947ba8",
        "title": "Location"
      },
      "status": "STARTED",
      "startTime": "2024-08-24T10:55:54.693671Z",
      "factsheetsTotal": 5,
      "factsheetsCompleted": 3,
      "factsheetsSelected": 5,
      "creator": {
        "id": "user-uuid-1",
        "firstName": "Jane",
        "lastName": "Smith",
        "email": "jane.smith@example.com"
      }
    },
    {
      "id": "c0735b3b-b032-4b0d-{...}-77f5e68b5210",
      "poll": {
        "id": "0b62781b-4266-4020-g87h-4cacb7947ba8",
        "title": "Location"
      },
      "status": "STARTED",
      "startTime": "2024-08-22T06:40:08.927306Z",
      "factsheetsTotal": 5,
      "factsheetsCompleted": 5,
      "factsheetsSelected": 5,
      "creator": {
        "id": "user-uuid-2",
        "firstName": "Bob",
        "lastName": "Johnson",
        "email": "bob.johnson@example.com"
      }
    }
  ]
}
```



From the response, save the id of the desired survey run.
