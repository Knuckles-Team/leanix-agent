##  Step 2: Configure the SAP LeanIX for Confluence App
To configure SAP LeanIX for Confluence, follow these steps:
  1. In the top navigation bar in Confluence, go to Apps > Manage apps.
  2. To find SAP LeanIX for Confluence, navigate the list or search for it in the Filter visible box. Click the app listing to open the app details.
  3. Choose Configure to open the configuration options.
  4. Enter the following information:
    1. Host: The main domain where the application is hosted. For example, your-subdomain.leanix.net. You don’t need to enter the protocol (https://).
    2. API Token: This helps us verify the workspace you are trying to access and enables the use of Smart Links in Confluence. To get an API token, create a technical user. Learn how in the topic [Technical Users](https://help.sap.com/docs/leanix/ea/technical-users?locale=en-US&state=PRODUCTION&version=CLOUD "To get an API token, create a technical user. Manage technical users collaboratively with other administrators.").
  5. Choose Save.
The system checks the host and API token. If they are correct, it fills in the workspace name (for example, DemoEAM) and saves your settings.
