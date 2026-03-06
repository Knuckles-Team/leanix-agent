##  Step 2: Configure SAML Settings
Follow these steps:
  1. In the SAML Settings section of the application, specify the following:
     * Audience URI (SP Entity ID): https://{REGION}-signin.leanix.net/realms/service-provider/broker/{UUID}
     * ACS URL(Single Sign On URL): https://{REGION}-signin.leanix.net/realms/service-provider/broker/{UUID}/endpoint
     * Name ID format: Select EmailAddress.
     * Application username: This parameter depends on your Okta implementation. If the Okta username matches the SAP LeanIX email, select Okta username.
  2. In the Attribute Statements section, specify attributes to be added to the SAML assertion as shown in the following table. All fields are case-sensitive. The first four objects in the table are values that already exist on the user object. The role object will be added when assigning user groups to the application.
Name | Name Format | Value | Description
---|---|---|---
firstname | URI Reference |  user.firstName | The first name of the user.
lastname | URI Reference |  user.lastName | The last name of the user.
uid | URI Reference |  user.email | The unique ID of the user in the email format. We recommend using an ID that is different from the user's email address.
email | URI Reference |  user.email | The email address of the user.
role | URI Reference |  appuser.role | The role to be assigned to the user. Possible values: ADMIN, MEMBER, or VIEWER. If you submit multiple values separated with commas, the role with the highest level of privileges is assigned. If you're managing roles within SAP LeanIX, you can omit this attribute. To learn more, see [Managing User Roles with SSO](https://help.sap.com/docs/leanix/ea/single-sign-on-sso?locale=en-US&state=PRODUCTION&version=CLOUD#loio275cc8227a441014a371975e4b816f0a__managing-user-roles-with-sso).
customer_roles | URI Reference |  appuser.customRole | The custom role to be assigned to the user. Use this attribute only for custom roles, otherwise omit it. To learn more, see [Custom User Roles](https://help.sap.com/docs/leanix/ea/single-sign-on-sso?locale=en-US&state=PRODUCTION&version=CLOUD#loio275cc8227a441014a371975e4b816f0a__custom-user-roles).
ace | URI Reference |  appuser.entryACI | The ID of the Access Control Entity (ACE) of a Virtual Workspace. Use this attribute only when configuring access to a Virtual Workspace, otherwise omit it. To learn more, see [Virtual Workspaces Configuration](https://help.sap.com/docs/leanix/ea/virtual-workspaces-configuration?locale=en-US&state=PRODUCTION&version=CLOUD "Set up virtual workspaces to manage access for custom user groups").


  3. In the Feedback section, specify that the app is internal, then click Finish.
![Specifying the Type of an SSO Application in Okta](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio275197bf7a441014b881a919e63d7575_LowRes.png)
Specifying the Type of an SSO Application
