##  Step 1: Retrieve User Permissions
To update a permission, first retrieve a list of user permissions for a workspace. To do that, make a GET request to the following endpoint:

```
https://{SUBDOMAIN}.leanix.net/services/mtm/v1/workspaces/{id}/permissions
```



The following table lists the input parameters.
Parameter | Parameter Type | Data Type | Required | Description
---|---|---|---|---
id | Path | String | Required | The ID of the workspace to retrieve user permissions for.
q | Query | String | Optional | Query string to filter data for a specific user. You can specify the user's first name, last name, role, or other details.
email | Query | String | Optional | The email address of the user to search for.
status | Query | String | Optional | The status of the user to search for, such as ACTIVE, INVITED, or ARCHIVED.
includeTechnicalUsers | Query | Boolean | Optional | Determines whether to include technical users in the response.
page | Query | Integer | Optional | The page number to return in the response. The default value is 1.
size | Query | Integer | Optional | The page size to return in the response. The default value is 30. The maximum value is 100.
sort | Query | String | Optional | A list of sorting parameters separated by commas.


Example request:

```
curl --request GET \
  --url https://{SUBDOMAIN}.leanix.net/services/mtm/v1/workspaces/bdba4b5d-2d63-49ef-f8g4-045f020294bb/permissions?email=john.doe%40meshlab.de \
  --header 'content-type: application/json' \
  --header 'authorization: Bearer {ACCESS_TOKEN}' \
```



Example response:

```
{
  "status": "OK",
  "type": "Permission",
  "errors": [],
  "total": 1,
  "data": [
    {
      "links": [...],
      "id": "04259076-8cbc-418e-5d8h-20144d5d8bda",
      "user": {
        "id": "f767b7a2-5dd8-423e-d7f4-f9ea34d36ce8",
        "account": {...},
        "userName": "john.doe@organization.com",
        "email": "john.doe@organization.com",
        "role": "ACCOUNTUSER",
        "status": "ACTIVE",
        ...
      },
      "workspace": {...},
      "workspaceId": "bdba4b5d-2d63-49ef-f8g4-045f020294bb",
      "role": "MEMBER",
      "status": "INVITED",
      "lastLogin": null,
      "invitedByUser": {...},
      "reviewedByUser": null,
      "customerRoles": null,
      "accessControlEntities": null,
      "ignoreBlacklist": false,
      "count": 0,
      "replayed": false,
      "active": false
    }
  ]
}
```



