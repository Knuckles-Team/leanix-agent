##  Get All Long-Lived Access Tokens
Before proceeding, obtain a short-lived access token. The associated Technical User must have the ACCOUNTADMIN role. For instructions, see [Get a Short-Lived Access Token](https://help.sap.com/docs/leanix/ea/access-tokens-required-for-scim?locale=en-US&state=PRODUCTION&version=CLOUD#loio27584fdb7a441014b39cc735479e4c85__get_a_short-lived_access_token).
To retrieve existing long-lived access tokens, make a GET request to the following endpoint:

```
https://{SUBDOMAIN}.leanix.net/services/mtm/v1/longlivedBearerTokens

```



Replace {SUBDOMAIN} and {SHORT_LIVED_ACCESS_TOKEN} with your values.
Example cURL request:

```
curl --request GET \
  --url https://{SUBDOMAIN}.leanix.net/services/mtm/v1/longlivedBearerTokens \
  --header 'Authorization: Bearer {SHORT_LIVED_ACCESS_TOKEN}'

```



Example JSON response:

```
[
  {
    "id": "47394a58-4165-45e4-6ge4-f9a706dad4fb",
    "accountId": "fb526496-751b-44cd-31h3-369f233fa543",
    "accessTokenId": "b25f9c17-5fab-41a5-96a5-fef3bc1943e1",
    "valid": true,
    "creatorId": "8c263138-afab-4823-34gh-3e32628d4dc6",
    "description": "My first long-lived bearer token",
    "createdAt": "2024-04-19T12:45:23.461Z"
  },
  ...
]

```



