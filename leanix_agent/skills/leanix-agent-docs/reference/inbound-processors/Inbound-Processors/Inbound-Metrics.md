##  Inbound Metrics
The inboundMetrics processor is used to write a single new point to a configured metrics endpoint.
The update section of the processor must contain the following keys with values:
Required Attribute | Description
---|---
measurement | Name of the configured metrics measurement a points needs to be added to
time | The date and time of the point in ISO formatting (e.g. 2019-09-09T08:00:00.000000Z)
fieldKey | Name of the field to store the point value in
fieldValueNumber | The value you want to store for that field and point of time
tagKey | Name of the tag
tagValue | Value of the tag. You may want to write the internal ID of a specific Fact Sheet here to allow assignment of the data to a specific Fact Sheet as a rule in the created chart for the measurement (go to admin/metrics to configure)


The output section of the inboundMetrics data processor should be configured the same as other inbound processors. The keys will be written to the corresponding variables.
Example inboundMetrics processor:

```
{
  "processorType": "inboundMetrics",
  "processorName": "Metrics data for measurement",
  "processorDescription": "Metrics processor configuration",
  "filter": {
    "exactType": "Metrics",
    "advanced": "${data.measurement.equals('measurement')}"
  },
  "run": 1,
  "updates": [
    {
      "key": {
        "expr": "measurement"
      },
      "values": [
        {
          "expr": "${data.measurement}"
        }
      ]
    },
    {
      "key": {
        "expr": "time"
      },
      "values": [
        {
          "expr": "${data.time}"
        }
      ]
    },
    {
      "key": {
        "expr": "fieldKey"
      },
      "values": [
        {
          "expr": "${data.fieldKey}"
        }
      ]
    },
    {
      "key": {
        "expr": "fieldValueNumber"
      },
      "values": [
        {
          "expr": "${data.fieldValueNumber}"
        }
      ]
    },
    {
      "key": {
        "expr": "tagKey"
      },
      "values": [
        {
          "expr": "${data.tagKey}"
        }
      ]
    },
    {
      "key": {
        "expr": "tagValue"
      },
      "values": [
        {
          "expr": "${data.tagValue}"
        }
      ]
    },
    {
      "key": {
        "expr": "tags"
      },
      "values": [
        {
          "map": [
            {
              "key": "key",
              "value": "${data.tagKey}_1"
            },
            {
              "key": "value",
              "value": "${data.tagValue}_1"
            }
          ]
        },
        {
          "map": [
            {
              "key": "key",
              "value": "${data.tagKey}_2"
            },
            {
              "key": "value",
              "value": "${data.tagValue}_2"
            }
          ]
        }
      ]
    }
  ],
  "logLevel": "debug"
}
```



