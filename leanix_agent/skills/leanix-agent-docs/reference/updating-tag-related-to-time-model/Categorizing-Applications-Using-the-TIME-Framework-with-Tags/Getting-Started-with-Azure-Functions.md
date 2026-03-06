##  Getting Started with Azure Functions
As defined by [Microsoft![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fazure%2Fazure-functions%2Ffunctions-overview "https://docs.microsoft.com/en-us/azure/azure-functions/functions-overview"), Azure Functions is a serverless solution that allows you to write less code, maintain less infrastructure, and save on costs. Instead of worrying about deploying and maintaining servers, the cloud infrastructure provides all the up-to-date resources needed to keep your applications running.
Azure Functions are triggered by specific events that you define.
### Create an Azure Function
You can use one of the below options to create an Azure Function:
  * [Visual Studio Code![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fazure%2Fazure-functions%2Ffunctions-create-first-function-vs-code%3Fpivots%3Dprogramming-language-python "https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-function-vs-code?pivots=programming-language-python")
  * [Visual Studio![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fazure%2Fazure-functions%2Ffunctions-create-your-first-function-visual-studio "https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-your-first-function-visual-studio")
  * [Command line![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fazure%2Fazure-functions%2Ffunctions-create-first-azure-function-azure-cli "https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-azure-function-azure-cli")
  * [Maven (Java)![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fazure%2Fazure-functions%2Ffunctions-create-first-java-maven "https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-java-maven")


Upon creation of the Azure Function you will receive a unique endpoint which can be used to invoke the function and will be used in the Webhooks configuration at a later point. You can also use the link highlighted below to get your Function URL.
![Get Function URL](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274bf3847a441014a602a24c2fbd9a21_LowRes.png)
Get Function URL
### Connect SAP LeanIX to Azure Function
  * Once you have created an Azure Function from the above section you can create a webhook in SAP LeanIX.
  * Updated the Target URL in the above as per the one available from Azure Function created above.
  * You can use a callback to determine what you want to send to Azure Function.
