##  Creating a Technical User
Follow these steps:
  1. In the user profile menu, select Administration, and then go to Technical Users.
  2. Click New Technical User.
  3. Enter the details for a Technical User:
     * Username: Enter a username for the Technical User.
     * (Optional) Description: Enter a description for the Technical User.
     * Permission Role: Select a permission role: Admin, Viewer, or Member.
     * (Optional) Customer Roles: Roles that you can define and configure in services that support them, such as the [Pathfinder![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fapp.leanix.net%2Fopenapi-explorer%2F%3Furls.primaryName%3DPathfinder "https://app.leanix.net/openapi-explorer/?urls.primaryName=Pathfinder"). In contrast, standard roles are an integral part of the SAP LeanIX authorization scheme and are recognized and supported by all services. You can configure custom roles only if your organization manages user roles within a single-sign-on (SSO) identity provider. For more information, see [Managing User Roles with SSO](https://help.sap.com/docs/leanix/ea/single-sign-on-sso?locale=en-US&state=PRODUCTION&version=CLOUD#loio275cc8227a441014a371975e4b816f0a__managing-user-roles-with-sso).
     * (Optional) Access Control Entities: Use this parameter to map a Technical User to Access Control Entities (ACEs) and Access Control Lists (ACLs) created with virtual workspaces. To learn more, see [Virtual Workspaces](https://help.sap.com/docs/leanix/ea/virtual-workspaces?locale=en-US&state=PRODUCTION&version=CLOUD "Manage access to fact sheets for custom user groups").
     * Expiry Date: Set the expiration date for the API token associated with this user.
  4. Click Save.
![Creating a Technical User](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2741dc8b7a441014aa64bb75eca554bd_LowRes.png)
Creating a Technical User


A Technical User is created, and an overlay with an API token is displayed.
Save the API token. It is shown only once.
![An API token is generated once you have created a Technical User](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2752dfee7a4410149c988ea0bb1f6874_LowRes.png)
An API token is generated once you have created a Technical User
