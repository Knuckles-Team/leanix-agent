##  Inbound Relation
The "inboundRelation" processor requires identification of two Fact Sheets. In this processor the "identifier" is replaced by two fields named "from" and "to". The potential values of the "from" and the "to" fields are identical with the "identifier" values and can handle internal and external ids as well.
Allowed values: JUEL expression plus optional replace RegEx map (available for each expression, for internal external and from and to in case of the inboundRelation processor).
Example RegEx in ID mapping:

```
{
  "identifier": {
    "external": {
      "id": {
        "expr": "${content.id}",
        "regexReplace": {
          "match": "",
          "replace": ""
        }
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
Please replace the type "relApplicationToITComponent" with the name of the relation that needs to be created or updated (e.g. "relToParent").
Example inboundRelation processor:

```
{
  "processors": [
    {
      "processorType": "inboundRelation",
      "processorName": "Rel from Apps to ITComponent",
      "processorDescription": "Creates LeanIX Relations between the created or updated Applications and ITComponents",
      "type": "relApplicationToITComponent",
      "filter": {
        "exactType": "Deployment"
      },
      "from": {
        "external": {
          "id": {
            "expr": "${content.id}"
          },
          "type": {
            "expr": "externalId"
          }
        }
      },
      "to": {
        "external": {
          "id": {
            "expr": "${data.clusterName}"
          },
          "type": {
            "expr": "externalId"
          }
        }
      },
      "run": 1,
      "updates": [
        {
          "key": {
            "expr": "description"
          },
          "values": [
            {
              "expr": "Relationship Description"
            }
          ]
        },
        {
          "key": {
            "expr": "activeFrom"
          },
          "values": [
            {
              "expr": "2019-08-02T09:03:49+00:00"
            }
          ]
        },
        {
          "key": {
            "expr": "activeUntil"
          },
          "values": [
            {
              "expr": "2020-08-02T09:03:49+00:00"
            }
          ]
        }
      ],
      "logLevel": "debug"
    }
  ]
}
```



**Note**
Referencing "from" and "to" fact sheets for relations by internal IDs.
The inboundRelation processor as well supports referencing source and target Fact Sheets by their internal id as well. The syntax is the same we see for the identifier for inboundFactsheet processor: "internal": "${content.id}"
**Note**
To create a Fact Sheet using the inboundFactsheet processor, providing an externalId is mandatory.
