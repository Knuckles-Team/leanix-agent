##  Step 1: Prepare Your Environment
Follow these steps:
  1. Clone SAP LeanIX public scripts.
    1. Clone the SAP LeanIX [repository with scripts![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fgithub.com%2Fleanix-public%2Fscripts "https://github.com/leanix-public/scripts").
    2. Go to the [timeModelSync folder![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fgithub.com%2Fleanix-public%2Fscripts%2Ftree%2Fmaster%2FtimeModelSync%2FazureFunctionApp%2FtimeModelSync "https://github.com/leanix-public/scripts/tree/master/timeModelSync/azureFunctionApp/timeModelSync").
  2. Create an Azure Function app. You can use one of the following options to create an app on your Azure Environment:
     * [Command Line![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fazure%2Fazure-functions%2Ffunctions-create-first-azure-function-azure-cli%23create-a-function-app "https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-azure-function-azure-cli#create-a-function-app")
     * [Azure Portal![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fazure%2Fazure-functions%2Ffunctions-create-first-azure-function%23create-a-function-app "https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-azure-function#create-a-function-app")
  3. Deploy the project to your environment.

```
func azure functionapp publish timeModelSync
```



Copy the Invoke URL that is posted in your console after the successful deployment.
