##  Case 6: Tagging Fact Sheets using SAP Signavio Attributes
In this sample case, we want to map the value of publish attribute in SAP Signavio to be applied as a tag in SAP LeanIX. To synchronize SAP Signavio attributes into Fact Sheet tags, we have to define the fields that compose a Tag: name and group, also set the leanixType to tag. The following JSON configuration data shows an example of synchronization to tags.

```
{
 "inboundMappings": [
  {
   "leanixType": "tag",
   "fields": [
    {
     "leanixFieldName": "group",
     "inboundPropertyPath": "PublishStatus",
     "valueMappings": []
    },
    {
     "leanixFieldName": "name",
     "inboundPropertyPath": "${model.status.publish}",
     "valueMappings": [
      {
       "outputExpression": "published",
       "regexMatch": "true"
      },
      {
       "outputExpression": "non-published",
       "regexMatch": "false"
      }
     ],
     "defaultValue": "",
     "ignoreUnknownProperty": true
    }
   ]
  }
 ]
}

```



New Fact Sheets will be tagged as published or non-published depending of the value from SAP Signavio publish attribute. The tag group for all Fact Sheets will be PublishStatus. It is necessary that the Tag Group and Tags are created by the Administrator before the synchronization, the bellow image shows the tag groups for this example:
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2748dea37a441014bd6ad91d8581026d_LowRes.png)
Both fields group and name are resolved using the same mechanism explained in previous sections, which consists in taking the value from inboundPropertyPath and use it together with valueMappings list to calculate the final result. In our example the group is resolved as a static text: PublishStatus, and the name of the tag is based on the value mapping of the model.status.publish value.
After the synchronization, the Fact Sheet created has the tag non-published because the SAP Signavio attribute model.publish was false.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2752505a7a441014b407df4a8d25d528_LowRes.png)
**Note**
Tagging Mode Multiple/Single
In order to remove the existing tags when a new tag is supposed to be applied recommendation is to use mode "Single"
