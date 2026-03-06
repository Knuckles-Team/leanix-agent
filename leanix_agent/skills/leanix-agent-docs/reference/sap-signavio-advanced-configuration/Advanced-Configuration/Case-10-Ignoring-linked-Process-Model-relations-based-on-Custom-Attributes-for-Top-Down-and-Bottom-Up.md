##  Case 10: Ignoring linked Process Model relations based on <Custom Attributes> for Top-Down and Bottom-Up
SAP Signavio offers linkage of diagrams (eg: process models) against each other based on a special custom attributes type Diagram Link. Some customers uses this way of linkage to express a special relationship between objects. Such a custom attribute can be defined in <Setup / Define notation/attributes>, like:
![907](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274ad9d17a441014b651edb10376efa9_LowRes.png)
Configuration of a customer attribute used to link another diagram.
In case a Process Model should be linked via a custom attribute, the linkage must be done inside the Custom Attributes area at the right side of the screen. For instance this looks like:
![497](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27549c3a7a44101483508c63531311a4_LowRes.png)
Setting a link to another process model using a custom attribute.
There are two methods for filtering relations, giving you enhanced control and flexibility over the synchronization process.
  * **Excluding custom attributes that contain links:** Use this method when specific custom attributes in your diagrams serve linking purposes but shouldn't be part of the hierarchy, such as in navigation relations.
  * **Excluding shapes that carry relations** :Use this method when certain shapes in your diagrams, regardless of type, have relations that shouldn't be included in the process hierarchy relations within SAP LeanIX.


### Excluding Custom Attributes with Links
To exclude relations coming from specific custom attributes for the top-down or bottom-up synchronizations, list the technical IDs of the attributes in excludeCustomRelationsAttributeIds. This parameter is mutually exclusive with excludeCustomRelations.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio5f1e699b904441c88329e066d55d258b_LowRes.png)
In the following JSON configuration, we exclude created relations by using two custom attributes with technical IDs: vorgngerprozesse and nachfolgerprozesse. These attributes come from the start and end event shapes in SAP Signavio Process Manager.

```
{
 "processSyncDescriptors": [
  {
   "inboundMappings": [],
   "active": true,
   "directoryIds": [
    "10d342f5db704199968d86688c528073"
   ],
   "linkProcessingMode": "PARENT_CHILD",
   "publishedOnly": false,
   "startNodeId": null,
   "filterExpression": null,
   "leanixParentFactSheetId": null,
   "blacklist": [],
   "shortDescription": "",
   "excludeCustomRelationsAttributeIds": [
    "vorgngerprozesse",
    "nachfolgerprozesse",
   ],
  }
 ]
}
```



### Excluding Shapes with Links
For a more granular filtering of relations, you can exclude them at the shape level based on a specific custom attribute for the top-down or bottom-up synchronization. To do this, set excludeRelationByCustomShapeAttribute to true and provide the technical IDs of attributes in excludeRelationByCustomShapeAttributeId.
In SAP Signavio, the created attribute must be of type Boolean and set to meta-excludefromleanixsync by default. This technical ID corresponds to a custom attribute named excludeFromLeanIXSync. When the attribute value is set to true on any shape that links to another process, the relation isn't created in SAP LeanIX. In the image below, we created a custom attribute for the "Intermediate Link Event BPMN 2.0" diagram element type and reused it for the "Collapsed Subprocess BPMN 2.0" diagram element type. This approach allows you to exclude "native" relations as well.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio7a953cc2cf314985a773b33c242fb6fb_LowRes.png)
In the following JSON configuration, we enabled the exclusion of relations on shapes based on the default custom attribute with the specified technical ID.

```
{
 "processSyncDescriptors": [
  {
   "inboundMappings": [],
   "active": true,
   "directoryIds": [
    "10d342f5db704199968d86688c528073"
   ],
   "linkProcessingMode": "PARENT_CHILD",
   "publishedOnly": false,
   "startNodeId": null,
   "filterExpression": null,
   "leanixParentFactSheetId": null,
   "blacklist": [],
   "shortDescription": "",
   "excludeRelationByCustomShapeAttribute": true
   "excludeRelationByCustomShapeAttributeId": "meta-excludefromleanixsync",
  }
 ]
}
```



