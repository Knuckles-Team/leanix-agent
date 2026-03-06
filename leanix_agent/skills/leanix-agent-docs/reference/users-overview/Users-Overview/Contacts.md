##  Contacts
In SAP LeanIX, users who are subscribed to fact sheets but haven't yet been invited to the workspace and don't have an SAP LeanIX account are called contacts. Contacts are created when non-SAP-LeanIX users are added as fact sheet subscribers. For more information, see [Adding Non-SAP-LeanIX Users as Subscribers](https://help.sap.com/docs/leanix/ea/fact-sheet-subscription?locale=en-US&state=PRODUCTION&version=CLOUD#loio275a16427a441014be448690c54e7cf0__adding_non-sap-leanix_users_as_subscribers).
The table below highlights the differences between contacts and workspace users:
Criteria | Contact | Workspace User
---|---|---
Status To learn more about statuses, see [User Statuses](https://help.sap.com/docs/leanix/ea/users-overview?locale=en-US&state=PRODUCTION&version=CLOUD#loio2758f7bb7a4410148ebaeb6edf8d8e3f__user_statuses). | Not invited |
  * Active
  * Invited (users who haven't yet accepted the invitation request)


Ways to add users |
  * Excel import (subscriber)
  * Inline table editing (subscriber)
  * API request

|
  * Email invitation
  * SSO
  * SCIM
  * API request


Can be added as a subscriber | Yes | Yes
A permission role is assigned | No | Yes
Access to the workspace | No | Yes
Receives notifications and surveys from SAP LeanIX | No | Yes


You can view all contacts on the Not invited tab in the Users section of the administration area. When needed, you can invite contacts to a workspace individually or in bulk by clicking Invite on the right. For SSO-enabled workspaces, to prevent sending invitation emails, clear the Send Invitation Email checkbox in the invitation overlay.
You can also invite contacts from the Subscriptions tab on a specific fact sheet or by using the Invite User option in the user profile menu.
![List of Contacts in the Not Invited Tab](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio275254267a4410148bf9b2d6d79dce3d_LowRes.png)
Contacts on the Not Invited Tab in the Users Section of the Administration Area
