##  Auto deletion with inboundProcessors
Integration API supports the processing mode "full" mode when creating the configuration. Only in case, the configuration is set to mode "full", a section "deletionScope" is read from the processor configuration. The following operations are supported:
  * Deletion of Fact Sheets If that section does contain a key "factSheets", all Fact Sheets matching the scope query inside will be removed if they are not found in the processed LDIF
  * All Fact Sheets that match the deletion scope but are not touched by an inbound Data Processor during processing, will be removed (set to "Archived")
  * Relations can be automatically removed as well. The structure to define relations to be deleted is similar. See an example configuration below. The example removes all relations but by narrowing the scope to fewer Fact Sheets, only for these Fact Sheets relations will be removed
  * Documents can be deleted by defining a scope of Fact Sheets and adding a regular expression pattern to match the documents by name that may be removed if they are no longer referenced by the incoming LDIF data


How does this work? Do I need to delete any data manually or first delete in a processor?
The concept of deletion is unique with the Integration API in that there is no active deletion needed by the user. All the deletion is done by the iAPI automatically through the configuration of a 'deletion scope'.
The logic of deletion works as follows:
  1. In an inbound 'Run', factsheets and other data like tags or relations are created and updated. These actions of creating or updating mark artifacts as 'touched'.
  2. Upon finishing a the 'Run', the API determines which artifacts within the defined deletion scope have not been touched at all in the course of the run and these untouched artifacts are deleted.
  3. This prevents constant “delete-create-delete-create” cycles that would be visible in the audit log of factsheets and avoids any manual work deletion any data


**Note**
Sending data for an archived Fact Sheet in the SyncRun.
In case an archived Fact Sheet exists in the Workspace with the same externalId as sent in one of the input LDIFs, Integration API will create a new FactSheet rather than recovering the deleted Fact Sheet, this is done in order to avoid unexpected data on the archived Fact Sheet reflected on the Active Fact Sheet.
This scenario can only happen when the "uniqueFactSheet" attribute for a Fact Sheet is set to "false" when set to "true" externalIds are already cleared while archiving a Fact Sheet.
**Note**
Please note that you can define multiple sets of deletion scopes for every type (e.g. 2 Fact Sheet deletion scopes and 3 relation deletion scopes). Processed items during synchronization runs will be compared against each set separately. Any item in each deletion scope definition will be removed if not touched during processing. It is allowed to even define overlapping scopes. Each item will be handled once only.
### Example
The example processor in this section removes the following data from a workspace:
  * All project fact sheets that are no longer part of the incoming LDIF data
  * All relations from applications to IT components
  * All documents prefixed with "MyDocs_"


**Caution**
Before running this example processor, consider implications and always proceed with caution. The processor is configured to delete all project fact sheets present in the workspace. To limit the deletion scope, modify the code so that a tag such as "TEST_PRJ" is assigned to test projects. You can add this tag as a facetFilter to the deletion scope definition as shown below:

```
{
     "facetKey": "${integration.tags.getTagGroupId('Testing')}",
     "operator": "OR",
     "keys": [
      "${integration.tags.getTagId('Testing','TEST_PRJ')}"
     ]
}
```



Run this example processor multiple times to first create all projects, then remove one item and try again.
Sample configuration for processingMode "full" to remove projects automatically:

```
{
 "deletionScope": {
  "maximumDeletionRatio": {
   "relations": 40,
   "factSheets": 30
  },
  "factSheets": [
   {
    "scope": {
     "facetFilters": [
      {
       "keys": [
        "Project"
       ],
       "facetKey": "FactSheetTypes",
       "operator": "OR"
      }
     ],
     "ids": []
    }
   }
  ],
  "relations": [
   {
    "relationTypes": [
     "relApplicationToITComponent"
    ],
    "scope": {
     "facetFilters": [],
     "ids": []
    }
   }
  ],
  "documents": [
   {
    "documentMatches": [
     "^MyDocs_.*"
    ],
    "scope": {
     "facetFilters": [
      {
       "keys": [
        "Project"
       ],
       "facetKey": "FactSheetTypes",
       "operator": "OR"
      }
     ],
     "ids": []
    }
   }
  ]
 },
 "processors": [
  {
   "processorType": "inboundFactSheet",
   "processorName": "Apps from Deployments",
   "processorDescription": "Creates LeanIX Applications from Deployments",
   "type": "Project",
   "filter": {
    "exactType": "prj"
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
       "expr": "${data.name}"
      }
     ]
    }
   ],
   "enabled": true,
   "logLevel": "debug"
  }
 ]
}
```



Sample LDIF:

```
{
 "connectorType": "prjFull",
 "connectorId": "prjFull",
 "connectorVersion": "1.0.0",
 "lxVersion": "1.0.0",
 "content": [
  {
   "type": "Project",
   "id": "prj-42",
   "data": {
    "name": "Project 42"
   }
  },
  {
   "type": "Project",
   "id": "prj-43",
   "data": {
    "name": "Project 43"
   }
  },
  {
   "type": "Project",
   "id": "prj-44",
   "data": {
    "name": "Project 44"
   }
  }
 ]
}
```



