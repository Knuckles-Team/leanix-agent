##  Step 1: Initiate an Export Job
To get started, initiate an export job by making a POST request to the following endpoint on the [Pathfinder REST API![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fapp.leanix.net%2Fopenapi-explorer%2F%3Furls.primaryName%3DPathfinder "https://app.leanix.net/openapi-explorer/?urls.primaryName=Pathfinder"):

```
https://{SUBDOMAIN}.leanix.net/services/pathfinder/v1/exports/fullExport
```



Use the exportType query parameter to specify the export type:
  * SNAPSHOT: Full snapshot of the workspace data that includes information from all active fact sheets, as well as information about related objects such as relations, tag groups, tags, resources (also referred to as documents), and comments. The snapshot doesn't include archived fact sheets. In the application UI, this export type appears as Full Snapshot.
  * AUDIT_LOG: Data-related changes made to the workspace within a specified time frame. The default time frame is 30 days. In the application UI, this export type appears as Changelog.
  * ARCHIVE: Full snapshot of the archived workspace data that includes information from all archived fact sheets, as well as information about related objects such as relations, tag groups, tags, resources (also referred to as documents), and comments. You can use this export option to view archived fact sheets before they are deleted at the end of the retention period. For more information, see [Archiving, Deleting and Recovering Fact Sheets](https://help.sap.com/docs/leanix/ea/archiving-deleting-and-recovering-fact-sheets?locale=en-US&state=PRODUCTION&version=CLOUD "Learn to archive fact sheets individually or in bulk and effortlessly view or recover archived fact sheets in SAP LeanIX.").


Example request:

```
curl -X 'POST' \
  'https://{SUBDOMAIN}.leanix.net/services/pathfinder/v1/exports/fullExport?exportType=SNAPSHOT' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -d ''
```



Example response:

```
{
  "status": "OK",
  "type": "JobResponseData",
  "data": {
    "jobId": "job:374234:cmbf4fdiozzp8q7m4u0dc1jss",
    "message": "A new job is queued.",
    "synclogId": null
  }
}
```



The OK status in the response indicates that an export job is initiated.
