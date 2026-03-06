##  Invitation-Based Access for SSO Workspaces
The Invitation Only setting determines which workspaces a user can see in their workspace chooser:
  * If a workspace has activated Invitation Only:
    * Visible if the user is invited to this workspace and has a role, for example, member or admin. This is the more strict configuration where you control user access and new users must be invited specifically. The setting works with username + password as well as SSO.
  * If a workspace doesn’t require invitations:
    * Visible if the user is included in your IdP, even if the user was not previously invited to the workspace. This configuration is an IdP-based access where you don’t control user access specifically. You rather allow user access based on, for example, groups you configure in your IdP. This settings works with SSO only.


Follow these steps to configure the invitation-based access:
  1. Navigate to Administration > SSO and Authentication.
  2. Go to the Authentication Settings section.
  3. Toggle to activate or deactivate Invitation Only for this workspace. Invitation setting when configuring workspace authentication
![Screenshot of the Invitation Only Toggle](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loiod3860b4954514d269944b10235235b43_HiRes.png)
  4. Click Save.
