##  Export Metrics
Integration API allows to export metrics information visible in a chart on a Fact Sheet to an LDIF file. This is advanced configuration and requires deeper understanding of Metrics data and configuration in SAP LeanIX. The Fact Sheet processor will contain one or more definitions to point to series of data points stored in the Metrics and displayed as a diagram attached to the Fact Sheet.
The configuration allows flexibility to customize the selection and aggregation of data points even different from the current display on the Fact Sheet as Integration API accesses the raw data not the processed data visible in the UI. Multiple data series as e.g. displayed on a stacked bar chart need to be configured as separate configurations in the processor and will be accessed separately when writing to the LDIF.
This example shows how to export Metrics data and needs to be adjusted to the defined metrics series in the workspace.
Multiple different configurations all need to define different values for the "name" key. This value is then used to access the collected data. Please use only characters that are supported by JUEL, avoid any special characters. In the example below "variableName" is used in the definition and then in the output section to access the data and write it to the LDIF.
  * "comparator" currently only supports "=" and intended for future extension.
  * "aggregationFunction" does support all standard influx aggregations supporting a column as parameter.


Example outboundFactsheet processor that exports metrics:

```
{
 "scope": {
  "ids": [
   "28fe4aa2-6e46-41a1-a131-72afb3acf256"
  ],
  "facetFilters": []
 },
 "processors": [
  {
   "processorType": "outboundFactSheet",
   "processorName": "Export to LDIF",
   "processorDescription": "This is an example how to use the processor",
   "enabled": true,
   "fields": [
    "lifecycle",
    "location",
    "createdAt",
    "technicalSuitabilityDescription",
    "description"
   ],
   "relations": {
    "filter": [
     "relToParent",
     "relApplicationToITComponent"
    ],
    "fields": [
     "description"
    ],
    "targetFields": [
     "displayName",
     "externalId"
    ],
    "constrainingRelations": false
   },
   "tags": {
    "groups": [
     "Other tags",
     "Cloud Transformation"
    ]
   },
   "subscriptions": {
    "types": [
     "RESPONSIBLE"
    ]
   },
   "documents": {
    "filter": ".*"
   },
   "metrics": [
    {
     "name": "variableName",
     "measurement": "money",
     "fieldName": "dollars_per_day",
     "aggregationFunction": "MEAN",
     "groupBy": "1h",
     "start": "2020-01-20T00:00:00Z",
     "duration": "P0DT24H30M",
     "rules": {
      "key": "factSheetId",
      "comparator": "=",
      "compareWith": "${lx.factsheet.id}"
     }
    }
   ],
   "output": [
    {
     "key": {
      "expr": "content.id"
     },
     "values": [
      {
       "expr": "${lx.factsheet.id}"
      }
     ]
    },
    {
     "key": {
      "expr": "content.type"
     },
     "values": [
      {
       "expr": "${lx.factsheet.type}"
      }
     ]
    },
    {
     "key": {
      "expr": "values"
     },
     "values": [
      {
       "expr": "${integration.toJson(lx.metrics.variableName.values)}"
      }
     ],
     "optional": true
    },
    {
     "key": {
      "expr": "fields"
     },
     "values": [
      {
       "expr": "${integration.toJson(lx.metrics.variableName.fields)}"
      }
     ],
     "optional": true
    },
    {
     "key": {
      "expr": "series"
     },
     "values": [
      {
       "expr": "${integration.toJson(lx.metrics.variableName.series)}"
      }
     ],
     "optional": true
    },
    {
     "key": {
      "expr": "metrics"
     },
     "mode": "list",
     "values": [
      {
       "forEach": {
        "elementOf": "${lx.metrics.variableName.series}",
        "filter": "${true}"
       },
       "map": [
        {
         "key": "time",
         "value": "${integration.output.valueOfForEach.time}"
        },
        {
         "key": "value",
         "value": "${integration.output.valueOfForEach.values}"
        }
       ]
      }
     ]
    }
   ]
  }
 ]
}

```



