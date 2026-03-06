##  Retrieving All Diagrams
To retrieve all diagrams that you have access to, make a GET request to the following API endpoint:

```
https://{SUBDOMAIN}.leanix.net/services/pathfinder/v1/bookmarks
```



To explore the endpoint schema, navigate to the [OpenAPI Explorer![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fapp.leanix.net%2Fopenapi-explorer%2F%23%2Fbookmarks%2FgetBookmarks "https://app.leanix.net/openapi-explorer/#/bookmarks/getBookmarks").
The following table contains the input parameters:
Parameter | Parameter Type | Data Type | Required | Description
---|---|---|---|---
bookmarkType | Query | String | Required | The type of the bookmark to retrieve. For diagrams, pass VISUALIZER. For a list of possible values, see [Bookmarks](https://help.sap.com/docs/leanix/ea/bookmarks?locale=en-US&state=PRODUCTION&version=CLOUD "Manage saved searches, reports, diagrams, and dashboards through the Pathfinder REST API.").
oDataOnly | Query | Boolean | Optional | Determines whether to return only bookmarks for which the Open Data Protocol (OData) is enabled. OData is not supported for diagrams.
groupKey | Query | String | Optional | The key used to separate bookmarks within the same query type.


Example request:

```
curl -X 'GET' \
  'https://{SUBDOMAIN}.leanix.net/services/pathfinder/v1/bookmarks?bookmarkType=VISUALIZER' \
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
  "status": "OK",
  "type": "Bookmark",
  "data": [
    {
      "id": "2452d5e1-ee8b-4b7c-b7f6-7af8bc4b9a73",
      "userId": "00000000-1111-4000-2222-000000000001",
      "name": "Dataflow w/ Data Objects",
      "type": "VISUALIZER",
      "groupKey": "dataflow",
      "state": {
        "graphXml": "<mxGraphModel grid=\"1\" gridSize=\"10\" guides=\"1\" tooltips=\"1\" connect=\"0\" fold=\"1\" page=\"0\" pageScale=\"1\" pageWidth=\"826\" pageHeight=\"1169\"><root><lx-settings layout=\"horizontalFlow\" relationLabels=\"interfaceTechnology,businessObjects\" id=\"0\"><mxCell/></lx-settings><mxCell id=\"1\" parent=\"0\"/><object type=\"factSheet\" autoSize=\"1\" layoutType=\"auto\" ...",
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
      "updatedAt": "2023-09-27T18:10:51.185149Z",
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
      "views": 11,
      "replaySequence": 6,
      "temporary": false,
      "oDataEnabled": false
    },
    {...}
  ],
  "total": 4
}
```



