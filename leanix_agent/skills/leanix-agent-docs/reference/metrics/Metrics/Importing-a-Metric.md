##  Importing a Metric
To import your first metric, go to the [OpenAPI Explorer![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fapp.leanix.net%2Fopenapi-explorer%2F%3Furls.primaryName%3DMetrics "https://app.leanix.net/openapi-explorer/?urls.primaryName=Metrics"). To navigate to the OpenAPI Explorer from your workspace, on the navigation bar, select About SAP LeanIX on the Help menu (question mark icon), then select Browse API.
You need to generate an API Token by using the [Technical User](https://help.sap.com/docs/leanix/ea/technical-users?locale=en-US&state=PRODUCTION&version=CLOUD "To get an API token, create a technical user. Manage technical users collaboratively with other administrators.") functionality and enter it on the top right to execute queries directly from the API documentation.
You can explore the full list of endpoints and associated operations in the OpenAPI Explorer.
Use this code snippet as body to POST /schemas to create a new schema named "My First Metric":

```
{
  "name": "My First Metric",
  "description": "This is a test metric for SAP LeanIX EAM docs",
  "attributes": [
    {
      "name": "Availability",
      "type": "metric"
    },
    {
      "name": "factSheetID",
      "type": "dimension"
    }
  ]
}

```



This call will return the UUID of the newly created schema. Then write a point to this schema by sending a POST request to /schemas/<schema_uuid>/points with the following body:

```
{
  "timestamp": 1621608440,
  "Availability": 100,
  "factSheetID": "<your Fact Sheet ID>"
}

```



You need to adapt to your context. Now, go to Admin -> Metrics, and you should see the first measurement.
