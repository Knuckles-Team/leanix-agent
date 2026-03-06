##  Starting a Synchronization Run
After deploying the GitHub agent, a full synchronization between the systems starts automatically. Any changes to the integration that trigger a webhook, such as a new installation or an update to the manifest file, start an automatic full synchronization.
You can manually run a full synchronization if needed. This may be useful in situations such as:
  * GitHub data in SAP LeanIX appears outdated or incomplete.
  * The webhook delivery failed or was temporarily disabled.
  * Repositories were added or changed outside regular sync mechanisms.


To start a full synchronization, follow these steps:
  1. Go to the GitHub integration configuration page.
  2. In the upper-right corner, choose the three-dot icon, then choose Run Full Sync.


**Note**
You can run only one full synchronization for an integration instance at a time.
