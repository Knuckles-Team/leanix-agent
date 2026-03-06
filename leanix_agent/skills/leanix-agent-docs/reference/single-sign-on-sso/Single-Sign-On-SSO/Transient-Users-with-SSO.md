##  Transient Users with SSO
SSO with an external IdP allows you to create transient user roles. A transient user is authenticated by SAP LeanIX based on their existence in your IdP, but is not assigned any role and therefore has no access to the workspace itself.
Transient users can access a simplified version of SAP LeanIX through self-service portals. You can embed these portals in your existing intranet, wiki, or any other system integrated with SSO. This setup allows you to directly share SAP LeanIX data without having to invite users to your workspace. For more information, see [Portal](https://help.sap.com/docs/leanix/ea/portals?locale=en-US&state=PRODUCTION&version=CLOUD "Create customizable, secure entry points that provide non-IT users with curated enterprise architecture information, resources, and visual assets outside the main application.").
To create transient users, follow these steps:
  1. Notify your support agent during the SSO setup or create a dedicated ticket.
  2. To grant access to a self-service portal to transient users, in the portal configuration, enter **TRANSIENT** in the **Accessible for** field.
![Modifying the Configuration of a Self-Service Portal to Grant Access to Transient Users](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274f14ba7a4410148301ad46bfac8950_LowRes.png)
Modifying the Configuration of a Self-Service Portal to Grant Access to Transient Users
  3. In your IdP, create a group for transient users if it doesn't already exist. Don't assign any permission roles (Admin, Viewer, or Member) to this group. If you're using Microsoft Entra ID, select the predefined value **Users**.
Users referenced in SAP LeanIX at any time, such as through an actual login or by being subscribed to a fact sheet as a contact, have a permanent user record. These users can't become transient users. Ensure they are granted proper role assignments, otherwise they'll lose access to the portal.


Upon signing in to SAP LeanIX, users are assigned the temporary transient role and are granted access to view the self-service portal data.
