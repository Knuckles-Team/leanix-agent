##  Step 4: Configure Global Read/Write Settings for New Fact Sheets
Configuring the global access settings reduces maintenance in the future. New fact sheets are automatically created with the correct access settings.
### Example: How do the global access settings work?
Let’s look at the global settings with a small example.
A member with the access control entities “Finance” and region “AMER” creates a new fact sheet. This is how the access settings for new fact sheets will be populated:
  * Global unrestricted
The fact sheet is visible to all users from all workspaces. Editing is possible for all users with the member role.
  * Read & Write restricted
The fact sheet is automatically restricted to “Finance” and region “AMER” users. All members with these access control entities can edit the fact sheet.
  * Write restricted
The fact sheet is visible to all users from all workspaces.
Editing is automatically restricted to “Finance” and region “AMER” members.


**Note**
The global access setting does not apply for users with the admin role.
Admins can always see all fact sheets and configure all access settings. Therefore, fact sheets created by an admin cannot be populated with access control information.
Admins always have to select the access settings when creating a new fact sheet. Otherwise the fact sheet is accessible to everyone across all virtual workspaces.
  1. In SAP LeanIX, navigate to Administration > Meta Model Configuration.
  2. Choose a fact sheet type.
  3. Choose Edit.
  4. In the configuration, choose your preferred setting from the Access Control dropdown.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2748a1387a441014ad5bb165a7051947_LowRes.png)
