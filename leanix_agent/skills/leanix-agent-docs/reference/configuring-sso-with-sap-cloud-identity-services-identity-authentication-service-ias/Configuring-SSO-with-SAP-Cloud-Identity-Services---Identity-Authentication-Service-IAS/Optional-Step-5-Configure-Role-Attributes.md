##  (Optional) Step 5: Configure Role Attributes
Create a user group in IAS to map it to role attributes from SAP LeanIX.
Standard user roles in SAP LeanIX are:
  * VIEWER
  * MEMBER
  * ADMIN


To learn more about roles and permissions, see [Standard User Roles](https://help.sap.com/docs/leanix/ea/user-roles-and-permissions?locale=en-US&state=PRODUCTION&version=CLOUD#loio275def827a4410149362f3672c614956__standard_user_roles).
### Create a Role Attribute in IAS
**Note**
You can't change group settings in IAS. If you want to edit a group, you need to delete it and create a new one.
  1. In IAS, navigate to Users & Authorizations > Groups.
![Screenshot showing the navigation to Users and Authorizations Groups in IAS.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio68c3a6f7a7394e56a3d39ae5090bea2f_LowRes.png)
Navigate to Groups
  2. Choose Create.
  3. Enter general information for the application, then choose Next Step.
  4. Select the application you created.
![Screenshot showing the application selection screen when creating a group in IAS.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loioc6ff081887424cac9fa8996087c751d7_LowRes.png)
Select Application
  5. Provide the External Name. This is equivalent to the role attribute in SAP LeanIX (for example, ADMIN or VIEWER). Ensure the spelling and capitalization are correct.
  6. For Group Type, select userGroup.
  7. Configure permissions in the Supported Operations field, then choose Next Step.
  8. Check the configuration summary, then choose Finish.


### Assign Role Attribute to User Groups
  1. In IAS, navigate to Users & Authorization > User Management > Groups.
  2. Select the group you created.
  3. Choose Add to add users to the group.
![Screenshot showing the Add button to add users to a group in IAS User Management.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio9814e7fad09f4dd4bb252db8e2798f91_LowRes.png)
Add Users to Group
  4. Select user groups.
  5. Choose Add to save.


### Assign Role Attribute to the IdP Application
Assigning a role works similarly to mapping the other SAML attributes.
  1. In IAS, navigate to Applications & Resources > Applications > [Your Application] > Attributes.
  2. Choose Add.
  3. Fill in the attribute name role.
  4. From the Source list, select Identity Directory.
  5. From the Value list, select the attribute Application Groups - External name.
  6. Choose Save.
