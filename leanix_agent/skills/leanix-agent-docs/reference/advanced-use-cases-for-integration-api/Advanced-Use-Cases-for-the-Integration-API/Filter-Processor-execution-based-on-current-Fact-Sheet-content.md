##  Filter Processor execution based on current Fact Sheet content
Using the onRead filter in an inbound processor allows to execute a processor based on currently existing Fact Sheets. The processor can be configured to only execute if a Fact sheet already exists or if the Fact sheet has defined values in some fields.
Or exactly the other way round: The Processor may only be executed if the Fact Sheet does not yet exist.
The following Example shows a Processor that will execute if a Fact Sheet exists that has a defined name and is flagged with a certain Tag. It adds " (Cloud)" to the name of a Fact Sheet if current the name is exactly as defined in the data object and a tag "Public Cloud" in a tag group "Cloud Transformation" is set on the Fact Sheet.
Processor configuration to demonstrate the onRead filter:
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
    "exactType": "Deployment",
    "onRead": "${lx.factsheet.name==data.name && lx.tags.size()>0 && lx.tags[0].name=='Public Cloud'}"
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
   "updates": [
    {
     "key": {
      "expr": "name"
     },
     "values": [
      {
       "expr": "${lx.factsheet.name} (Cloud)"
      }
     ]
    }
   ],
   "logLevel": "debug",
   "read": {
    "fields": [
     "name"
    ],
    "tags": {
     "groups": [
      "Cloud Transformation"
     ]
    }
   }
  }
 ]
}
```



**Caution**
The onRead filter is only available for inbound processors. The outbound processor will ignore setting this filter configuration.
Functionality is available same way outbound however as it is possible to use read content in the "advanced" filter like e.g. "filter": {"advanced": "${lx.relations.size()>0}"}, for cases where you only want to export if any requested relation was found
**Note**
Order of RegEx execution.
Using the replace regEx will allow to modify the output after applying the match regEx
