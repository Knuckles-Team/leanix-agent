##  Inbound Document
The inboundDocument processor is used to create, update, or delete documents linked to Fact Sheets.
The structure is the same as for the inboundFactSheet data processor. Same matching logic for Fact Sheets applies. The found Fact Sheet will not be modified but a linked document changed according to mode (default is "createOrUpdate")
Keys Specific to theinboundDocumentProcessor | Details
---|---
description | Description of the document
origin | From what department or person does this originate from
url | Link to the document
documentType | A string containing information how to display the link on the Resource tab. Values are dynamic. It is suggested to first read the links for an item, then copy the values for writing similar links. Some examples of the value but this can change based on your specific configuration: policy, decision, jira, documentation, website, support_ticket, faq, additional_help, task, roadmap
metadata | A string containing information how to display the link on the Resource tab. Values are dynamic. It is suggested to first read the links for an item, then copy the values for writing similar links


**Caution**
The updates section must contain the key name, otherwise the run will fail.
Example inboundDocument processor:

```
{
  "processorType": "inboundDocument",
  "processorName": "My link to Integration API docs",
  "processorDescription": "Contains the link that will point to the documentation for the Integration API",
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
    "exactType": "ITComponent"
  },
  "run": 1,
  "updates": [
    {
      "key": {
        "expr": "name"
      },
      "values": [
        {
          "expr": "Integration API Document"
        }
      ]
    },
    {
      "key": {
        "expr": "documentType"
      },
      "values": [
        {
          "expr": "website"
        }
      ]
    },
    {
      "key": {
        "expr": "origin"
      },
      "values": [
        {
          "expr": "CUSTOM_LINK"
        }
      ]
    },
    {
      "key": {
        "expr": "url"
      },
      "values": [
        {
          "expr": "https://docs-eam.leanix.net/reference/integration-api"
        }
      ]
    }
  ]
}
```



