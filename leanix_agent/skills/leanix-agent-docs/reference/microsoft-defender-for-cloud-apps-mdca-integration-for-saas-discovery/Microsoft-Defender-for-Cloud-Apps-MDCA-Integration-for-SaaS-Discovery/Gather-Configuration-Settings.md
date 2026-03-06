##  Gather Configuration Settings
  1. Return to the application overview section (App registrations > Created app) and gather the following identifiers: Application (client) ID and Directory (tenant) ID.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2754aa9d7a4410149f3db84e6be0c082_LowRes.png)
  2. From the left pane, open the Certificates & secrets section. Here, generate a client secret (also called the application password) by following these steps:
    1. Click New client secret to create a new password.
    2. Optionally, enter a description for the client secret.
    3. Select the expiration length of the secret. Once the expiration date of the created client secret is reached, you need to create a new one and reconfigure the integration in SAP LeanIX.
    4. Click Add.
![Adding a Client Secret](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2752b0f57a441014b8a9d5c8da368d76_LowRes.png)
Adding a Client Secret
  3. Copy the client secret value to your clipboard.
![Copying the Client Secret Value](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2742a1787a44101484aac22ad31bb068_LowRes.png)
Copying the Client Secret Value
  4. Go to the MDCA product, navigate to Settings > Cloud Apps > System > About, and copy the API URL value.
![Copying the API URL Value](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2747973e7a4410149f43c5fa78491054_LowRes.png)
Copying the API URL Value
