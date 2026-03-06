##  Moving the Cursor
Once you have successfully retrieved and processed a batch of events, you need to move the cursor forward to get the next batch. Otherwise, the next GET request would return the same events as in the previous response. This ensures that even if your application is temporarily malfunctioning, it will eventually receive all events.
**Caution**
When using PULL webhooks, move the cursor forward only after you've processed the current batch of events. Once the cursor is moved, you can't fetch events from previous batches.
To move the cursor to the next given nextCursor, make a PUT request to the following endpoint:

```
https://{SUBDOMAIN}.leanix.net/services/webhooks/v1/subscriptions/{id}/cursor
```



Example request:

```
curl --request PUT \
  --url https://{SUBDOMAIN}.leanix.net/services/webhooks/v1/subscriptions/888eaaf3-c72f-411c-a78a-d382ba9b2f75/cursor \
  --header 'Authorization: Bearer {ACCESS_TOKEN}' \
  --header 'Content-Type: application/json' \
  --data '{"offset": 182}'
```



Alternatively, you can move the cursor forward automatically when retrieving events. To enable this behavior, add autoCommit=true as a query string parameter to the /services/webhooks/v1/subscriptions/{id}/events endpoint. Enabling automated commits does not guarantee that all events will be successfully received and processed by your application due to possible network issues or other problems.
Example request:

```
curl --request GET \
  --url https://{SUBDOMAIN}.leanix.net/services/webhooks/v1/subscriptions/888eaaf3-c72f-411c-a78a-d382ba9b2f75/events?autoCommit=true \
  --header 'Authorization: Bearer {ACCESS_TOKEN}'
```



YesNo
Send
