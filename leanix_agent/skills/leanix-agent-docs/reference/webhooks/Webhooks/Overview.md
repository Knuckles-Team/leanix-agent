##  Overview
Webhooks let you receive updates about events as they happen in near real time in SAP LeanIX. With webhooks, you can set up event-driven triggers that initiate automated actions, which allows you to automate workflows for your organization and eliminate manual processes.
We support the following webhook types, based on the event delivery method:
  * PUSH webhooks: As events occur in SAP LeanIX, they're sent through HTTP POST requests to the specified target URL. This is the recommended way to receive events from SAP LeanIX.
  * PULL webhooks: A client requests events by polling a REST endpoint on the SAP LeanIX API. This method of retrieving events is useful if your environment doesn't allow exposing a public HTTP server to receive events, such as when your application operates behind a firewall. Events are retained on the server for 30 days, but it's recommended to retrieve them more regularly.


The following image illustrates how PUSH and PULL webhooks work.
![Workflows for Data Retrieval Using PUSH and PULL Webhooks](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27498a0a7a44101480d58f637ab18a2d_LowRes.png)
Workflows for Data Retrieval Using PUSH and PULL Webhooks
