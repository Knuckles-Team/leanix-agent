##  Long running API calls
The default behaviour of Integration API is to execute all changes with the user that is provided by the API client when logging in. E.g. the history of factsheets will show this user as the one executing the changes as if the user logged into the SAP LeanIX UI and did the changes manually. This is easy to understand and communicate. In some situations however, it may not be sufficient.
Use Cases may be:
  * The process takes more than 60 minutes.
  * All changes the API does are caused by different login users, but should rather be shown to the user as a change the Integration API did instead of showing all the different API users.


In order to support long running inbound or outbound processes, an API Token may be provided in the configuration. This will be used instead of the access token that comes with the call from the API (as it will expire after one hour and does not contain any refresh token to grant access to the workspace data for more than 60 minutes)
Configure API Token as part of the Processor configuration:

```
{
  "credentials": {
    "apiToken": "..."
  },
  "processors": [
  ]
}
```



As an alternative, the Integration API can be configured to use a "Technical User" for accessing the SAP LeanIX Pathfinder backend. This user called INTEGRATION_API will be automatically created in the workspace by the API if it is not existing.
To use the Technical Users, please add the following section.
Usage of the default Technical User by the Integration API:

```
{
  "credentials": {
    "useTechnicalUser": true
  },
  "processors": [
  ]
}
```



