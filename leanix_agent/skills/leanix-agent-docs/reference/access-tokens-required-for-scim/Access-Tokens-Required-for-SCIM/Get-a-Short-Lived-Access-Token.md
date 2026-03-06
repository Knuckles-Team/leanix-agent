##  Get a Short-Lived Access Token
To obtain a long-lived access token required for the SCIM integration, you need a short-lived access token. The long-lived token inherits the user role from the short-lived token. The Technical User through which you request a short-lived token must have the ACCOUNTADMIN role.
To obtain a short-lived access token, follow these steps:
  1. Create a technical user with the admin permission role. Save the API token that appears. For instructions, see [Technical Users](https://help.sap.com/docs/leanix/ea/technical-users?locale=en-US&state=PRODUCTION&version=CLOUD "To get an API token, create a technical user. Manage technical users collaboratively with other administrators.").
  2. Request the ACCOUNTADMIN role for the Technical User by [submitting a ticket![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fwww.leanix.net%2Fsupport "https://www.leanix.net/support") to SAP LeanIX Support. If you're an SAP customer, submit a request from the [SAP for Me![Information published on SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/sap_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fme.sap.com%2F "https://me.sap.com/") portal. In the request, provide the name of the Technical User.
  3. Using the API token of the Technical User, obtain a short-lived access token. Replace the following placeholders with your values:
     * {SUBDOMAIN}: Your SAP LeanIX subdomain. You can copy the subdomain value from the URL of your workspace.
     * {API_TOKEN}: The API token that you obtained by creating a Technical User.


Example cURL request:
```
                        curl --request POST https://{SUBDOMAIN}.leanix.net/services/mtm/v1/oauth2/token \
  -u apitoken:{API_TOKEN} \
  --data grant_type=client_credentials

```

A short-lived access token is returned in the access_token attribute in the response. The token is valid for 3600 seconds.
Save the token. You need it to obtain a long-lived access token.
Example JSON response:

```
{
   "scope": "",
   "expired": false,
   "access_token": "eyJhbGciOiJSUzI1NiJ9.eyJz [...] ssqaPSA",
   "token_type": "bearer",
   "expires_in": 3599
}

```



