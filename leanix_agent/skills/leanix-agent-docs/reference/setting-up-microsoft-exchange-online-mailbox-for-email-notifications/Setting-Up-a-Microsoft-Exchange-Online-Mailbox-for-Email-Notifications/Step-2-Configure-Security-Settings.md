##  Step 2: Configure Security Settings
To ensure notifications are sent only from a specific mailbox, limit SAP LeanIX access to that mailbox. Microsoft recommends that you use the new role based access control (RBAC) instead of the legacy Application Access Policies. To learn more about the RBAC approach, visit the [Microsoft documentation![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fexchange%2Fpermissions-exo%2Fapplication-rbac "https://learn.microsoft.com/en-us/exchange/permissions-exo/application-rbac").
You can use the provided PowerShell commands to configure the mailbox. First, you gather relevant data. Then you update these values in the sample script before executing.
**Caution**
These steps replace the legacy Application Access Policies with the new RBAC approach recommended by Microsoft.
### Collect the Required Data
  1. Go to your Azure Portal Azure Active Directory Enterprise Applications.
  2. Search for and select "SAP LeanIX Email Notifications". ![Azure portal in the Enterprise applications section showing search results for SAP LeanIX Email Notifications](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loioe04a25cca81149cc97a52858a992b306_HiRes.png)
  3. On the overview page copy:
     * Application ID
     * Object ID
  4. Define your input to replace the following placeholders that you'll see in PowerShell commands in the next steps:
     * <LeanIXNotificationMailboxScope> is the name you want to use for the management scope.
     * <senderUPN> is the email address you want to allow as a sender.
     * <Your-AppId> is the Application ID from Azure.
     * <Your-ServiceID> is the Object ID from Azure.


### Running the PowerShell Commands
**Note**
Some of the commands below include placeholders (for example, <LeanIXNotificationMailboxScope>, <senderUPN>, <Your-AppId>).
Before running those commands:
  * Replace only the text inside the angle brackets with your values.
  * Remove the angle brackets.
  * Keep any quotation marks (" ") in the command, and insert your value inside the quotes, for example "<LeanIXNotificationMailboxScope>" > "acmeNotificationMails".


Copy and run commands without placeholders as shown.
  1. Launch your terminal and start the PowerShell.

```
pwsh
```



  2. Connect to Exchange Online PowerShell.

```
Connect-ExchangeOnline
```



In the browser that opens, sign in with administrator credentials.
  3. Go back to the terminal and enable organization customization.

```
Enable-OrganizationCustomization
```



This is required to create custom management scopes. It can take several minutes.
  4. Verify that the customization is working.

```
Write-Host $(if ((Get-OrganizationConfig).IsDehydrated -eq $false) {"Organization customization is enabled."} else {"Warning: Organization customization is still processing. Wait for a few minutes and retry."}) -ForegroundColor $(if ((Get-OrganizationConfig).IsDehydrated -eq $false) {"Green"} else {"Red"})
```



  5. Create custom management scopes to restrict mailbox access and provide the email address that you want to use for sending notifications.

```
New-ManagementScope -Name "<LeanIXNotificationMailboxScope>" -RecipientRestrictionFilter "EmailAddresses -eq '<senderUPN>'"
```



  6. Register the SAP LeanIX service principal with Exchange Online. This informs Exchange Online about SAP LeanIX. You can then assign permissions in the next step.

```
New-ServicePrincipal -AppId <Application-ID> -ServiceId <Object-ID>
```



  7. Use the custom scope to restrict access to one email address.

```
New-ManagementRoleAssignment -Role "Application Mail.Send" -App <Application-ID> -CustomResourceScope "<LeanIXNotificationMailboxScope>"
```



  8. Verify that the scope is set up.
    1. Confirm scoped role assignment.

```
Get-ManagementRoleAssignment -RoleAssignee <Application-ID> | Format-List Name, Role, CustomResourceScope
```



The output shows CustomResourceScope with your scope name.
    2. Verify that sender mailbox is authorized.

```
Test-ServicePrincipalAuthorization -Identity <Application-ID> -Resource "<senderUPN>"
```



The output shows InScope: True.
    3. List all mailboxes that the application is allowed to send from.

```
Get-Recipient -RecipientPreviewFilter (Get-ManagementScope -Identity "<LeanIXNotificationMailboxScope>").RecipientFilter | Format-List DisplayName, PrimarySmtpAddress
```



  9. Optionally, disconnect.

```
Disconnect-ExchangeOnline -Confirm:$false
```





### Revoke Mail.Send Permissions in Microsoft Entra ID
**Note**
This step is required for the scope restriction to take effect. Without it, the Azure AD permission overrides the RBAC scope.
  1. Go to Azure Portal Microsoft Entra ID Enterprise Applications.
  2. Go to the Permissions tab.
  3. Under Admin consent, find the Mail.Send permission.
  4. Choose More options (…) Revoke permission.
A confirmation dialog box opens.
  5. In the dialog box, choose Confirm.
After revoking, the application can only send emails from the mailbox specified in your custom scope.


Revoking Permissions in the Microsoft Azure Portal
![The Azure Portal Permissions tab showing the option to revoke the Mail.Send permission.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio186890a78fab4eeab65fa0f1ea404820_LowRes.png)
