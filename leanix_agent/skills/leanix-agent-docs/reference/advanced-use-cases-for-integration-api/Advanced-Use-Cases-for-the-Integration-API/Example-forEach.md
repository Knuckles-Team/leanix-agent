##  Example: forEach
Sample LDIF with a map:

```
{
 "connectorType": "ee",
 "connectorId": "Kub Dev-001",
 "connectorVersion": "1.2.0",
 "lxVersion": "1.0.0",
 "content": [
  {
   "type": "Deployment",
   "id": "634c16bf-198c-1129-9d08-92630b573fbf",
   "data": {
    "app": "HR Service",
    "version": "1.8.4",
    "myList": [
     "lValue1",
     "lValue2"
    ],
    "myMap": {
     "key1": "value1",
     "key2": "value2"
    }
   }
  }
 ]
}
```



Iterate over maps:

```
{
  "processors": [
    {
      "processorType": "inboundFactSheet",
      "processorName": "Apps from Deployments",
      "processorDescription": "Creates LeanIX Applications from Kubernetes Deployments",
      "type": "Application",
      "filter": {
        "exactType": "Deployment"
      },
      "identifier": {
        "external": {
          "id": {
            "expr": "${content.id}"
          },
          "type": {
            "expr": "externalId"
          }
        }
      },
      "run": 0,
      "updates": [
        {
          "key": {
            "expr": "name"
          },
          "values": [
            {
              "expr": "${data.app}"
            }
          ]
        },
        {
          "key": {
            "expr": "description"
          },
          "values": [
            {
              "expr": "${integration.keyOfForEach}: ${integration.valueOfForEach}"
            }
          ]
        }
      ],
      "forEach": "${data.myMap}",
      "logLevel": "debug"
    }
  ]
}
```



For each logic can as well be applied inside the value section for and update key. The list or map will be iterated and the values result will contain n entires that are then mapped to the defined key. Please ensure to set the mode to "list" if not only the first value is to be used as a result (default mode for every key in the update section of a processor is "selectFirst" to only take the first non null result from what was defined in the values array. The "inner forEach" is behaving exactly as if the admin defined a fix number of elements in the "values" section.
