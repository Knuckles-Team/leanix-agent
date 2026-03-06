##  Example: Nested forEach
Using all three options to iterate with "forEach" functionality, Integration API now allows to ingest data in LDIF where data structures are nested up to three levels.
Example configuration of "inner forEach":

```
{
 "key": {
  "expr": "targetITComponents"
 },
 "mode": "list",
 "values": [
  {
   "forEach": {
    "elementOf": "${lx.relations}",
    "filter": "${true}"
   },
   "map": [
    {
     "key": "id",
     "value": "${integration.output.valueOfForEach.target.id}"
    },
    {
     "key": "type",
     "value": "${integration.output.valueOfForEach.target.type}"
    },
    {
     "key": "name",
     "value": "${integration.output.valueOfForEach.target.displayName}"
    }
   ]
  }
 ]
}
```



Given the processor was configured to read relations (read section) and put the results into a list "lx-relations", the above example of an outboundFactsheet processor, will output all relation results into an array as value of a key named "targetITCmponents".
Please note that admins may configure the filter JUEL expression evaluating to boolean in order to not have some of the input list elements in the output. The JUEL may contain references to "integration.output.valueOfForEach" and filter on any content.
A third option to iterate using "forEach" is to add the key at the level of "updates". It allows to create a dynamic set of field updates to be pushed to e.g. a Fact Sheet. In the below example the fields to be updated will be read from the incoming LDIF. In order to execute the example, the referenced Fact Sheet needs to already exist. Most easy way is to one time execute the "starter example" configuration on the workspace.
