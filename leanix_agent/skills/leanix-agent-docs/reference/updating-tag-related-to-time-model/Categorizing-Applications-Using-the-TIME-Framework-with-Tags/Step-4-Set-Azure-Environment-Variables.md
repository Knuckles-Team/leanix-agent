##  Step 4: Set Azure Environment Variables
  1. Create an environment variable in your Azure portal called "HOST " and set it to your host (e.g. app.leanix.net)
  2. Paste the following JSON into an environment variable called "TAG_MAPPING" with the correct ids for your workspace.



```
{
    "tolerate": "<tag id>",
    "invest": "<tag id>",
    "migrate": "<tag id>",
    "eliminate": "<tag id>"
}
```



**Tip**
To save your API token for a live environment SAP LeanIX advises you to use the [Microsoft KeyVault![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fazure.microsoft.com%2Fde-de%2Fservices%2Fkey-vault%2F "https://azure.microsoft.com/de-de/services/key-vault/"). Create a link to the Key Vault from an environment variable called: "DEMO_TOKEN"
Now you are ready to use the Azure Functions and run some tests by changing values of the Functional Fit and Technical Fit. The corresponding tags are assigned to fact sheets.
YesNo
Send
