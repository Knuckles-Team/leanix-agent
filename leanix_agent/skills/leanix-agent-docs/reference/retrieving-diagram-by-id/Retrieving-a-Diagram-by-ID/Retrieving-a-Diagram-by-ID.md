##  Retrieving a Diagram by ID
To retrieve a specific diagram that you have access to by its ID, make a GET request to the following API endpoint:

```
https://{SUBDOMAIN}.leanix.net/services/pathfinder/v1/bookmarks/{id}
```



To explore the endpoint schema, navigate to the [OpenAPI Explorer![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fapp.leanix.net%2Fopenapi-explorer%2F%23%2Fbookmarks%2FgetBookmark "https://app.leanix.net/openapi-explorer/#/bookmarks/getBookmark").
The following table contains the input parameters:
Parameter | Parameter Type | Data Type | Required | Description
---|---|---|---|---
id | Path | String | Required | The ID of the diagram to retrieve. To get the diagram ID, retrieve all diagrams and save the id of the desired diagram from the response. In the application user interface, you can navigate to the diagram page and copy the ID from the URL.
markAsViewed | Query | Boolean | Optional | Determines whether to mark the diagram as viewed upon executing the request. If true, the value of the views parameter is increased by one. Defaults to true if not specified.


Example request:

```
curl -X 'GET' \
  'https://{SUBDOMAIN}.leanix.net/services/pathfinder/v1/bookmarks/2452d5e1-ee8b-4b7c-b7f6-7af8bc4b9a73' \
  -H 'accept: application/json' \
  -H 'authorization: Bearer {ACCESS_TOKEN}'
```



The state attribute in the response contains the diagram layout and filters.
Example response:

```
{
  "data": {
    "id": "2452d5e1-ee8b-4b7c-b7f6-7af8bc4b9a73",
    "userId": "00000000-1111-4000-2222-000000000001",
    "name": "Dataflow w/ Data Objects",
    "type": "VISUALIZER",
    "groupKey": "dataflow",
    "state": {
      "graphXml": "<mxGraphModel grid=\"1\" gridSize=\"10\" guides=\"1\" tooltips=\"1\" connect=\"0\" fold=\"1\" page=\"0\" pageScale=\"1\" pageWidth=\"826\" pageHeight=\"1169\"><root><lx-settings layout=\"horizontalFlow\" relationLabels=\"interfaceTechnology,businessObjects\" id=\"0\"><mxCell/></lx-settings><mxCell id=\"1\" parent=\"0\"/><object type=\"factSheet\" autoSize=\"1\" layoutType=\"auto\"...",
      "viewport": {
        "scale": 1,
        "translate": {
          "x": 0,
          "y": 0
        }
      }
    },
    "workingCopy": null,
    "description": "",
    "createdAt": "2019-03-20T15:59:54.714Z",
    "updatedAt": "2024-01-05T11:51:50.876878Z",
    "i18nKey": null,
    "predefined": true,
    "readonly": false,
    "defaultSharingPriority": 20,
    "user": {...},
    "permittedReadUserIds": [],
    "permittedWriteUserIds": [],
    "referencedFactSheetIds": [
      "a0197ca7-e614-4e93-d89f-82dd28ef819a",
      "26be83c4-2b7f-479e-e5f3-ef0006db54ba",
      ...
    ],
    "views": 12,
    "replaySequence": 6,
    "temporary": false,
    "oDataEnabled": false
  },
  "status": "OK",
  "type": "Bookmark"
}
```



YesNo
Send
