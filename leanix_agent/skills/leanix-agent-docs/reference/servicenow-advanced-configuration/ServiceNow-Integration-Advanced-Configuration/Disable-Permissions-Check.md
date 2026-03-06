##  Disable Permissions Check
In case you run into issues with the validation of permissions for a given ServiceNow table and/or field and wish to disable this check during the validation phase, set the "ignorePermissionCheck" variable to "true" in the configuration as below in JSON:

```
{
  "factSheetSyncDescriptors": [
    ...
  ],
  ...
  "validation": {
    "ignorePermissionCheck": true
  }
}

```



YesNo
Send
