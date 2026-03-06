##  Setting Filters
Filter section is where you define if the Data Processor should work on the found data object. It can be set to null to indicate no filter is being provided.
Example outbound processor with filters:

```
{
 "scope": {},
 "processors": [
  {
   "processorType": "outboundFactSheet",
   "processorName": "User Groups that Begin with Br",
   "processorDescription": "",
   "filter": {
    "advanced": "${lx.factsheet.name.startsWith('Br')}"
   }
  }
 ]
}
```



Filter Type | Details
---|---
type | If configured, the string is interpreted as a regular expression and matched against the "type" of the Fact Sheet
id | If configured, the string is interpreted as a regular expression and matched against the "id" d of the Fact Sheet
advanced | If configured, the field contains a JUEL expression that may evaluate to "true" for a match or "false". This filter allows to filter even for combinations of certain key and values in the Fact Sheet


**Note**
Data Processors provide filter capabilities to configure on which Data Object the data processor will work on (match the filter) and what Data Objects to skip (not match the filter)
Below example also includes the option to modify the choices as per external System.
Example single outbound processor:

```
{
 "processorType": "outboundFactSheet",
 "processorName": "<Unnamed processor>",
 "processorDescription": "",
 "filter": null,
 "enabled": true,
 "fields": [
  "nonExistingField",
  "lifecycle",
  "location",
  "createdAt",
  "businessCriticality",
  "technicalSuitabilityDescription"
 ],
 "output": [
  {
   "key": {
    "expr": "content.id"
   },
   "mode": "selectFirst",
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
   "mode": "selectFirst",
   "values": [
    {
     "expr": "${lx.factsheet.type}"
    }
   ]
  },
  {
   "key": {
    "expr": "lifecycle.times"
   },
   "mode": "list",
   "values": [
    {
     "expr": "${lx.factsheet.lifecycle.endOfLife}"
    },
    {
     "expr": "${lx.factsheet.lifecycle.active}"
    },
    {
     "expr": "${lx.factsheet.lifecycle.phaseOut}"
    },
    {
     "expr": "${lx.factsheet.lifecycle.phaseIn}"
    }
   ]
  },
  {
   "key": {
    "expr": "location"
   },
   "mode": "selectFirst",
   "values": [
    {
     "expr": "${lx.factsheet.location.rawAddress}, with place id: ${lx.factsheet.location.placeId}"
    }
   ]
  },
  {
   "key": {
    "expr": "businessCriticality"
   },
   "values": [
    {
     "expr": "${lx.factsheet.businessCriticality}",
     "regexMatch": "administrativeService",
     "regexReplace": {
      "match": "^.*$",
      "replace": "Administrative Service"
     }
    },
    {
     "expr": "${lx.factsheet.businessCriticality}",
     "regexMatch": "businessOperational",
     "regexReplace": {
      "match": "^.*$",
      "replace": "Business Operational"
     }
    }
   ]
  },
  {
   "key": {
    "expr": "creationTime"
   },
   "mode": "selectFirst",
   "values": [
    {
     "expr": "${lx.factsheet.createdAt}"
    }
   ]
  },
  {
   "key": {
    "expr": "technicalSuitabilityDescription"
   },
   "mode": "selectFirst",
   "values": [
    {
     "expr": "${lx.factsheet.technicalSuitabilityDescription}"
    }
   ]
  }
 ]
}
```



