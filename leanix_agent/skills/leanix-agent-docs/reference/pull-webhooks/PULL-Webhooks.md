# PULL Webhooks
### On this page
  * [Intended Usage](https://help.sap.com/docs/leanix/ea/pull-webhooks#intended-usage)
  * [Concurrency](https://help.sap.com/docs/leanix/ea/pull-webhooks#concurrency)
  * [Event Availability](https://help.sap.com/docs/leanix/ea/pull-webhooks#event-availability)
  * [Automatic Deactivation of PULL Webhooks](https://help.sap.com/docs/leanix/ea/pull-webhooks#automatic-deactivation-of-pull-webhooks)
  * [Retrieving Events](https://help.sap.com/docs/leanix/ea/pull-webhooks#retrieving-events)
  * [Moving the Cursor](https://help.sap.com/docs/leanix/ea/pull-webhooks#moving-the-cursor)


Request events by polling an API endpoint.
With PULL webhooks, a client requests events by polling an endpoint on the SAP LeanIX Webhooks API.
When configuring a PULL webhook, you can optionally adjust the maximum batch size that defines a soft upper limit for data in each event batch. The default maxBatchSize value is 512 KB. Usually, batches don't exceed the specified size limit. However, a single event exceeding this limit will still be delivered.
