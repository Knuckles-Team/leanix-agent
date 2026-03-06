##  Creating Custom User Roles
Follow these steps:
  1. In your IdP, add claims role and customerRoles, then create the corresponding roles.
     * role: Create the following roles using uppercase letters: VIEWER, MEMBER, and ADMIN.
     * customerRoles: Create custom user roles using uppercase letters, for example, AUDITOR.
To learn more about attribute mapping, see [Attribute Mapping](https://help.sap.com/docs/leanix/ea/single-sign-on-sso?locale=en-US&state=PRODUCTION&version=CLOUD#loio275cc8227a441014a371975e4b816f0a__attribute-mapping).
  2. In SAP LeanIX, create the corresponding user roles in the User Roles section of the administration area.
    1. Click New User Role. You land on the role configuration page.
    2. In the Technical Name field, enter the role name using uppercase letters as specified in your IdP, for example, AUDITOR. The name serves as the unique role ID.
    3. Optional: Clone permissions for the custom role from an existing role. This is a one-time snapshot, not a dynamic relation that is actively maintained. If you skip this option, the new custom role gets a set of default permissions, ensuring that the workspace functions as expected.
    4. Optional: Add translations for the technical name to provide a more user-friendly format for the role label. Translations appear in various areas of the application. Select languages, then enter a translation and description for each language.
    5. Click Add.
    6. Create more custom roles to match the role matrix in your IdP.
![Creating a Custom User Role](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio275036e07a441014ae15fcf078b15228_LowRes.png)
Creating a Custom User Role
  3. In SAP LeanIX, configure permissions for each custom role. To learn more about permissions, see [Role-Based Permissions](https://help.sap.com/docs/leanix/ea/user-roles-and-permissions?locale=en-US&state=PRODUCTION&version=CLOUD#loio275def827a4410149362f3672c614956__role-based_permissions).


After you’ve configured custom roles, you can assign these roles to users in your IdP. Users get access to SAP LeanIX with the permissions that you configured.
With this configuration, you can’t assign custom roles to users in your SAP LeanIX workspace. You can only do it in your IdP.
