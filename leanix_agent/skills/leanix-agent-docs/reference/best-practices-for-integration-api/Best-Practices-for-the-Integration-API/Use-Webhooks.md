##  Use Webhooks
Our tutorial on [Sending Alerts to Slack and Microsoft Teams](https://help.sap.com/docs/leanix/ea/sending-alerts-to-slack-and-microsoft-teams?locale=en-US&state=PRODUCTION&version=CLOUD "Set up a webhook to receive notifications about failed events in your integration runs.") can be used to set up alerts for Integration API runs that occur on a recurring basis.
One way to do this could be to have a separate slack channel wherein successful or unsuccessful runs are sent with a different emoji in their payload.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27576d147a44101495f7cbec566d1433_LowRes.png)

```
{
 "deliveryType": "PUSH",
 "id": "",
 "identifier": "Integration Statistics to Slack",
 "tagSets": [
  [
   "integrations",
   "statistics"
  ]
 ],
 "createdAt": "2020-06-10T15:17:11.064809Z",
 "workspaceId": "[Workspace ID from API Token section",
 "userId": "[User ID from API Token Section]",
 "targetUrl": "[SLACK TARGET URL]",
 "targetMethod": "POST",
 "authorizationHeader": "",
 "callback": "var payload = delivery.payload;delivery.active = false;var base_url = 'https://eu.leanix.net/WORKSPCENAME/';if((payload.progress == 'FINISHED') && (payload.connectorId == 'ConnectorID-3' || payload.connectorId == 'ConnectorID-1' || payload.connectorId == 'ConnectorID-2')){delivery.active = true;var text = ':SLACK EMOJI: '+'*Workspace:* WORKSPACE_NAME '+ '*Connector Id:* '+payload.connectorId+' *Scope:* '+ payload.scope+' *Connector Direction:* '+ payload.direction+' has *Status:* '+ payload.progress+' and *error count:* '+ payload.errorCount;text += ' *Synclog link :* '+base_url+'/admin/synclog/'+ payload.synchronizationId;}delivery.payload = {text : text}",
 "lastDeliveryStatus": 200,
 "ignoreError": false,
 "maxBatchSize": 512,
 "workspaceConstraint": "WORKSPACE",
 "active": true,
 "errorCount": 0,
 "firstTimeDeliveryFailed": null,
 "payloadMode": "DEFAULT"
}
```



![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274707907a441014b96afc4b9c3a97d2_LowRes.png)
