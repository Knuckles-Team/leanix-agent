##  Authentication and Authorization
### Authentication
Authentication is the process of verifying the identity of a user or system attempting to access SAP LeanIX. Users provide credentials to confirm their identity and gain access.
You have two options for managing authentication:
  * SAP LeanIX (without SSO): You manage access directly in SAP LeanIX. Users sign in to your workspace using their email and password on the sign-in page.
  * SSO: You manage access through your identity provider (IdP) system. Users sign in through your IdP, which eliminates the need for separate credentials.


### Authorization
Authorization determines what actions an authenticated user is allowed to perform in SAP LeanIX. It involves assigning specific roles and permissions that define the data and features users can access.
In SAP LeanIX, you manage permissions by assigning user roles. These roles define each user's access level within the workspace. For more details, see [User Roles and Permissions](https://help.sap.com/docs/leanix/ea/user-roles-and-permissions?locale=en-US&state=PRODUCTION&version=CLOUD "Adjust role-based permissions and define custom roles.").
You have two options for managing authorization:
  * SAP LeanIX: You manage user roles directly in SAP LeanIX.
    * If SSO is not enabled in your workspace, you always manage user roles in SAP LeanIX.
    * If SSO is used only for authentication, you manage user roles in SAP LeanIX.
  * SSO: If you use SSO for both authentication and authorization, you manage user roles in your IdP system.


**Note**
When setting up SSO, decide whether to use it for authentication only or for both authentication and authorization. For more information, see [Single Sign-On (SSO)](https://help.sap.com/docs/leanix/ea/single-sign-on-sso?locale=en-US&state=PRODUCTION&version=CLOUD "Learn how to configure single sign-on \(SSO\) with SAP LeanIX.").
