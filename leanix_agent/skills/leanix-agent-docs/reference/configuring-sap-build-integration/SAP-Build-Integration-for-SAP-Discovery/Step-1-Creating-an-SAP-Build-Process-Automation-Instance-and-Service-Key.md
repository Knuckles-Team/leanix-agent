##  Step 1: Creating an SAP Build Process Automation Instance and Service Key
If you are not yet using SAP Build Process Automation, follow the instructions in the following guides to set up the service:
  1. [Subscribe to SAP Build Process Automation (Standard Plan)](https://help.sap.com/docs/build-process-automation/sap-build-process-automation/subscribe-to-sap-build-process-automation-standard-plan?locale=en-US "https://help.sap.com/docs/build-process-automation/sap-build-process-automation/subscribe-to-sap-build-process-automation-standard-plan?locale=en-US")
  2. [Create an SAP Build Process Automation Service Instance](https://help.sap.com/docs/build-process-automation/sap-build-process-automation/create-service-instance?locale=en-US "https://help.sap.com/docs/build-process-automation/sap-build-process-automation/create-service-instance?locale=en-US")
     * Under **Service Plan** , select “standard”.
     * Under **Parameters** , add the following JSON parameters:

```
{"permissions":
                      ["buildtime.administer"],"authorized-environments":
                      ["$all"],"authorized-projects":
              ["$all"]}
```



  3. [Create a Service Key for the SAP Build Process Automation Instance](https://help.sap.com/docs/build-process-automation/sap-build-process-automation/create-service-key-for-sap-build-process-automation-instance?locale=en-US "https://help.sap.com/docs/build-process-automation/sap-build-process-automation/create-service-key-for-sap-build-process-automation-instance?locale=en-US")
