##  Inbound Tag
### Tag Sent as an Array
In the below example if you just specify the name of the tag without other attributes the Tag by the name specified will be created under "Other Tags" and attached to the Fact Sheet.
Example inboundTag processor:

```
{
  "processorType": "inboundTag",
  "processorName": "Tag creation",
  "processorDescription": "Creates tags and tag groups",
  "factSheets": {
    "external": {
      "ids": "${content.id}",
      "type": {
        "expr": "externalId"
      }
    }
  },
  "run": 1,
  "updates": [
    {
      "key": {
        "expr": "name"
      },
      "values": [
        {
          "expr": "${integration.valueOfForEach}"
        }
      ]
    },
    {
      "key": {
        "expr": "description"
      },
      "values": [
        {
          "expr": "${integration.valueOfForEach}"
        }
      ]
    },
    {
      "key": {
        "expr": "color"
      },
      "values": [
        {
          "expr": "#123456"
        }
      ]
    },
    {
      "key": {
        "expr": "group.name"
      },
      "values": [
        {
          "expr": "Kubernetes Tags"
        }
      ]
    },
    {
      "key": {
        "expr": "group.shortName"
      },
      "values": [
        {
          "expr": "k8s"
        }
      ]
    },
    {
      "key": {
        "expr": "group.description"
      },
      "values": [
        {
          "expr": "Tags relevant for Kubernetes"
        }
      ]
    },
    {
      "key": {
        "expr": "group.mode"
      },
      "values": [
        {
          "expr": "MULTIPLE"
        }
      ]
    },
    {
      "key": {
        "expr": "group.restrictToFactSheetTypes"
      },
      "values": [
        {
          "expr": "Application"
        },
        {
          "expr": "ITComponent"
        }
      ]
    }
  ],
  "forEach": "${data.tags}",
  "logLevel": "debug"
}
```



Example input in LDIF format for importing tags:

```
{
  "connectorType": "ee",
  "connectorId": "Kub Dev-001",
  "connectorVersion": "1.2.0",
  "lxVersion": "1.0.0",
  "description": "Imports kubernetes data into LeanIX",
  "processingDirection": "inbound",
  "processingMode": "partial",
  "customFields": {},
  "content": [
    {
      "type": "Deployment",
      "id": "784616bf-198c-11f9-9da8-9263b0573fbe",
      "data": {
        "app": "Finance Service",
        "version": "10.5",
        "maturity": "5",
        "clusterName": "westeurope",
        "tags": [
          "Important"
        ]
      }
    }
  ]
}
```



Example input in LDIF format for importing tag groups and tags:

```
{
  "connectorType": "Report Technology Radar",
  "connectorId": "Technology Radar Tags",
  "connectorVersion": "1.0.0",
  "lxVersion": "1.0.0",
  "processingDirection": "inbound",
  "processingMode": "partial",
  "customFields": {},
  "content": [
    {
      "type": "Deployment",
      "id": "1",
      "data": {
        "taggroups": [
          {
            "name": "Technology radar - Quadrant",
            "shortname": "TRQ",
            "description": "Beschreibung Quadrant",
            "mode": "SINGLE",
            "factsheettype": "ITComponent"
          },
          {
            "name": "Technology radar - Ring",
            "shortname": "TRR",
            "description": "Beschreibung Ring",
            "mode": "SINGLE",
            "factsheettype": "ITComponent"
          }
        ],
        "tags": [
          {
            "groupname": "Technology radar - Quadrant",
            "name": "Architecture Concepts",
            "description": "Beschreibung Architecture Concepts",
            "color": "#ff0000"
          },
          {
            "groupname": "Technology radar - Quadrant",
            "name": "Platforms",
            "description": "Beschreibung Platforms",
            "color": "#00ff00"
          },
          {
            "groupname": "Technology radar - Quadrant",
            "name": "Techniques",
            "description": "Beschreibung Techniques",
            "color": "#0000ff"
          },
          {
            "groupname": "Technology radar - Quadrant",
            "name": "Tools & Infrastructure",
            "description": "Beschreibung Tools & Infrastructure",
            "color": "#000000"
          },
          {
            "groupname": "Technology radar - Ring",
            "name": "Hold",
            "description": "Beschreibung Hold",
            "color": "#ff0000"
          },
          {
            "groupname": "Technology radar - Ring",
            "name": "Incubating",
            "description": "Beschreibung Incubating",
            "color": "#00ff00"
          },
          {
            "groupname": "Technology radar - Ring",
            "name": "Emerging",
            "description": "Beschreibung Emerging",
            "color": "#0000ff"
          },
          {
            "groupname": "Technology radar - Ring",
            "name": "Mature",
            "description": "Beschreibung Mature",
            "color": "#000000"
          }
        ]
      }
    }
  ]
}
```



### Tag Groups
Processor and sample LDIF for Tag Groups and Tags.
Example inboundTag processor for tag groups and tags:

```
{
  "processors": [
    {
      "processorType": "inboundTag",
      "processorName": "Tag group creation",
      "processorDescription": "Creates tag groups",
      "run": 0,
      "forEach": "${data.taggroups}",
      "updates": [
        {
          "key": {
            "expr": "group.name"
          },
          "values": [
            {
              "expr": "${integration.valueOfForEach.name}"
            }
          ]
        },
        {
          "key": {
            "expr": "group.shortName"
          },
          "values": [
            {
              "expr": "${integration.valueOfForEach.shortname}"
            }
          ]
        },
        {
          "key": {
            "expr": "group.description"
          },
          "values": [
            {
              "expr": "${integration.valueOfForEach.description}"
            }
          ]
        },
        {
          "key": {
            "expr": "group.mode"
          },
          "values": [
            {
              "expr": "${integration.valueOfForEach.mode}"
            }
          ]
        },
        {
          "key": {
            "expr": "group.restrictToFactSheetTypes"
          },
          "values": [
            {
              "expr": "${integration.valueOfForEach.factsheettype}"
            }
          ]
        }
      ],
      "logLevel": "warning",
      "enabled": true
    },
    {
      "processorType": "inboundTag",
      "processorName": "Tag creation",
      "processorDescription": "Creates tags",
      "run": 1,
      "forEach": "${data.tags}",
      "updates": [
        {
          "key": {
            "expr": "group.name"
          },
          "values": [
            {
              "expr": "${integration.valueOfForEach.groupname}"
            }
          ]
        },
        {
          "key": {
            "expr": "name"
          },
          "values": [
            {
              "expr": "${integration.valueOfForEach.name}"
            }
          ]
        },
        {
          "key": {
            "expr": "description"
          },
          "values": [
            {
              "expr": "${integration.valueOfForEach.description}"
            }
          ]
        },
        {
          "key": {
            "expr": "color"
          },
          "values": [
            {
              "expr": "${integration.valueOfForEach.color}"
            }
          ]
        }
      ],
      "logLevel": "warning",
      "enabled": true
    }
  ]
}
```



Example input in LDIF format for tag groups and tags:

```
{
  "connectorType": "Report Technology Radar",
  "connectorId": "Technology Radar Tags",
  "connectorVersion": "1.0.0",
  "lxVersion": "1.0.0",
  "processingDirection": "inbound",
  "processingMode": "partial",
  "customFields": {},
  "content": [
    {
      "type": "Deployment",
      "id": "1",
      "data": {
        "taggroups": [
          {
            "name": "Technology radar - Quadrant",
            "shortname": "TRQ",
            "description": "Beschreibung Quadrant",
            "mode": "SINGLE",
            "factsheettype": "ITComponent"
          },
          {
            "name": "Technology radar - Ring",
            "shortname": "TRR",
            "description": "Beschreibung Ring",
            "mode": "SINGLE",
            "factsheettype": "ITComponent"
          }
        ],
        "tags": [
          {
            "groupname": "Technology radar - Quadrant",
            "name": "Architecture Concepts",
            "description": "Beschreibung Architecture Concepts",
            "color": "#ff0000"
          },
          {
            "groupname": "Technology radar - Quadrant",
            "name": "Platforms",
            "description": "Beschreibung Platforms",
            "color": "#00ff00"
          },
          {
            "groupname": "Technology radar - Quadrant",
            "name": "Techniques",
            "description": "Beschreibung Techniques",
            "color": "#0000ff"
          },
          {
            "groupname": "Technology radar - Quadrant",
            "name": "Tools & Infrastructure",
            "description": "Beschreibung Tools & Infrastructure",
            "color": "#000000"
          },
          {
            "groupname": "Technology radar - Ring",
            "name": "Hold",
            "description": "Beschreibung Hold",
            "color": "#ff0000"
          },
          {
            "groupname": "Technology radar - Ring",
            "name": "Incubating",
            "description": "Beschreibung Incubating",
            "color": "#00ff00"
          },
          {
            "groupname": "Technology radar - Ring",
            "name": "Emerging",
            "description": "Beschreibung Emerging",
            "color": "#0000ff"
          },
          {
            "groupname": "Technology radar - Ring",
            "name": "Mature",
            "description": "Beschreibung Mature",
            "color": "#000000"
          }
        ]
      }
    }
  ]
}
```



### Tag Sent as a Comma-Separated List
Data in the tags looks like "Important,Mature". Helper function(toList) below will convert the comma-separated string to an Array and the Output of the below processor will be "Other Tags" : Important and Mature attached to Deployment "Finance Service".
Example inboundTag processor:

```
{
  "processorType": "inboundTag",
  "processorName": "Tag creation",
  "processorDescription": "Creates tags and tag groups",
  "factSheets": {
    "external": {
      "ids": "${content.id}",
      "type": {
        "expr": "externalId"
      }
    }
  },
  "run": 1,
  "updates": [
    {
      "key": {
        "expr": "name"
      },
      "values": [
        {
          "expr": "${integration.valueOfForEach.trim()}"
        }
      ]
    }
  ],
  "forEach": "${helper:toList(data.tags.split(','))}",
  "logLevel": "debug"
}
```



Example LDIF input for tags:

```
{
  "connectorType": "ee",
  "connectorId": "Kub Dev-001",
  "connectorVersion": "1.2.0",
  "lxVersion": "1.0.0",
  "description": "Imports kubernetes data into LeanIX",
  "processingDirection": "inbound",
  "processingMode": "partial",
  "customFields": {},
  "content": [
    {
      "type": "Deployment",
      "id": "784616bf-198c-11f9-9da8-9263b0573fbe",
      "data": {
        "app": "Finance Service",
        "version": "10.5",
        "maturity": "5",
        "clusterName": "westeurope",
        "tags": "Important,Mature"
      }
    }
  ]
}
```



The inboundTag processor does automatically creates tags that do not exist for a tag group (the tag processor does not create new tag groups).
The inbound tagProcessor can be configured to not create any tags nor change metadata of existing tags but only to assign Fact Sheets to existing tags. To use this functionality, an additional key "tagsReadOnly" needs to be configured in the updates section as shown in the example:
Example of enabling the "read only" mode for the inboundTag processor:

```
{
  "updates": [
    {
      "key": {
        "expr": "tagsReadOnly"
      },
      "values": [
        {
          "expr": "${true}"
        }
      ]
    },
    {
      "key": {
        "expr": "name"
      },
      "values": [
        {
          "expr": "${data.myTagName}"
        }
      ]
    }
  ]
}
```



**Note**
The "optional" flag avoids warning messages if the input data may not contain values for all fields and this is expected.
**Note**
Is used to only write values to internal variables. This will be used for aggregation use cases where the LDIF content needs to be used to only collect values without directly writing anything to SAP LeanIX.
