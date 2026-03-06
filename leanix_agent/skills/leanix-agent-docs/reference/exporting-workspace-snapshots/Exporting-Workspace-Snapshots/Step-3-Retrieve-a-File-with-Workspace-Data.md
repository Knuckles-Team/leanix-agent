##  Step 3: Retrieve a File with Workspace Data
With the downloadKey of the export, you can retrieve an XLSX file with workspace data. The downloadKey is a single-use key, valid for one download only. workspaceId is a required parameter for this request.
To retrieve a file with workspace data, make a GET request to the following endpoint:

```
https://{SUBDOMAIN}.leanix.net/services/pathfinder/v1/exports/downloads/{workspaceId}
```



Example request:

```
curl -X 'GET' \
  'https://{SUBDOMAIN}.leanix.net/services/pathfinder/v1/exports/downloads/b7d533f1-4aa0-4132-92c6-a390a60cbghf?key=cf1d1f70-539e-4207-acf0-64d2955007d7' \
  -H 'accept: application/octet-stream' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}'
```



An XLSX file is returned in the response.
