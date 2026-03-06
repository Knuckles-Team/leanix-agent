##  General Structure
### Filters
Filter section is where you define if the Data Processor should work on the found data object.
**Note**
Data Processors provide filter capabilities to configure on which Data Object the data processor will work on (match the filter) and what Data Objects to skip (not match the filter)
Types of filters that can be configured:
Filter Type | Details
---|---
exactType (type) |  The exactType and type filters work differently when comparing strings with the type field of a data object. The exactType filter requires an exact match between the string and the type field. This means the entire string must match the type field for the filter to be applied. We recommend using this filter type to ensure accurate matching. The type filter performs a comparison based on the first characters of the string, following the logic of a regular expression. This means the filter is applied if the initial characters of the string match the type field of the data object, without considering the remaining characters.
id | If configured, the string is interpreted as a regular expression and matched against the "id" field of the Data Object
advanced | If configured, the field contains a JUEL expression that may evaluate to "true" for a match or "false". This filter allows to filter even for combinations of certain key and values in the Data Object
onRead | Behaves like the advanced filter but uses results of eventually configured read sections to filter based on existence of a Fact Sheet or based on specific values on an existing Fact Sheet. You can find an example of how to use this filter in [Advanced Use Cases for the Integration API](https://help.sap.com/docs/leanix/ea/advanced-use-cases-for-integration-api?locale=en-US&state=PRODUCTION&version=CLOUD "Explore advanced scenarios and examples for the Integration API.").
writeToLdif | Using this processor, Administrators can configure an inbound Integration API run to write a new LDIF file. The resulting LDIF will be available using the /results and the /resultsUrl endpoints same as with outbound Integration API runs
updatedInDuration | Used to filter on items that have changed recently. Integration API can target Fact Sheets that have been changed recently. Only Fact Sheets that pass this criteria will be processed. The feature is most helpful to generate proper output with the "writeToLdif" processor that only contains e.g. Fact Sheets changed since last export. It is used the following way: "updatedInDuration": "P3D". You can find an example in [Outbound Processors](https://help.sap.com/docs/leanix/ea/outbound-processors?locale=en-US&state=PRODUCTION&version=CLOUD).


**Note**
All configured filters need to match in order to start the Data Processor on the Data Object (AND logic).
Example of combining multiple filters:

```
{
  "filters": {
    "exactType": "ITComponent",
    "updatedInDuration": "P3D"
  }
}
```



### Identifier Section
Identifier section defines the pathfinder entity in scope of the processor. Depending on the processor it can be called "identifier" (all processors with one Fact Sheet in scope) or "from" and "to" for the inboundRelation processor.
Identification of the target Fact Sheet happens by defining the internal ID, the external ID or a "search scope".
Only one field must be filled as a value of key "identifier":
  * internalId: JUEL expression, replace RegEx


Example of identification by an internal ID:

```
{
  "identifier": {
    "internal": "${content.id}"
  }
}
```



  * externalId: JUEL expression, replace RegEx (id/name of Fact Sheet or other entity)


Example of Identification by an external ID:

```
{
  "identifier": {
    "external": {
      "id": {
        "expr": "${content.id}"
      },
      "type": {
        "expr": "externalId"
      }
    }
  }
}
```



Using the external key, it is possible to create an object in case it is not found. This happens transparently without any need to distinguish between create or update when configuring the processor.
When using the "search" based identification of the Fact Sheet that are supposed to be updated by the incoming data object, then the section may contain a section to limit the scope of searched Fact Sheets and an expression filtering the Fact Sheets that should be updated. Details can be found on the "Advanced" page of this documentation.
The below processor will update all descriptions of Application Fact Sheets that have a tag "AsiaPacific" in the tag group "Region". The full example can be found on the "Advanced" page.
Example processor for identifying Fact Sheets using search and updating them with incoming data:

```
{
  "processors": [
    {
      "processorType": "inboundFactSheet",
      "processorName": "Update all Cloud Apps",
      "processorDescription": "Updates all Apps with tag 'Cloud'",
      "type": "Application",
      "filter": {
        "exactType": "AppUpdate"
      },
      "identifier": {
        "search": {
          "scope": {
            "facetFilters": [
              {
                "facetKey": "FactSheetTypes",
                "operator": "OR",
                "keys": [
                  "Application"
                ]
              },
              {
                "facetKey": "${integration.tags.getTagGroupId('Region')}",
                "operator": "OR",
                "keys": [
                  "${integration.tags.getTagId('Region','AsiaPacific')}"
                ]
              }
            ],
            "ids": []
          },
          "filter": "${true}",
          "multipleMatchesAllowed": true
        }
      },
      "logLevel": "debug",
      "updates": [
        {
          "key": {
            "expr": "description"
          },
          "values": [
            {
              "expr": "External sync executed ${data.dateTime}"
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
### Update Section
The Update Section provides the ability to write to fields or further metadata to the targeted entity (depending on the processor).
Multiple values can be written. Each value consists of a JUEL and a RegEx for building the name of the target key to be written and a list of potential values to be written.
Some keys might be mandatory depending on the processor (see the processor description for details).
The following field types in Fact Sheet fields can be updated (using the update section):
Attribute | Description
---|---
STRING | Is a basic text field with no functionality. This field has no configurable formatting like displaying clickable links or bold formatting
SINGLE_SELECT | Allows for the selection of one value from a dropdown list. This list of values can be changed at any point in time without data loss. This attribute can be filtered in the inventory and used as a view in the reports
MULTIPLE_SELECT | Allows for the selection of multiple values from a predefined list. Once defined this list cannot be changed again without incurring data loss
DOUBLE | There is no explicit currency field in SAP LeanIX, but this type can display a currency icon
INTEGER | Represents a numeric value without decimal places
LOCATION | Will be sent to the location service to resolve a valid location from the given input string. Setting the location will fail if the given data is not specific and results in multiple possible locations. In case a "#" is found as the first one, the API will pick the first result returned by the location service and use this. This is helpful if comma separated coordinates are being provided
LIFECYCLE | Content needs to follow the date format specifications "yyyy-mm-dd". Each field in the life cycle can be addressed with "."-syntax like e.g. lifecycle.active
EXTERNALID | External Ids can only be written if they are not marked readonly in the data model. The following fields can be written using "."-syntax: externalId.externalId, externalId.externalUrl, externalId.comment, externalId.status, externalId.externalVersion. The "externalId" left of the "." may be changed with the name of the external id field.
PROJECT |  Project status values will always written as a full set that replaces the currently set project status values. In order to add to existing values, you need to add the field to the read section. This returns an object you would then iterate over using inner forEach (see advanced section for usage). While iterating a filter could be applied to not write back all found status values but selected only. In addition by defining more values new values can be added in the same step. The structure of the required map can be copied from a read result (e.g. output to a description field for testing):   ```
{
  "updates": [
    {
      "key": {
        "expr": "projectStatus"
      },
      "values": [
        {
          "map": [
            {
              "key": "id",
              "value": "myId"
            },
            {
              "key": "date",
              "value": "2020-07-25"
            },
            {
              "key": "status",
              "value": "green"
            },
            {
              "key": "progress",
              "value": "20"
            }
          ]
        }
      ]
    }
  ]
}
```
 
FACTSHEETSTATE | Integration API reads and writes the content of a FactSheetState field as a String, which makes it easy to handle. Please be aware to only send allowed values into a state field.
MILESTONE |  Milestones can be written following the same logic as "project" data is written by the Integration API. All content will just replace the current content by default. iAPI takes care to ensure the final state in Pathfinder reflects what was sent in the processor. There is no need to decide if items need to be deleted or modified or added new. The data sent by iAPI will always reflect the full state after writing. This allows to process without knowledge of the current state and does not interfere with potential other operations happening in parallel.   ```
{
  "key": {
    "expr": "lxMilestones"
  },
  "values": [
    {
      "forEach": {
        "elementOf": "${data.milestones}",
        "filter": "${true}"
      },
      "map": [
        {
          "key": "name",
          "value": "${integration.output.valueOfForEach.n}"
        },
        {
          "key": "date",
          "value": "${integration.output.valueOfForEach.d}"
        },
        {
          "key": "description",
          "value": "${integration.output.valueOfForEach.type}"
        }
      ]
    }
  ]
}
```
 


Example updates section for an inbound data processor:

```
{
  "updates": [
    {
      "key": {
        "expr": "name",
        "regexReplace": {
          "match": "",
          "replace": ""
        }
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
          "expr": "${header.processingMode}",
          "regexMatch": "abc"
        },
        {
          "expr": "${header.processingMode}_2"
        }
      ],
      "optional": true
    }
  ]
}
```



### Modes
Changing the Data Processor mode to "delete" will mark the Fact Sheet "archived", so behave the same way as if users selected "Delete" from the UI.
Delete mode:

```
{
  "mode": "delete"
}
```



Example connector and input data using the delete mode:

```
{
  "processors": [
    {
      "processorType": "inboundFactSheet",
      "processorName": "Delete Data sent in the Input",
      "processorDescription": "",
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
      "updates": [],
      "mode": "delete"
    }
  ],
  "variables": {}
}
```



Example input:

```
{
  "connectorType": "example",
  "connectorId": "deleteMode",
  "connectorVersion": "1.0.0",
  "lxVersion": "1.0.0",
  "description": "Delete Data using mode",
  "processingDirection": "inbound",
  "processingMode": "partial",
  "customFields": {},
  "content": [
    {
      "type": "Deployment",
      "id": "634c16bf-198c-1129-9d08-92630b573fbf",
      "data": {
        "app": "HR Service",
        "version": "1.8.4",
        "maturity": "3",
        "clusterName": "westeurope",
        "tags": []
      }
    }
  ]
}
```



In case a Fact Sheet is updated with a standard mode that has been set to "archived", there are two potential behaviors:
  * In case the Fact Sheet was matched using the external ID, then a new Fact Sheet will be created
  * In case the reference was done by using the internal ID, then the old Fact Sheet will be used and set back to "active"
