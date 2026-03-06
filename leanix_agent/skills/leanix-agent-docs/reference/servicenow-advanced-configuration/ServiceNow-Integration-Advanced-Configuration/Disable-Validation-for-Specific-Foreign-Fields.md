##  Disable Validation for Specific Foreign Fields
Due to issues integrating with ServiceNow, some field metadata may not be read correctly, which can lead to failed validations when saving otherwise valid configurations.
In this case, validation can be disabled specifically for these ServiceNow fields as follows in JSON:

```
{
  "factSheetSyncDescriptors": [
    {
      ...
      "fieldMapping": {
        "mapping": {
          "description": {
            "fieldType": "FOREIGN_FIELD",
            "foreignFieldName": "serviceNow_field_one",
            "useNormalDirection": true
          }
        }
      }
    },
    ...
  ],
  ...
  "validation": {
    "ignoredMissingFields": ["serviceNow_field_one"]
  }
}

```



In ignoredMissingFields, list all values of foreignFieldName for which you want to disable validation. The integration will still attempt to load the necessary metadata as usual, but will continue if the metadata cannot be found.
