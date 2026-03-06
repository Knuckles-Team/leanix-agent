##  Restricting the Execution of Processor Configurations
To restrict the execution of processor configurations to specific users, you can add the executionRestrictions object next to the processors of the configuration.
Restricting the execution of Integration API processor configurations:

```
{
  "executionRestrictions": {
    "defaultTechnicalUser": true,
    "userIds": ["USER_ID"]
  },
  "processors": [
  ]
}
```



The defaultTechnicalUser parameter specifies whether the default technical user should be allowed to execute the configuration, while the userIds parameter specifies the user IDs of the users that should be allowed to execute the configuration. To restrict execution to multiple users, simply add their user IDs to the userIds array.
Both parameters are optional and when the executionRestrictionsobject is specified and keept empty no user will be able to execute the processor.
