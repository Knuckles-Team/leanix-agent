##  Access Control for Virtual Workspaces
The following components work together to achieve effective access control management:
  * Virtual workspaces:
Virtual workspaces represent logical or organizational units within your organization. Such a unit could be a region, for example Americas or APAC. You define virtual workspaces based on the user groups you want to manage access for.
  * Access control entities:
Access control entities represent virtual workspaces. To create a workspace, you add a new access control entity. For example, the access control entity APAC creates the virtual workspace for the region APAC.
Access control entities are key to managing the access. You list all your access control entities in the ACL and assign them to users and to fact sheets.
  * User groups:
You assign users to access control entities. A user can belong to one or more entities, or none at all. You can combine several different access control entities to represent where the user needs access. You perform the assignment in your IdP through Active Directory (AD) user groups.
  * Fact sheets:
To apply access control, you assign access control entities to fact sheets. Once assigned, fact sheets belong to virtual workspaces. For every access control entity you specify read or write permissions for a fact sheet.
  * Access control list (ACL):
The ACL brings together all the access rights you configure for users and fact sheets. When a user logs in to SAP LeanIX, their details are checked including access permissions from the ACL. Only users that match the access control entities of the fact sheet are given read/write access to a fact sheet.


![Checking for Matching Access Control Entities](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274cc20f7a4410149fb89710c901e1ac_LowRes.png)
Checking for Matching Access Control Entities
Together, the access control entity assignment for each user and for each fact sheet create the unique virtual workspaces for each user. The user will see all fact sheets of each access control entity. The more access control entities a user is assigned to, the more fact sheets the user can access. Additionally, all fact sheets without any restrictions are accessible for all users in all virtual workspaces. By limiting access to fact sheets, you give your users focus.
To start configuring virtual workspaces see See [Virtual Workspace Configuration](https://help.sap.com/docs/leanix/ea/virtual-workspaces-configuration?locale=en-US&state=PRODUCTION&version=CLOUD "Set up virtual workspaces to manage access for custom user groups").
![Unique Virtual Workspaces for Each User](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio275473e07a441014914186a177b3927c_LowRes.png)
Unique Virtual Workspaces for Each User
