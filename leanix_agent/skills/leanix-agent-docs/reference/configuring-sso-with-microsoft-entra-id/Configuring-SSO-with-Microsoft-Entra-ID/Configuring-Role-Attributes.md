##  Configuring Role Attributes
If you want to manage user roles within Microsoft Entra ID and not within SAP LeanIX, create the corresponding roles in Entra ID. To learn more about managing roles, see [Managing User Roles with SSO](https://help.sap.com/docs/leanix/ea/single-sign-on-sso?locale=en-US&state=PRODUCTION&version=CLOUD#loio275cc8227a441014a371975e4b816f0a__managing-user-roles-with-sso).
To configure role attributes, follow these steps:
  1. In Microsoft Entra ID, navigate to your enterprise application, then go to the Single sign-on section. Under Attributes and Claims, add attributes listed in the following table.
Name | Required | Source Attribute
---|---|---
role | Required |  user.assignedroles
customer_roles | Optional Use this attribute if you want to create custom roles. For more information, see [Custom User Roles](https://help.sap.com/docs/leanix/ea/user-roles-and-permissions?locale=en-US&state=PRODUCTION&version=CLOUD "Adjust role-based permissions and define custom roles."). |  user.assignedroles
ace | Optional Use this attribute if you want to configure virtual workspaces. For more information, see [Virtual Workspaces Configuration](https://help.sap.com/docs/leanix/ea/virtual-workspaces-configuration?locale=en-US&state=PRODUCTION&version=CLOUD "Set up virtual workspaces to manage access for custom user groups"). |  user.assignedroles


![Adding Claims](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27542de37a441014bb40a31610cf9f08_LowRes.png)
Adding Claims
  2. Create app roles for your enterprise application. Navigate to App registrations, go to App roles, then create standard roles by clicking Create app role: VIEWER, MEMBER, and ADMIN. If you're also using custom roles, create them using uppercase letters and underscores.
![Creating Application Roles](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274e2f9e7a441014aa07b7370f02a2c9_LowRes.png)
Creating Application Roles
  3. In the configuration of the enterprise application, assign app roles to users or groups.
![Assigning User Roles](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274a5ee67a4410149e07fcc339014a6c_LowRes.png)
Assigning User Roles
  4. Optional: If needed, configure claim conditions. Claim conditions is an option for assigning roles to Active Directory groups. Conditions will be processed in order of appearance.
An example of configured claim conditions is shown in the following image. If a user belongs to the scoped groups VIEWER and MEMBER, they will be assigned the MEMBER permission according to the specified order because the latest matching condition is always applied.
To learn how to configure the user.assignedroles values, please refer to the [Microsoft Entra ID documentation![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fentra%2Fidentity-platform%2Freference-app-manifest "https://learn.microsoft.com/en-us/entra/identity-platform/reference-app-manifest").
![Configuration of Claim Conditions](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2746385b7a441014b841b2a5fca45beb_LowRes.png)
Configuring Claim Conditions


### Verify your SSO Configuration
To verify your SSO configuration, first, access your workspace at https://{SUBDOMAIN}.leanix.netand log in, then open a SAML tracer browser extension or desktop application. In the SAML tracing you can see a list of required user attributes.
YesNo
Send
![close icon](https://consent.trustarc.com/get?name=sapglow-close-icon.png)
This site uses cookies and related technologies, as described in our Cookie Statement, for purposes that may include site operation, analytics, enhanced user experience, or advertising. You may choose to consent to our use of these technologies, or manage your own preferences.
Understood Manage Settings
[Privacy Statement](https://help.sap.com/docs/privacy)|[Cookie Statement](https://www.sap.com/about/legal/privacy/cookies.html)
