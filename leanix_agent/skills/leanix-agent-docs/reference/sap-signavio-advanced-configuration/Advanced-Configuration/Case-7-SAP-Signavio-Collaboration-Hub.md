##  Case 7: SAP Signavio Collaboration Hub
To be able to go to the SAP Signavio Collaboration Hub directly from the SAP LeanIX interface we need to add a new custom field to the specified process fact sheet and configure a inbound mapping. The custom field has to be called collaborationHubUrl. And the inbound mapping configuration is shown below:

```
{
 "inboundMappings": [
  {
   "leanixType": "factSheetField",
   "fields": [
    {
     "leanixFieldName": "collaborationHubUrl",
     "inboundPropertyPath": "${model.status.publish}",
     "valueMappings": [
      {
       "outputExpression": "https://editor.signavio.com/p/hub-preview#model/${editordata.modelId}",
       "regexMatch": "true"
      },
      {
       "outputExpression": "",
       "regexMatch": "false"
      }
     ]
    }
   ]
  }
 ]
}

```



In our example the link to the SAP Signavio Collaboration Hub is only shown when the model is published. The two possible values for model.status.publish are true or false, using the valueMappings we are filtering the cases for true to have the URL that points to SAP Signavio Collaboration Hub. To build a URL for each model we need to add the id from editordata.modelId. The domain as well as the path in the URL might be different for your SAP Signavio setup.
After the synchronization, all published models will be shown with a Collaboration Hub link in the SAP LeanIX interface:
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274fd0b57a441014bf24ddc4b1e9877d_LowRes.png)
