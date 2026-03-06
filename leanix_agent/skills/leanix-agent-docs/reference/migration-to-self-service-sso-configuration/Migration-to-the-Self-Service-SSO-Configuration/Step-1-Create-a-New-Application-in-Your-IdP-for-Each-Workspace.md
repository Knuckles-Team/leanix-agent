##  Step 1: Create a New Application in Your IdP for Each Workspace
Create new IdP applications instead of copying or editing existing ones. If you keep your existing application unchanged, users will keep access until you fully migrate to the new SSO setup. The new application already uses the correct attribute names and can be tested without interfering with existing SSO connections.
Migrating to the new SSO configuration is a good opportunity to rethink your SSO setup and optimize it with additional advanced options:
  * Configure different IdPs for different workspaces. For example, you can use Microsoft Entra ID for your sandbox workspace and Okta for your production workspace.
  * Use regional IT setups and configure different IdPs for the same workspace. For example, the headquarters in Brazil can use Microsoft ADFS, while the subsidiary in Italy can use OneLogin.


### Create an IdP Configuration in SAP LeanIX
  1. In SAP LeanIX, navigate to Administration > Authentication and SSO.
  2. Start the SSO self-service configuration.
  3. Select the authentication type based on how you manage user roles: in the IdP or in SAP LeanIX. For more information, see [Managing Users with SSO](https://help.sap.com/docs/leanix/ea/managing-users?locale=en-US&state=PRODUCTION&version=CLOUD#loio275afeb47a441014b2a8c3973c072ba7__managing_users_with_sso).
  4. Optionally, configure additional settings:
     * Default role
     * Invitation only
     * Transient users
  5. Choose Save.


![Screenshot showing the SSO self-service configuration interface in SAP LeanIX with authentication type options and additional settings.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loiob3949cffb0d941ceac98b8f660352c23_LowRes.png)
SSO Self-Service Configuration
### Add a New Identity Provider
  1. In the Identity Provider section, choose Add Identity Provider.
  2. Enter the following details:
     * Display Name: A name for the IdP.
     * Description: A description for the IdP.
     * Username Domain: Only necessary if the attribute uid sends a value that doesn't have an email format, such as an employee number or ID. In this case, enter a domain (for example, "company.com").
     * Protocol: Select SAML.
  3. Choose Next.


![Screenshot showing the Identity Provider configuration form with fields for display name, description, username domain, and protocol selection.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loiofc38ef8290874406bf3c6fd240cc226a_LowRes.png)
Add Identity Provider Details
Metadata information is displayed.
![Screenshot showing the next step of Identity Provider configuration with additional configuration options.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio7e8a8d95673f4c18832b2b339a2f97b9_LowRes.png)
Identity Provider: Metadata Configuration
