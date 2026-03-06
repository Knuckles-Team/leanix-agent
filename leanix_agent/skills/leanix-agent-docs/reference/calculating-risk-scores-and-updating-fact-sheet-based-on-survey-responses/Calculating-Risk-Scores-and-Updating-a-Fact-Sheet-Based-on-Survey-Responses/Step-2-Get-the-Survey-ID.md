##  Step 2: Get the Survey ID
The automation is initiated only for a specific survey. To get the survey ID, navigate to the survey page in your workspace and copy the id from the URL.
Alternatively, you can get the survey id through the API. To do that, make a GET request to the following endpoint and save the id from the response. To learn how to get an access token, see [Authentication to SAP LeanIX Services](https://help.sap.com/docs/leanix/ea/authentication-to-sap-leanix-services?locale=en-US&state=PRODUCTION&version=CLOUD "Learn how to authenticate to SAP LeanIX services.").

```
https://{SUBDOMAIN}.leanix.net/services/poll/v2/polls
```



Example request:

```
curl -X GET
--header 'Accept: application/json'
--header 'Authorization: Bearer {ACCESS_TOKEN}'
'https://{SUBDOMAIN}.leanix.net/services/poll/v2/polls?q=Technology%Risk%20Assessment'
```



Example response:

```
{
  "status": "OK",
  "type": "Poll",
  "errors": [],
  "total": 1,
  "data": [
    {
      "id": "411f278a-eb38-4b45-84b3-5abf648d0e49",
      "legacyId": null,
      "questionnaire": {
        "id": "f01ec0ea-5137-75e6-73b0-53d8fbf02e27",
        "questions": [...]
      },
      "title": "Technology Risk Assessment",
      ...
    }
  ]
}
```



