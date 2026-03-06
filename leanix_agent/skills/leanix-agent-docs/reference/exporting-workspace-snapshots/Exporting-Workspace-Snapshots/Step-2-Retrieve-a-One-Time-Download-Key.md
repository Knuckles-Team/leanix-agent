##  Step 2: Retrieve a One-Time Download Key
Before you download a file with workspace data, retrieve a one-time key that serves as the download identifier. To do that, make a GET request to the following endpoint:

```
https://{SUBDOMAIN}.leanix.net/services/pathfinder/v1/exports
```



You can optionally use query parameters to filter the results returned in the response.
Example request:

```
curl -X 'GET' \
  'https://{SUBDOMAIN}.leanix.net/services/pathfinder/v1/exports?exportType=SNAPSHOT&pageSize=40&sorting=createdAt&sortDirection=DESC' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}'
```



Example response:

```
{
  "status": "OK",
  "type": "Export",
  "data": [
    {
      "id": "3159d0bc-f0c1-4d6a-a541-cc534ebf7102",
      "user": {
        "id": "25d63c1a-4cc9-4c46-bb4c-a82a78cb8686",
        "firstName": null,
        "lastName": "Technical User",
        "displayName": "Technical User",
        "userName": "Technical User",
        "email": null,
        "technicalUser": true,
        "role": "ACCOUNTUSER",
        "status": "ACTIVE"
      },
      "type": "SNAPSHOT",
      "status": "COMPLETED",
      "createdAt": "2024-03-26T15:04:25.378194Z",
      "deleteAt": "2024-03-26T15:14:29.515400Z",
      "dryRun": false,
      "downloadKey": "ba25c032-f399-462e-803a-016bdf13335d",
      "factSheetTypes": null,
      "factSheetCount": null,
      "columnCount": null,
      "bookmark": null
    },
    ...
  ],
  "total": 9,
  "endCursor": "YXJyYXk6OA=="
}

```



Once the export status updates to COMPLETED, which indicates a successful operation, a one-time download key is generated in downloadKey. Save this key from the response.
