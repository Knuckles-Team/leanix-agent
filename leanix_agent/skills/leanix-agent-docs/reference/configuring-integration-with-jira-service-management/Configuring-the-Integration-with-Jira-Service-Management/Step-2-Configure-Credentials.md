##  Step 2: Configure Credentials
After selecting the integration, you're prompted to provide connection credentials. On the Credentials tab, provide the following information.
Credential Parameters Parameter | Description
---|---
Configuration Name | A descriptive name for this integration configuration.
Jira Domain URL |  The origin of the URL used to access your Assets.  The URL follows this format: https://{your-domain}.atlassian.net/. Replace {your-domain} with your Jira Service Management domain name.
Username | Your Jira Service Management account email address.
Access Key | An API token generated from your Jira Service Management account.
Managing User |  SAP LeanIX technical user associated with the integration.


### Get an Access Key (API Token)
To generate an API token in Jira Service Management, follow these steps:
  1. Navigate to Account Settings in Jira Service Management.
  2. Go to the Security tab.
  3. Under API tokens, choose Create and manage API tokens.
![Screenshot showing the API tokens section with the Create and manage API tokens link.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loiocf02e9cfcda24b4f9b8ff135a8fa3061_LowRes.png)
API Tokens Section
  4. Choose Create API token.
![Screenshot showing the Create API token button in the API tokens management page.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio9506ab1e8b3747b9a4508025926953cd_LowRes.png)
Create API Token Button
  5. Provide a label for the token, set the expiration date, then choose Create.
![Screenshot showing the API token creation dialog with fields for label and expiration date.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio1d1998dc24d146ca8c22a82208225be4_LowRes.png)
API Token Creation Dialog
  6. Copy the generated token. The token is displayed only once.
![Screenshot showing the generated API token ready to be copied.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2b82fa81dcc84cc292bd44aa9450dd17_LowRes.png)
Copy API Token


After completing this step, the integration is active but requires a mapping configuration to begin synchronization.
