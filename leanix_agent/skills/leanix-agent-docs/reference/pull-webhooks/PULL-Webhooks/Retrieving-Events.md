##  Retrieving Events
Before you start, ensure that you know how to authenticate to SAP LeanIX APIs. To learn more, see [Authentication to SAP LeanIX Services](https://help.sap.com/docs/leanix/ea/authentication-to-sap-leanix-services?locale=en-US&state=PRODUCTION&version=CLOUD "Learn how to authenticate to SAP LeanIX services.").
To retrieve events, make a GET request to the following endpoint:

```
https://{SUBDOMAIN}.leanix.net/services/webhooks/v1/subscriptions/{id}/events
```



To get the subscription id, navigate to the webhook details page.
Example request:

```
curl --request GET \
  --url https://{SUBDOMAIN}.leanix.net/services/webhooks/v1/subscriptions/888eaaf3-c72f-411c-a78a-d382ba9b2f75/events \
  --header 'Authorization: Bearer {ACCESS_TOKEN}'
```



Example response:

```
{
  "status": "OK",
  "type": "PullResult",
  "errors": [],
  "total": 3,
  "data": {
    "events": [
      {
        "cursor": {
          "offset": 178
        },
        "event": {...}
      },
      {
        "cursor": {
          "offset": 179
        },
        "event": {...}
      }
    ],
    "nextCursor": {
      "offset": 182
    }
  }
}
```



The event object contains the webhook payload. Additionally, each event is annotated with the cursor attribute that can be used later to navigate to this event. The nextCursor attribute applies to the entire batch of events.
If there are no new events, an empty response is returned.
