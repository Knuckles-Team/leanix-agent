##  Case 8: Mapping SAP Signavio Attributes to Subscriptions
In this sample case, we will show how to synchronize SAP Signavio Attributes to add Subscriptions in SAP LeanIX Fact Sheets. Business Owner defined in SAP Signavio models will have a subscription to the corresponding Fact Sheet as role Process Owner with the type Responsible.
We set leanixType keyword as subscription, and add the field definitions for a Fact Sheet Subscription: email , type, role, and optionally comment, as shown in the JSON configuration:

```
{
 "inboundMappings": [
  {
   "leanixType": "subscription",
   "fields": [
    {
     "leanixFieldName": "email",
     "inboundPropertyPath": "${glossaryItem.get(editordata.model.properties['meta-processowner']).metaDataValues['meta-zustndigeemailadresse']}",
     "valueMappings": []
    },
    {
     "leanixFieldName": "type",
     "inboundPropertyPath": "RESPONSIBLE",
     "valueMappings": []
    },
    {
     "leanixFieldName": "comment",
     "inboundPropertyPath": "Subscription role added by Signavio integration",
     "valueMappings": []
    },
    {
     "leanixFieldName": "role",
     "inboundPropertyPath": "Process Owner",
     "valueMappings": []
    }
   ]
  }
 ]
}

```



  * leanixFieldName = email Field: Defines the data path to obtain the email address from SAP Signavio. This is a two steps process: first, obtain the data for the SAP Signavio Item that represents a Role for business Owner; and second, obtain the Glossary Item data associated with the previous reference. In the inboundPropertyPath expression , the data path editordata.model.properties['meta-processowner'] resolves to a value similar to "/glossary/<id>", which is then used by the symbol glossaryItem.get(...) to obtain a complete Glossary Item data object; then, the email is taken from the Glossary Item using the path .metaDataValues['meta-zustndigeemailadresse'].
  * leanixFieldName = type Field: Defines the value for the type of subscription.
  * leanixFieldName = role Field: Defines the value for the role of the subscription, in our example Process Owner.
  * leanixFieldName = comment Field: Defines the comment applied to the subscription.


It is necessary the SAP LeanIX administrator creates the Subscription Roles before the synchronization is executed, for this example the role to create is: Process Owner. Also, for every email that is obtained during the synchronization, it is expected that an SAP LeanIX user email already exists, otherwise the subscription will be ignored for that non-existing email address and a warning will be logged to Sync Logging.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2756249f7a4410148631b6194f89d0a0_LowRes.png)
