##  Dynamic definition of Fact Sheet fields to read
Sometimes it is helpful to decide at run time which fields from a Fact Sheet to read and not hard code the names of the fields in the configuration.
For this purpose, Integration API allows to define a key "multipleFields" and a value that is a JUEL expression and will be resolved to boolean true and false. The Integration API will iterate over all available fields taken from the data model and allow the expression to do any filter logic required. As input value, the currently iterated field can be used with "dm.factSheetField.name". The type of the field can be identified with "dm.factSheetField.type"
In following JUEL expressions like forEach or update section, the list of read fields can be used with dm.factSheetFields, which is an object with keys: name, type and factsheetType
The below example would read all fields of type "STRING" from a Fact Sheet.
Dynamic fact sheet fields:
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
   "read": {
    "multipleFields": "${dm.factSheetField.type=='STRING'}"
   },
   "updates": [
    {
     "key": {
      "expr": "${integration.valueOfForEach.name}"
     },
     "values": [
      {
       "expr": "${lx[integration.valueOfForEach.name]} - added by Integration API"
      }
     ]
    }
   ],
   "forEach": "${dm.factSheetFields}",
   "logLevel": "debug"
  }
 ]
}
```



In the sample, all String fields of the Fact Sheet get a string " - added by Integration API" appended.
multipleFields can be used for relations as well.
After evaluation of dynamic relation reading, fields dm.relationFilters[], lx.relationTargetFields[] and lx.relationFields[] are available.
Multiple fields on relations:

```
"multipleFields": "${data.fieldsToRead.contains(dm.relationField.name) && dm.relationField.type=='relToParent'}"

"multipleTargetFields": "${data.fieldsToRead.contains(dm.factSheetField.name) && dm.relationType=='relToParent'}"

"multipleFilters": "${data.myDynamicRelationList.contains(dm.relationType)}",
```



Same way, dynamic definition of Tags can happen: (after execution, the collected tag groups are available in a "lx.tagGroups" list.
In the filter "multipleGroups", the object of the currently iterated tag group "dm.tagGroup" can be used.
Dynamic tag group definition:

```
{
 "read": {
  "tags": {
   "multipleGroups": "${true}",
   "groups": [
    "Cloud Transformation"
   ]
  }
 }
}
```



**Note**
Availability of information read from the Fact Sheet.
Information read from the Fact Sheet is available in the output section. The information is not available in the outer forEach, in the identifier and the filter section. The reason for this is, that at the time when the content in these sections is evaluated, the target Fact Sheet is not yet identified.
