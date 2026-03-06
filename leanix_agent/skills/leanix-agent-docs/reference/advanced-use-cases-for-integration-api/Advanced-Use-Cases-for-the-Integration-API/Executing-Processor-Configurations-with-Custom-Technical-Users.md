##  Executing Processor Configurations with Custom Technical Users
Besides using the default technical user that is created by the integration, it is possible to use technical users that are already set up in the workspace. To execute a processor configuration with a custom technical user, the user ID of the technical user has to be added to the credentials section of the configuration. In the following example, the CUSTOM_TECHNICAL_USER_ID placeholder would need to be replaced by the ID of the technical user that will be used when reading data from or writing data to your workspace.
Usage of a Custom Technical User by the Integration API:

```
{
  "credentials": {
    "technicalUserId": "CUSTOM_TECHNICAL_USER_ID"
  },
  "processors": [
  ]
}
```



