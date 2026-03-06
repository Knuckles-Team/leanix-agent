##  Step 2: Update User Permissions
To update user permissions, make a POST request to the following endpoint:

```
https://{SUBDOMAIN}.leanix.net/services/mtm/v1/permissions
```



There are two main use cases for managing user permissions:
  * Updating the user role: Set role to one of the following values: VIEWER, MEMBER, or ADMIN. To learn more about these roles, see [Standard User Roles](https://help.sap.com/docs/leanix/ea/user-roles-and-permissions?locale=en-US&state=PRODUCTION&version=CLOUD#loio275def827a4410149362f3672c614956__standard_user_roles).
  * Updating the user status: Set status to one of the following values:
    * ARCHIVED: Archive a user. You can't remove users from a workspace. You can only archive their permissions.
    * ACTIVE: Reactivate an archived user account. You can't change the status from INVITED to ACTIVE.


From the response body that you received in the previous step, copy the JSON object within the data array and modify relevant attributes.
The following table lists required parameters to be passed in the request body. Other parameters are optional.
Parameter | Parameter Type | Data Type | Required | Description
---|---|---|---|---
user.id | Body | String | Required | The ID of the user.
workspace.id | Body | String | Required | The ID of the workspace the user belongs to.
role | Body | String | Required | The role to be assigned to the user.
status | Body | String | Required | The status to be assigned to the user.


In the example request, we change the user role to ADMIN. The request body contains only required parameters.
Example request:

```
curl --request POST \
  --url https://{SUBDOMAIN}.leanix.net/services/mtm/v1/permissions \
  --header 'content-type: application/json' \
  --header 'authorization: Bearer {ACCESS_TOKEN}' \
  --data '{
    "user": {
        "id": "f767b7a2-5dd8-423e-d7f4-f9ea34d36ce8"
     },
     "workspace": {
        "id": "bdba4b5d-2d63-49ef-f8g4-045f020294bb"
     },
     "role": "ADMIN",
     "status": "INVITED"
    }'
```



Example request body:

```
{
    "user": {
       "id": "f767b7a2-5dd8-423e-d7f4-f9ea34d36ce8"
    },
    "workspace": {
       "id": "bdba4b5d-2d63-49ef-f8g4-045f020294bb"
    },
    "role": "ADMIN",
    "status": "INVITED"
  }
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
  "total": 0,
  "data": {
    "links": [...],
    "id": "04259076-8cbc-418e-5d8h-20144d5d8bda",
    "user": {
      "id": "f767b7a2-5dd8-423e-d7f4-f9ea34d36ce8",
      "account": {...},
      "userName": "john.doe@organization.com",
      "email": "john.doe@organization.com",
      "role": "ACCOUNTUSER",
      "status": "ACTIVE",
      "technicalUser": false,
      "scimManaged": false,
      "transientUser": false,
      "links": [...],
      ...
    },
    "workspace": {...},
    "workspaceId": "bdba4b5d-2d63-49ef-f8g4-045f020294bb",
    "role": "ADMIN",
    "status": "INVITED",
    ...
  }
}
```



