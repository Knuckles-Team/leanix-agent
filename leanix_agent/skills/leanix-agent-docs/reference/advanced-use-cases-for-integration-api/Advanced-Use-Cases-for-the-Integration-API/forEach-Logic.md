##  forEach Logic
Each data processor provides additional capabilities to handle values that are lists. Using the standard functionality, every data processor will be executed exactly one time for each data object sent to the Integration API.
Sometimes however, there is a need to update multiple Fact Sheets or multiple fields in a Fact Sheet for each value we find in a list of values found in the LDIF.
Iterate over lists in Data Processor Configuration:

```
{
 "data": {
  "attachedDocuments": [
   {
    "extension": "vsdx",
    "name": "thediagram.vsdx",
    "displayName": "Diagram",
    "url": "sotrage.azure.com/123/thediagram.vsdx",
    "content": null
   },
   {
    "extension": "docx",
    "name": "thedoc.docx",
    "displayName": "Documentation",
    "url": "sotrage.azure.com/123/thedoc.docx",
    "content": null
   },
   {
    "extension": "html",
    "name": "webpage.html",
    "displayName": "Web Page",
    "url": null,
    "content": "<body>the vm 789 ...</body>"
   }
  ],
  "version": "1.8.4",
  "myForEachField": "attachedDocuments",
  "maturity": "3",
  "note": "I did the first comment here",
  "Home Country": "D",
  "Other Country": "UK",
  "clusterName": "leanix-westeurope-int-aks"
 }
}
```



inboundFactSheet ForEach example:

```
{
 "processorType": "inboundFactSheet",
 "processorName": "Deployment To Application",
 "processorDescription": "The processor creates or updates an Application from every data object of type 'Deployment'",
 "type": "Application",
 "name": "My Awesome App",
 "run": 0,
 "enabled": true,
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
 "filter": {
  "exactType": "Deployment"
 },
 "forEach": "${data.myForEachField}",
 "updates": [
  {
   "key": {
    "expr": "name"
   },
   "values": [
    {
     "expr": "${data.attachedDocuments[integration.indexOfForEach].name}",  // or in short: ${integration.valueOfForEach.name}, remove this comment before trying
     "regexReplace": {
      "match": "",
      "replace": ""
     }
    },
    {
     "expr": "${data.value}"
    }
   ]
  }
 ]
}
```



Using the "forEach" section in each data processor as in the example above. Will result in executing the data processor "Deployment To Application" four times for the given data object and each run will allow the user to use the index of the current iteration in all expressions (integration.indexOfForEach).
To fill some output field of the data processor with the specific url (see example above), the configuration would look like this: ${data.attachedDocuments[integration.indexOfForEach].name}. This will generate the three different names of the attached documents in each run of the data processor. This could be used to create separate Fact Sheets and relations from the source data.
There is another way to access the value of the element referenced by the current index:
${integration.valueOfForEach}
Which is the same as:
${data.attachedDocuments[integration.indexOfForEach].name}
The index variable however can be used to reference the same index of another list element e.g. Important note: The admin can configure a "regexReplace" section in the forEach section. This will allow to manipulate the JSON representation of the value object resulting from the expression. In case such a manipulation is configured, it will have impact on the "integration.valueOfForEach" and not alter the original data one may reference using the indexOfForEach variable in the original data and reference manually.
Of course, the logic could be used to always execute a data processor n times. Just add '[1,2,3]' as configuration and the data processor will execute three times with the index variable integration.indexOfForEach set to 0-2 for reference.
In case the field 'attachedDocuments' is not available or contains an empty list, the data processor will not execute (operate on an empty list). In case the url is a single value and no list, the data processor will execute once.
The Integration API allows to iterate over list values and map values. In case of iterating over a map, indexOfForEach will always return -1 as maps are not sorted. For maps there is an additional variable "keyOfForEach" available providing access to the name of the key. The value will be accessed with "valueOfForEach"
