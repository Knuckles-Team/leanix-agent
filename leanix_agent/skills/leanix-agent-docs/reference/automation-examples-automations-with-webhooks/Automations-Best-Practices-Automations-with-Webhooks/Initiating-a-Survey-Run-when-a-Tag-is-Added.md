##  Initiating a Survey Run when a Tag is Added
When a specific tag, such as Survey Required, is added to a fact sheet, a survey run is initiated. This can be useful for automatically gathering feedback or additional information when required.
Set up an automation where the triggering event is Tag is added. The action is sending a webhook to a target URL. On your automation platform, set up a process to receive this webhook and initiate a survey run. To initiate a survey run, make a POST request to the following endpoint:

```
https://{SUBDOMAIN}.leanix.net/services/poll/v2/pollRuns
```



