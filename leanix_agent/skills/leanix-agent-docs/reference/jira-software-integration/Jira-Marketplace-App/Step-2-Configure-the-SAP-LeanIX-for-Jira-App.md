##  Step 2: Configure the SAP LeanIX for Jira App
After you install SAP LeanIX for Jira, the next step is to connect the app to your SAP LeanIX workspace. You will do this in the Jira administration.
To configure SAP LeanIX for Jira, follow these steps:
  1. In the top navigation bar in Jira, go to Apps > Manage apps.
  2. To find SAP LeanIX for Jira, navigate the list or search for it in the Filter visible box. Click the app listing to open the app details.
  3. Choose Configure to open the configuration options.
  4. Enter the following information:
    1. Host: The main domain where the application is hosted. For example, your-subdomain.leanix.net. You don’t need to enter the protocol (https://).
    2. Workspace Name: The specific workspace within SAP LeanIX. For example, DemoEAM.
    3. API Token: The unique identifier from SAP LeanIX that allows Jira to access your workspace. To get an API token, create a technical user. Learn how in [Technical Users](https://help.sap.com/docs/leanix/ea/technical-users?locale=en-US&state=PRODUCTION&version=CLOUD "To get an API token, create a technical user. Manage technical users collaboratively with other administrators.").
  5. Choose Save.
