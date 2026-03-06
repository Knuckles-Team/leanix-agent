##  Using "Integration" Object
Expression | Details | More Examples
---|---|---
"${integration.now}" | Contains the information about the date and time the synchronization run started. "integration.now" contains a Java LocalDateTime object and allows to call methods with parameters of types String or long. E.g. | integration.now.plusHours(1) would return an object showing date and time UTC plus one hour. Content like the date of last sync can be made visible in any SAP LeanIX field like this "Last sync: ${integration.now.getMonth}.${integration.now.getDayOfMonth()}.${integration.now.getYear()}". The values can be used for filtering and/or to write date and time to the output of a data processor.
"${integration.contentIndex}" | Contains the index number of the currently processed data object. This could be used to e.g. create a filter for a data processor to always run for the first data object of a synchronization run. |
"${integration.maxContentIndex}" | Contains the contentIndex of the last data object in scope of the sync run. Matching this in an advanced filter for a data processor would ensure the processor only runs e.g. when processing the last data object. |
"${integration.toJson(data.Properties)}" | Offers a helper method to convert any given section from the LDIF (data.Properties in the example) into a valid JSON string. The JSON can be used to be rendered in a Fact Sheet without any option to search but dump arbitrary data. |
"${integration.toObject(data.Properties)}" | The opposite of "toJson". The method converts any Json String back to the corresponding object representation. This might be lists or maps e.g.. | Given a String "{"key1":"value1"}" (a serialized JSON) in a data property 'json'. The method "${integration.toObject(data.json).key1}" will provide "value1" as the result string after evaluating the JUEL expression
${helper:toActiveLifecyclePhase(lx.factsheet.lifecycle, integration.now)}" | Offers a helper method to read the name of the lifecycle phase at a given point of time. Potential parameter for the current date may be "integration.now" |  "${helper:toActiveLifecyclePhase(lx.factsheet.lifecycle, '2020-02-01'}"  "${helper:toActiveLifecyclePhase(lx.factsheet.lifecycle, integration.now)}" Note: In case custom lifecycle phases are defined, pleases use the "helper:toActiveLifecyclePhaseOrdered" function to ensure ordering when lifecycle phases occure on the same date.
${helper:toActiveLifecyclePhaseOrdered(lx.factsheet.lifecycle, integration.now, helper:toList("planned","phaseIn","active","phaseOut","endOfLife"))}" | Same as "helper:toActiveLifecyclePhase" with an additonal parameter to define the order of the phases. |  "${helper:toActiveLifecyclePhaseOrdered(lx.factsheet.lifecycle, integration.now, helper:toList("phase1","phase2","phase3"))}"
"${helper:toList('default','optionHighPrio','optionMediumPrio','optionLowPrio')}" | Converts a set of strings into a list to be used as parameters in a java String method | This works as well if an array is passed to the helper: helper:toList(myString.split(','))
integration.processing.* | The methods sum(), distinct(), average(), max(), min(), and getNumbers() allow to operate on every list in the JUEL scope in order to aggregate data and work with all lists in a way that is already supported for variables | Even chaining like data.myvalueWithAList.getNumbers().distinct().size() works to e.g. find out how many different number values are in a given input list.
integration.processing.mergeList(firstList, secondList) | The method merges two source lists and can be used to iterate over all values in multiple different input lists using one forEach loop | Even merging multiple lists is possible by nesting the calls
integration.tags.getTagGroupId(tagGroupName}" | Allows to resolve internally used tag group ids from their external name | The conversion is used in search based scope filters to allow Filters based on tag names their name and not their internal IDs. Internal IDs are not exposed easily and will change from workspace to workspace
integration.tags.getTagId(tagGroupName,tagName) | Allows to resolve internally used tag ids from their external name | The conversion is used in search based scope filters to allow Filters based on tag names their name and not their internal IDs. Internal IDs are not exposed easily and will change from workspace to workspace
integration.tags.getAllTagGroups() | Allows to work with an object containing all tag groups and all tags defined in the workspace | See example configuration "Export all tag groups" below this table
helper:localDateTimeFromString(‘2016-03-04 11:30’, ‘yy-MM-dd HH:mm’, ‘yyyy-MM-dd HH:mm’) | Returns a LocalDateTime object representing the time 2016-03-04 11:30 |  Can be used to convert any input string into a localDateTime object. The object and available Java methods can then be used in the JUEL expression. See Java documentation:
  * [LocalDateTime![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fdocs.oracle.com%2Fen%2Fjava%2Fjavase%2F11%2Fdocs%2Fapi%2Fjava.base%2Fjava%2Ftime%2FLocalDateTime.html?locale=en-US&state=PRODUCTION&version=CLOUD "https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/time/LocalDateTime.html")
  * [SimpleDateFormat![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fdocs.oracle.com%2Fen%2Fjava%2Fjavase%2F11%2Fdocs%2Fapi%2Fjava.base%2Fjava%2Ftext%2FSimpleDateFormat.html?locale=en-US&state=PRODUCTION&version=CLOUD "https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/text/SimpleDateFormat.html")


helper:localDateTimeToString(integration.now, ‘yy-MM-dd HH:mm’) | Returns a string “20-07-02 11:30". The helper allows to convert any localDateTime object back to a string in the required format | See Java documentation for string pattern description: [SimpleDateFormat![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fdocs.oracle.com%2Fen%2Fjava%2Fjavase%2F11%2Fdocs%2Fapi%2Fjava.base%2Fjava%2Ftext%2FSimpleDateFormat.html?locale=en-US&state=PRODUCTION&version=CLOUD "https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/text/SimpleDateFormat.html")
helper:getDuration(localDateTime,localDateTime) | Returns a Duration object to allow flexible work with the result. See java documentation to Duration class methods. Parameters can be the return of the localDateTimeFromString or integration.now as well as localDateTimeObjects returned by other methods called. | The helper will be used to calculate time differences between two points of time. Writing the age in days to a field is one potential use case. See the Java documentation for methods on the returned "duration" object: [Duration![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fdocs.oracle.com%2Fen%2Fjava%2Fjavase%2F11%2Fdocs%2Fapi%2Fjava.base%2Fjava%2Ftime%2FDuration.html?locale=en-US&state=PRODUCTION&version=CLOUD "https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/time/Duration.html")
math:nameOfTheMethod | calculates abs, round and other functions always on the highest available precision (double). In case a method returns a double, users can add ". intValue()" to convert to an integer for display purposes or to push to an integer field | For details on supported methods see the Oracle Java documentation.
lx.toOrdinal('fieldName') | returns the position of the currently set value for a SINGLE_SELECT field. This allows to do calculations on SINGLE_SELECT fields given the order of the select options reflect a kind of order like "low", "medium", "high" would be returned as 0, 1, 2 | See the configuration example "Calculating with single select fields" below this table. Please be aware that the fields to be used need to be defined as fields in the "read"-section of the processor as shown in the example.
helper:getFromMap(myMap,myKeyInTheMapAsString) | returns the object referenced by the specified key in the provided map. The helper can be used to access keys with spaces like a map containing a key names "my Important Value", which cannot be referenced by dot Syntax. | The helper allows to avoid [] syntax to access elements of a map where dot syntax is not possible. E.g. in cases where the map is "variables" and the name of the variable needs to be determined dynamically.


To test the below example, please change the id in "ids" to an existing internal id of a Fact Sheet in your workspace. You may just open a Fact Sheet and copy the id from the browser URL.
In real world scenarios, you may not want to export the whole object, but iterate over tag groups or export a subset of the information.
Example for exporting all tag groups:

```
{
 "scope": {
  "ids": [
   "869ee28b-c60a-4e88-8d18-f9e4ff466456"
  ],
  "facetFilters": []
 },
 "processors": [
  {
   "processorType": "outboundFactSheet",
   "processorName": "Export tag groups and tags",
   "processorDescription": "Sample how to export all available tag groups and all tags as part of one fact sheet export",
   "fields": [
    "name"
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
      "expr": "name"
     },
     "values": [
      {
       "expr": "${lx.factsheet.name}"
      }
     ]
    },
    {
     "key": {
      "expr": "tagGroupsAndTags"
     },
     "values": [
      {
       "object": "${integration.tags.getAllTagGroups()}"
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
A similar configuration will help gathering all tag groups where a specific Fact Sheet has tags set. The lx.tagGroups list will be filled with all tag groups where the Fact Sheet has at least one tag set. And inside each tag group element there will be a list of the found tags for the Fact Sheet. The below example filters and returns only a sub set (default tag group). Just adding "${true}" in the filter will ensure to return all tag groups and included tags the Fact Sheet has set.
Reading all tag groups for a fact sheet:

```
{
 "scope": {
  "ids": [
   "bb8b0b74-f737-4f1b-a937-a06bddf3fe47"
  ],
  "facetFilters": [
   {
    "keys": [
     "Application"
    ],
    "facetKey": "FactSheetTypes",
    "operator": "OR"
   }
  ]
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
     "SomeTagGroupName"
    ],
    "multipleGroups": "${dm.tagGroup.name =='Other tags'}"
   },
   "subscriptions": {
    "types": [
     "RESPONSIBLE"
    ]
   },
   "documents": {
    "filter": ".*"
   },
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
      "expr": "Description"
     },
     "values": [
      {
       "expr": "${integration.toJson(lx.tagGroups).toString()}"
      }
     ],
     "optional": true
    }
   ]
  }
 ]
}
```



