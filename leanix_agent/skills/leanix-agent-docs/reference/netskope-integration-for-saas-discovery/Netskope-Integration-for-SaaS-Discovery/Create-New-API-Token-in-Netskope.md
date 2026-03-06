##  Create New API Token in Netskope
  1. Log in to Netskope with an Admin account.
  2. Navigate to Settings > Tools > REST API v2, then click New token.
![Creating a New API Token](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2750f7b87a4410149065808f13b0c818_LowRes.png)
Creating a New API Token
  3. In the token creation modal:
    1. Enter a name for the token.
    2. Choose an expiration time based on your requirements (longer for convenience, shorter for security). Note that expired tokens must be updated manually.
    3. Add /api/v2/events/data/application scope/endpoint.
    4. Click Save.
![Adding the API Endpoint](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2747eee77a441014a2368481762e8ca0_LowRes.jpg)
Adding the API Endpoint
  4. Click Copy token and save the API token for future use. Note that once the modal is closed, the token cannot be accessed again and will need to be regenerated if required.

![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274c12ec7a441014866e8bd47d1ff6b0_LowRes.png)
