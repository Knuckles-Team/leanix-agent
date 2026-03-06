##  Writing Variables using Expressions
The following example shows how to write variables using expressions to define names and values.

```
{
 "variables": [
  {
   "key": "prefix_§{dataMyNameFromDataObjectValue}",
   "value": "${data.myValueFromDataObject}"
  }
 ]
}
```



Below is an example of a processor with a matching LDIF that shows how variables work. In the first run which is marked by the processor with "run": 0, the variable section can be called on with the key aggregatedCosts and gathers together all the costs in the data section of each entry of an LDIF that is gathered by the filter in place. In this case, that filter is a Fact Sheet of type ITComponent. In the next run marked with "run": 1, the processor is calling the sum function on the variable aggregatedCosts and writing the sum to the description field of the Fact Sheets that fall under the specified filter, which in this case is all the Applications in the LDIF.
The example's result is three Fact Sheets created, two IT Components, and one Application with a description of 11. Note that the costs of the IT Components were not written in the IT Component's Fact Sheets.
Using variables in processors:

```
{
 "processors": [
  {
   "processorType": "inboundFactSheet",
   "processorName": "Create IT Components",
   "processorDescription": "One Processor for IT Components",
   "enabled": true,
   "type": "ITComponent",
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
   "filter": {
    "exactType": "ITComponent"
   },
   "updates": [
    {
     "key": {
      "expr": "name"
     },
     "values": [
      {
       "expr": "${data.name}"
      }
     ]
    }
   ],
   "variables": [
    {
     "key": "aggregatedCosts",
     "value": "${data.cost}"
    }
   ]
  },
  {
   "processorType": "inboundFactSheet",
   "processorName": "Create Applications",
   "processorDescription": "Aggregated IT Costs in Application's Description",
   "enabled": true,
   "type": "Application",
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
   "run": 1,
   "filter": {
    "exactType": "Application"
   },
   "updates": [
    {
     "key": {
      "expr": "name"
     },
     "values": [
      {
       "expr": "${data.name}"
      }
     ]
    },
    {
     "key": {
      "expr": "description"
     },
     "values": [
      {
       "expr": "${variables.aggregatedCosts.sum()}"
      }
     ]
    }
   ]
  }
 ],
 "variables": {}
}
```



Sample LDIF:

```
{
  "connectorType": "ee",
  "connectorId": "Kub Dev-001",
  "connectorVersion": "1.2.0",
  "lxVersion": "1.0.0",
  "content": [
    {
      "type": "ITComponent",
      "id": "itc1",
      "data": {
        "name": "IT1",
        "cost": 5
      }
    },
    {
      "type": "ITComponent",
      "id": "itc2",
      "data": {
        "name": "IT2",
        "cost": 6
      }
    },
    {
      "type": "Application",
      "id": "app",
      "data": {
        "name": "My App"
      }
    }
  ]
}
```



