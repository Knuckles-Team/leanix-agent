##  Step 2: Grant Permissions to SAP LeanIX
After registering SAP LeanIX in Microsoft Entra ID, grant the necessary permissions to call APIs.
  1. Go to Entra ID > App registrations, and select your client application.
  2. Select API permissions > Add a permission > Microsoft Graph > Application permissions.
All permissions that apply to Microsoft Graph are shown under Select permissions.
  3. Select Application.Read.All.
![The Request API permissions screen with Application.Read.All selected in Microsoft Entra admin center.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio8e1b1161cf2f48ff9eb8bf3f2e5c7c36_LowRes.png)
Granting Permissions
  4. Choose Add permissions to save.
  5. On the API permissions page, choose Grant admin consent for MSFT to enable configured permissions.
![The API permissions page with Application.Read.All selected and Grant admin consent highlighted.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio6d94af3cb5f943ae8ca3e31429e46d11_LowRes.png)
Enabling Configured Permissions
  6. Choose Yes and grant consent for the requested permissions.
The permission status indicator in the API permissions page will change to approved.
