##  Configuring User Provisioning
Follow these steps:
  1. In the Okta admin dashboard, in the Applications section, select the SSO application for SAP LeanIX.
  2. On the General tab, in the App Settings section, click Edit, then select SCIM against Provisioning. Save the changes.
![Selecting the](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2747539f7a441014b467857d900c6d95_LowRes.png)
Selecting the SCIM Option for Provisioning in Okta
  3. If you've previously created the role attribute, in the Profile Editor section, delete the attribute and then recreate it with the following External namespace value. Save the changes. The update might take some time. To verify that the property update has been completed, check a sample user assignment for their role inheritance.
External namespace

```
urn:ietf:params:scim:schemas:extension:workspacePermission:2.0:User

```



![Creating the](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2748b4497a441014885993a89a124f2e_LowRes.png)
Creating the "role" Attribute
  4. On the SSO application page, navigate to the Provisioning tab. In the Integration section, click Edit against SCIM Connection and specify the following details. Save the changes.
Parameter | Value
---|---
SCIM connector base URL |  https://{SUBDOMAIN}.leanix.net/services/mtm/v1/scim/v2
Unique identifier field for users |  userName
Supported provisioning actions |  Select the following checkboxes:
     * Import New Users and Profile Updates: Any potential changes only apply to users assigned to the SAML application in Okta. If you leave this checkbox unselected, new users assigned to the SAML application won't be created in SAP LeanIX, and any potential changes made to user attributes won't be synchronized.
     * Push New Users
     * Push Profile Updates
Authentication Mode | HTTP Header
Authorization | Long-lived access token that you obtained


![Configuring SCIM Connection Settings](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274dc1df7a441014b77fc527ece754a8_LowRes.png)
Configuring SCIM Connection Settings
  5. On the Provisioning tab, in the To App section, enable the following options:
     * Create Users
     * Update User Attributes
     * Deactivate Users
Save the changes.
![Configuring Provisioning to App Settings](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274ef6ad7a4410148218fb448a4e35c7_LowRes.png)
Configuring Provisioning to App Settings
  6. To configure attribute mappings, scroll down to the Attribute Mappings section. The following attributes are mandatory for SCIM:
     * Username
     * Given name
     * Family name
     * Email
     * Primary email type
     * role: This attribute is only relevant for customers using an external IdP for SSO.
![Configuring Attribute Mappings for SCIM](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274fb6f67a4410148785b56749cf7060_LowRes.png)
Configuring Attribute Mappings for SCIM


SCIM with Okta is set up. User states should be synchronized between the systems.
YesNo
Send
![close icon](https://consent.trustarc.com/get?name=sapglow-close-icon.png)
This site uses cookies and related technologies, as described in our Cookie Statement, for purposes that may include site operation, analytics, enhanced user experience, or advertising. You may choose to consent to our use of these technologies, or manage your own preferences.
Understood Manage Settings
[Privacy Statement](https://help.sap.com/docs/privacy)|[Cookie Statement](https://www.sap.com/about/legal/privacy/cookies.html)
