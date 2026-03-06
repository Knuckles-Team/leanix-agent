##  Step 4: Configure Attribute Mapping
  1. In IAS, navigate to Applications & Resources > Applications > [Your Application] > Attributes.
![Screenshot showing the navigation to Attributes settings for an application in IAS.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio6bcf26da9a904c3694412a007fc87ccb_LowRes.png)
Navigate to Attributes
  2. Remove the provided default attributes. Choose Expand All and then delete all entries. The attributes are now empty.
  3. Add the LeanIX attributes as shown in the following table. All fields are case-sensitive. For more information, see [Attribute Mapping](https://help.sap.com/docs/leanix/ea/single-sign-on-sso?locale=en-US&state=PRODUCTION&version=CLOUD#loio275cc8227a441014a371975e4b816f0a__attribute-mapping).


Required Attributes Name | Source | Value
---|---|---
firstname | Identity Directory | First Name
lastname | Identity Directory | Last Name
email | Identity Directory | Email
uid | Identity Directory | Email


The following table lists the attributes that you need when using SSO for authentication and authorization. In this scenario, you manage user roles in IAS.
Optional Attributes Name | Source | Value
---|---|---
role | Identity Directory | Application Groups - External Name
customer_roles | Identity Directory | Application Groups - External Name
ace | Identity Directory | Application Groups - External Name


  1. Choose Save.
![Screenshot showing the completed attribute configuration with the Save button in IAS.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio76be42c1f4bb4c81902138d29f08e633_LowRes.png)
Save Attributes Configuration
