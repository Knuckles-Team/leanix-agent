##  Advanced deletion
The functionality to delete content for elements we do no longer see references in the LDIF, can be used in an even more advanced was if required. The deletion scope for Relations, Tags and Documents may contain an optional key "advanced". If configured in the specific deletion scope, the value is evaluated as a JUEL expression resulting in "true" or "false". Only such elements will be added to the scope of elements potentially to be deleted if not touched where the JUEL expression evaluates to "true".
Multiple deletion scopes of same or different types can be defined. Please note that deletions of Fact Sheets will always happen last. This allows to use the Fact Sheet meta data lx.factsheet.* even for Fact Sheets that will be deleted. If allows to even use the owner field of the Fact Sheet deletion and evaluate in a relation, tag, document or subscription deletion scope in the state before the owner of the current run will be removed from the field (see ownership concept of advanced Fact Sheet deletion)
Please note, that currently no content from fields of type projectStatus is available for advanced deletion.
The information about the current Fact Sheet (for relations always the source Fact Sheet of a relation) is available using "lx.factsheet.*". All fields of the Fact Sheet can be used. In addition, all meta data fields of relations, documents and tags can be used in the JUEL for the related type of deletion scope.
Sample configuration to execute an advanced filter on document meta data:

```
{
 "deletionScope": {
  "factSheets": [
   {
    "scope":
     {
      "facetFilters": [
       {
        "keys": [
         "Project"
        ],
        "facetKey": "FactSheetTypes",
        "operator": "OR"
       }
      ]
     }
   }
  ],
  "relations": [
   {
    "relationTypes": [
     "relProjectToITComponent"
    ],
    "scope": {
     "ids": [],
     "facetFilters": []
    },
    "advanced": "${lx.relation.description.contains('from hr service')}"
   }
  ],
  "documents": [
   {
    "documentMatches": [
     ".*"
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
     ]
    },
    "advanced": "${lx.document.documentType.equals('jira') || lx.document.name.equals('someName') }"
   }
  ]
 },
 "processors": [
  {
   "processorType": "inboundFactSheet",
   "processorName": "Read Projects",
   "processorDescription": "Creates LeanIX Projects from Project Management Solution",
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
   }
  }
 ]
}
```



