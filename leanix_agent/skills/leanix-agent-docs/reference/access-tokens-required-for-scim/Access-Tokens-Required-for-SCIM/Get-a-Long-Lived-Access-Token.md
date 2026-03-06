##  Get a Long-Lived Access Token
A long-lived access token is required for the SCIM integration. This token does not have an expiration date. It's valid until deleted or deactivated.
Before proceeding, obtain a short-lived access token. For instructions, see [Get a Short-Lived Access Token](https://help.sap.com/docs/leanix/ea/access-tokens-required-for-scim?locale=en-US&state=PRODUCTION&version=CLOUD#loio27584fdb7a441014b39cc735479e4c85__get_a_short-lived_access_token).
To obtain a long-lived access token, make a POST request to the following endpoint:
```
https://{SUBDOMAIN}.leanix.net/services/mtm/v1/longlivedBearerTokens

```

The following table lists parameters that you should pass in the request body.
Parameter | Parameter Type | Data Type | Required | Description
---|---|---|---|---
description | Body | String | Optional | The description for the long-lived access token.
scimConfiguration.workspaceId | Body | String | Required | The ID of the workspace to configure SCIM for. To get your workspace ID, in the administration area, navigate to API Tokens, then copy the WorkspaceId value.
scimConfiguration.permissionRole | Body | String | Required |  The default SAP LeanIX role to be assigned to the user. Possible values:
  * MEMBER
  * ADMIN
  * VIEWER




The following example request contains placeholders that you should replace with your values.
  * {SUBDOMAIN}: Your SAP LeanIX subdomain. You can copy the subdomain value from the URL of your workspace.
  * {SHORT_LIVED_ACCESS_TOKEN}: Short-lived access token that you retrieved in the previous step.
  * {WORKSPACE_ID}: The ID of your workspace. To get your workspace ID, in the administration area, navigate to the API Tokens section, then copy the WorkspaceId value.
  * {DEFAULT_USER_ROLE}: The default SAP LeanIX role to be assigned to the user. Possible values: VIEWER, MEMBER, or ADMIN.


Example cURL request:
```
 curl --request POST \
  --url https://{SUBDOMAIN}.leanix.net/services/mtm/v1/longlivedBearerTokens \
  --header 'Authorization: Bearer {SHORT_LIVED_ACCESS_TOKEN}' \
  --header 'Content-Type: application/json' \
  --data '{"description":"My first long-lived bearer token","scope":"","scimConfiguration":{"workspaceId":"{WORKSPACE_ID}","permissionRole":"{DEFAULT_USER_ROLE}"}}'

```

A long-lived access token is returned in the accessToken attribute in the response.
**Caution**
The access token is shown only once in the response. Save the token and make sure that you store it securely.
Example JSON response:

```
{
    "id": "47394a58-4165-45e4-6ge4-f9a706dad4fb",
    "accountId": "fb526496-751b-44cd-31h3-369f233fa543",
    "accessTokenId": "b25f9c17-5fab-41a5-96a5-fef3bc1943e1",
    "valid": true,
    "accessToken": "eyJraWQiOiI0MDJjODg3NTBjZmJhOGQzZTQ0Nj...LlRK-8-W7cg",
    "creatorId": "8c263138-afab-4823-34gh-3e32628d4dc6",
    "description": "My first long-lived bearer token",
    "createdAt": "2024-04-19T12:45:23.461Z"
}

```



