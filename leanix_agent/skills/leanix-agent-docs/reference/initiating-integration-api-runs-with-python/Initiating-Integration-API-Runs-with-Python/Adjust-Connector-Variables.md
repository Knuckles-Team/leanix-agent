##  Adjust Connector Variables
The variables on lines 69 - 74 are used to identify the proper Workspace and Connector to be triggered by the script.
  * Variables connectorType, connectorId, connectorVersion, processingDirection, and processingMode should all be adapted to match the Connector you want to trigger and can be found within the Integration API user interface (Admin > Integration API).
  * lxWorkspace should be set to your workspace ID, which can be found in Admin > API Tokens.


![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27478a597a44101489529eaea3171025_LowRes.png)
**Note**
For detailed information about the LDIF configuration elements, visit [Mandatory Attributes](https://help.sap.com/docs/leanix/ea/integration-api?locale=en-US&state=PRODUCTION&version=CLOUD#loio275a99087a441014a04fa6cda4e0ec2b__mandatory_attributes).
With these variables in place, you can run the script and it will call the Integration API, initiating a 'run' of the processor indicated per your configured variables. The data retrieved from the run will be saved in the same directory as your copy of initiateOutboundRun.py in a file called leanixOutboundData.json
