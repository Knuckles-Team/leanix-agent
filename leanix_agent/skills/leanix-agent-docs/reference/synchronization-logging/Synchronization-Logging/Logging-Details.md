##  Logging Details
To view logs for a specific synchronization run, on the Synchronization Logging page, click the link in the Date column. You land on the Logging details page that displays synchronization logs, providing a comprehensive view of the synchronization process for analysis and troubleshooting.
Synchronization logs capture the sequence of actions performed during a synchronization run. Each log entry records details such as the action type, status, and timestamp, allowing you to trace the execution flow and identify any issues.
![Logging details page showing a list of actions for a synchronization run](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274cf3467a441014b411d95bfe50269c_LowRes.png)
Logging Details Page Showing a List of Actions for a Synchronization Run
Synchronization Log Details Parameter | Description
---|---
Date | The date and time when the synchronization action started.
Source and Target | The source and target of the synchronization action and their identifiers. The source and target depend on the data flows configured in the integration.
Action |  The action of the operation:
  * If there is a mismatch in data between the systems, the action reflects the corresponding operation: CREATE, UPDATE, or DELETE.
  * If there is no mismatch in data, the action is NONE.


Status | The status of the action: OK, ERROR, WARNING, or INFO. Learn more about [why synchronizations fail](https://help.sap.com/docs/leanix/ea/synchronization-logging?locale=en-US&state=PRODUCTION&version=CLOUD#loio275d86a77a4410149a3cc45e299aa022__why_synchronizations_fail).
Message | The details of the synchronization action. To view full details of the operation, click the message. You can copy the message to your clipboard to initiate troubleshooting.


