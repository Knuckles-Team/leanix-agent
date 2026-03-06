##  Procedure
  1. Select the collection for which you want to configure authentication. If needed, create a new collection.
  2. On the collection page, navigate to the Authorization tab.
  3. In the Type list, select OAuth 2.0.
  4. Under Configure New Token, click Edit token configuration and specify the following details:
     * Token Name: Enter a name for the token.
     * Grant Type: Select Client Credentials.
     * Access Token URL: Enter the following URL of the authentication endpoint: https://{SUBDOMAIN}.leanix.net/services/mtm/v1/oauth2/token. Replace {SUBDOMAIN} with your SAP LeanIX subdomain. You can copy the subdomain value from the URL of your workspace.
     * Client ID: Enter apitoken.
     * Client Secret: Enter the API token that you obtained by creating a Technical User.
     * Client Authentication: Select Send as Basic Auth header.
![Configure a new token for authentication in Postman.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274d868d7a44101490f592c95dcd12b1_LowRes.png)
Configuring a New Token for OAuth 2.0 Authentication in Postman
  5. To save the changes that you applied to the collection, click Save.


The authorization method that you configured will be used for every request in the collection.
To request a new access token, click Get New Access Token.
YesNo
Send
![close icon](https://consent.trustarc.com/get?name=sapglow-close-icon.png)
This site uses cookies and related technologies, as described in our Cookie Statement, for purposes that may include site operation, analytics, enhanced user experience, or advertising. You may choose to consent to our use of these technologies, or manage your own preferences.
Understood Manage Settings
[Privacy Statement](https://help.sap.com/docs/privacy)|[Cookie Statement](https://www.sap.com/about/legal/privacy/cookies.html)
