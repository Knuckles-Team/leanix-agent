##  Safety Net for Survey Notifications
The safety net feature is designed to prevent unintended mass notifications.
When a survey is run with a dynamic scope, it automatically includes fact sheets that meet specified filters. Additionally, changes in fact sheet subscriptions are monitored continuously, and subscribers are invited to participate in the survey.
The system checks for changes every hour, automatically updating and notifying survey recipients when there is any change. This time-saving feature may also lead to unintended mass notifications, for example, when you update a large number of fact sheets for an unrelated task. The safety net feature prevents unintended mass notifications in such situations.
The safety net is enabled by default for all workspaces, with a default threshold set at 100. During the hourly check, if the system detects 100 or more new recipients added to a survey in a single check cycle, it temporarily halts sending out survey notifications to recipients and notifies the survey creator about the affected survey run.
![Safety Net to Prevent Unintended Mass Notifications](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274490c27a441014844bb02ef956ab85_LowRes.png)
Safety Net to Prevent Unintended Mass Notifications
