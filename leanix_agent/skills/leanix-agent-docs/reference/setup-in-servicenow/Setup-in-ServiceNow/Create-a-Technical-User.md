##  Create a Technical User
To configure the integration and connect to ServiceNow, you need an API token. To get an API token, in SAP LeanIX, create a technical user through which the integration will run. Technical users enable you to manage API tokens for your workspace and audit your integrations.
For instructions on how to create a technical user, see [Technical Users](https://help.sap.com/docs/leanix/ea/technical-users?locale=en-US&state=PRODUCTION&version=CLOUD "To get an API token, create a technical user. Manage technical users collaboratively with other administrators."). Specify the following details:
  * Username: Enter a name that enables you to identify the technical user for the ServiceNow integration. This name appears in the audit log.
  * Permission Role: Select the Admin permission role.
  * Customer Roles and Access Control Entities: Leave these fields blank.
  * Expiry Date: The expiration date of the API token. You can set this date based on your security policy on regularly refreshing API tokens. Please note that it is not possible to automatically update the Integration Application on the ServiceNow side with the regenerated token.


Once you've created a technical user, an API token is displayed. Save the API token. It is shown only once.
