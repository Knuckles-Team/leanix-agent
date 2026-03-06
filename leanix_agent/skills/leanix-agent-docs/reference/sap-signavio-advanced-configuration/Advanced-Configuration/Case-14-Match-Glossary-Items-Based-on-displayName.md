##  Case 14: Match Glossary Items Based on displayName
You can match the glossary item titles with SAP LeanIX Fact Sheet display names. This can be achieved with the following code snippet in the advanced configuration of integration.

```
{
 "glossaryCategorySyncDescriptors": [
  {
   "active": true,
   "nameResolvedByFSField”: “displayName"
  }
 ]
}

```



