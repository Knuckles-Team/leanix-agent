##  Access Control Behavior for Different User Roles
User role permissions, such as viewer, member, or admin take precedence over the virtual workspaces. Depending on the user role, the read/write settings apply differently.
User Role | Read/Write Access Behavior
---|---
Viewer | Viewers cannot edit anything, but they can see fact sheets for their virtual workspaces.
Member | Members can see and edit fact sheets in their virtual workspace. When a member creates a new fact sheet, it is created with with the member’s access settings. Members cannot see the access control configuration and therefore cannot change these settings. See [User Flow for a Member Creating a New Fact Sheet](https://help.sap.com/docs/leanix/ea/virtual-workspaces?locale=en-US&state=PRODUCTION&version=CLOUD#loio275e04b57a4410149370f49e62aa038f__user_flow_for_a_member_creating_a_new_fact_sheet)
Admin | Admins can see and edit all fact sheets in all virtual workspaces. Admins can change the access control settings for the meta model and the fact sheet. See [User Flow for an Admin Creating a New Fact Sheet](https://help.sap.com/docs/leanix/ea/virtual-workspaces?locale=en-US&state=PRODUCTION&version=CLOUD#loio275e04b57a4410149370f49e62aa038f__user_flow_for_an_admin_creating_a_new_fact_sheet)


