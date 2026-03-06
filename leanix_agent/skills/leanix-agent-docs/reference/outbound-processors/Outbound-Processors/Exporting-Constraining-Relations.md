##  Exporting Constraining Relations
All information about constraining relations may be made available as content in "lx.relations" to be ready for export on demand by setting the key "constrainingRelations" to true. If the key is set to false or is not defined, no information about constraining relations will be present in the variable "lx.relations"
When exporting, the following field structure may be used when iterating over relations e.g. using forEach: "integration.valueOfForEach.constrainingRelations" and write all content to a map target or filter in a forEach section applied in the "values" segment.
Example configuration of constraining relations:

```
{
 "constrainingRelations": {
  "relations": [
   {
    "id": "60f57ffd-6dc8-42a5-9099-283256e627ad",
    "target": {
     "id": "1c3ef333-5cc1-414d-ba3e-108af7f0ffc4",
     "type": "UserGroup",
     "leanixV3IdUserGroup": "120000002"
    }
   },
   {
    "id": "a4661164-a948-4112-82de-270c31da4297",
    "target": {
     "id": "d973d8a8-6435-4952-988d-2e29feeafd57",
     "type": "UserGroup",
     "externalId": "Europe",
     "leanixV3IdUserGroup": "120000052"
    }
   }
  ],
  "totalCounts": [
   {
    "type": "relApplicationToUserGroup",
    "totalCount": 2
   }
  ]
 }
}
```



