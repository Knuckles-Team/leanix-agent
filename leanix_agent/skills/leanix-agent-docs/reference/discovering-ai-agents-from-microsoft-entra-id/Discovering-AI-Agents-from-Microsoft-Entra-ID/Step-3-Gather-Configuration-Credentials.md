##  Step 3: Gather Configuration Credentials
  1. Return to the overview page for the created app and copy the following identifiers:
    1. Application (client) ID
    2. Directory (tenant) ID
![The Microsoft Entra admin center showing Application and Directory IDs highlighted.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loiodaff1d5357f9459c9469524477b2919a_LowRes.png)
Where to Find the App and Directory IDs
  2. Go to Certificates & secrets > New client secret to create a new password.
    1. Enter a description for the client secret.
    2. Select the expiration length of the secret.
When the client secret expires, an error message appears on the integration overview page in SAP LeanIX. You'll need to create a new secret and reconfigure the integration in SAP LeanIX.
    3. Choose Add.
![The Add a client secret panel open in Microsoft Entra admin center.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loioe23b9fe3ff6545a9b458590e1f4f887c_LowRes.png)
Adding a Client Secret
  3. Copy the client secret value from the Value field.
**Note**
Save the client secret value as soon as it's revealed. After you leave the page, the value will not appear again.
