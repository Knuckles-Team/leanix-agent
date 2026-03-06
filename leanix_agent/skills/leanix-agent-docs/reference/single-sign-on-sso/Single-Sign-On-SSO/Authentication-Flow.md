##  Authentication Flow
SAP LeanIX supports SP-initiated SSO. The following image illustrates the SAML 2.0 authentication flow.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio4100c19c53924af8b9a46e618ddfdedb_HiRes.png)
Authentication Flow
When a user attempts to access the SAP LeanIX application through a browser, the SP first checks if the user is already authenticated. If not, the user is redirected to the identity provider system, which initiates the authentication process, typically through a username and password.
Once the user has been successfully authenticated within the IdP, the IdP sends a response to the SP. The response includes relevant attributes, such as the user's email address, that serve to identify the user within SAP LeanIX. Once the SP has verified the response, the user is granted access to the SAP LeanIX application.
