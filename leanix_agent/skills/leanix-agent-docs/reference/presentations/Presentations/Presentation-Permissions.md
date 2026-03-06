##  Presentation Permissions
By default, all workspace users can view and edit presentations. You can change the permission type of presentations to restrict viewing and editing permissions to specific users. The presentation owner always has editing permissions.
You can modify permissions for all presentations for non-admin roles in the User Roles and Permissions section of the administration area. For more information, see [Role-Based Permissions](https://help.sap.com/docs/leanix/ea/user-roles-and-permissions?locale=en-US&state=PRODUCTION&version=CLOUD#loio275def827a4410149362f3672c614956__role-based_permissions).
The following table lists presentation permissions for standard user roles.
Action | Admin | Member | Viewer
---|---|---|---
Create a new presentation | Yes | Yes | No
Edit a presentation | Yes | Yes | No
Delete a presentation | Yes |
  * Yes: User’s own presentations and shared presentations for which the user has edit permission.
  * No: Shared presentations for which the user doesn’t have edit permission.

| No
Share a presentation | Yes | Yes | Yes


**Note**
Users with custom user roles may not have permissions to create or edit presentations. To request presentation permissions for users with custom roles, please contact [SAP LeanIX Support![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fwww.leanix.net%2Fsupport "https://www.leanix.net/support") or, if you're an SAP customer, submit a request from the [SAP for Me![Information published on SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/sap_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fme.sap.com%2F "https://me.sap.com/") portal.
You can configure custom user roles only if you're managing roles within your single sign-on identity provider. For more information, see:
  * [Managing User Roles with SSO](https://help.sap.com/docs/leanix/ea/single-sign-on-sso?locale=en-US&state=PRODUCTION&version=CLOUD#loio275cc8227a441014a371975e4b816f0a__managing-user-roles-with-sso)
  * [Creating Custom User Roles](https://help.sap.com/docs/leanix/ea/user-roles-and-permissions?locale=en-US&state=PRODUCTION&version=CLOUD#loio275def827a4410149362f3672c614956__creating_custom_user_roles)
