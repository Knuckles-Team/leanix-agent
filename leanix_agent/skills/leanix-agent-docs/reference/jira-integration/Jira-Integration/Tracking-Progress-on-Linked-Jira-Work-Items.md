##  Tracking Progress on Linked Jira Work Items
You can track progress directly in the **Execution progress** field of child initiatives created from Jira. This helps you understand how much work you’ve completed on an initiative. Progress information is updated as part of the regular sync schedule.
To ensure consistent tracking, SAP LeanIX includes only the first level of child work items under each initiative in the progress calculation.
**Caution**
If you close a top-level item in Jira, such as an epic or parent task, SAP LeanIX will mark it as 100% complete, even if some of its child items are still open. This is designed to streamline reporting but can lead to inaccurate progress tracking.
Make sure all child items are complete before closing the top-level work item.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio0d1a968f796345cf9f57e9c4962f151b_LowRes.png)
Execution Progress Tracking
**Tip**
Use the roadmap report to track the progress of synced Jira work items. It gives you a clear, timeline-based view of initiatives, helping you align execution with strategic goals. Learn more in the article [Roadmap Report](https://help.sap.com/docs/leanix/ea/roadmap-report?locale=en-US&state=PRODUCTION&version=CLOUD).
Progress is calculated using the following formula:
Execution progress (%) = (Completed work items / Total work items) × 100
**Example**
A user imports 5 epics into an initiative fact sheet. Each epic contains 10 stories, with 5 completed per epic:
5 epics × 10 stories = 50/100 → 50% progress
SAP LeanIX counts only the first level of child work items under an initiative fact sheet created from Jira.
