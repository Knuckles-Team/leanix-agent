##  Step 1: Get the Survey ID
First, get the ID of the survey you want to retrieve results from. To retrieve all surveys, make a GET request to the following endpoint:

```
https://{SUBDOMAIN}.leanix.net/services/survey/v1/polls
```



In the example request, we retrieve a survey by its title using the q query parameter.
Example request:

```
curl -X GET \
--header 'Accept: application/json' \
--header 'Authorization: Bearer {ACCESS_TOKEN}' \
'https://{SUBDOMAIN}.leanix.net/services/survey/v1/polls?page=1&size=30&sort=-createdAt&q=Location'
```



Example response:

```
{
  "status": "OK",
  "type": "Poll",
  "total": 1,
  "data": [
    {
      "id": "0b62781b-4266-4020-g87h-4cacb7947ba8",
      "title": "Location",
      "language": "en",
      "questionnaire": {
        "questions": [
          {
            "id": "q1-uuid",
            "text": "Where are your users located?",
            "type": "TEXT"
          }
        ]
      },
      "createdAt": "2024-01-15T10:00:00Z",
      "createdBy": {
        "id": "user-uuid",
        "firstName": "John",
        "lastName": "Doe"
      }
    }
  ]
}
```



From the response, save the id of the desired survey.
