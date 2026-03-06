##  Step 1: Grant Permissions
To enable the connection between SAP LeanIX and Microsoft 365, grant the needed permissions.
Follow these steps:
  1. In SAP LeanIX, go to Administration > Notifications Center.
  2. For Email, choose Edit Settings, then go to the Custom Configuration tab.
  3. For Exchange Online, choose Edit Configuration.
  4. Enter your Microsoft Tenant ID, then choose Save.
  5. Copy the generated Consent Link and paste it into your browser to start the consent process, then review and approve the needed permissions.
**Note**
You need permissions to grant consent or can also forward the consent link to an administrator, for example, with global administration permission. The required permission level can vary depending on your Azure tenant setup.
![Microsoft permissions request screen for SAP LeanIX Email Notifications app.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loiofc01c2d1c2ab46a7968b19feea280081_HiRes.png)
Granting Permissions for an Application in Microsoft Exchange Online
While waiting for consent, you can view and refresh the status in SAP LeanIX.
  6. In Exchange Online, copy the Sender UPN and enter it on the configuration page in SAP LeanIX. The Sender UPN (user principal name) is the email address used to send email notifications.
![Configuration screen in SAP LeanIX showing fields for Exchange Online Tenant ID, Consent Link, and Sender UPN](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loioe53e8a7322084f5dbd2aaba15f6a9ee8_HiRes.png)
Entering Credentials for Microsoft Exchange Online in SAP LeanIX
  7. Choose Test Configuration.
  8. Choose Save.


**Caution**
Once you grant SAP LeanIX permission to send emails on behalf of your Microsoft 365 tenant, you can use any email address from your Exchange Online. However, as this poses a security risk, we recommend limiting access to a single mailbox. For details, see [Step 2: Configure Security Settings](https://help.sap.com/docs/leanix/ea/setting-up-microsoft-exchange-online-mailbox-for-email-notifications?locale=en-US&state=PRODUCTION&version=CLOUD#loio6f36fe677fa944d0b77be312e8c13d9e__section_u42_2jz_ygc).
