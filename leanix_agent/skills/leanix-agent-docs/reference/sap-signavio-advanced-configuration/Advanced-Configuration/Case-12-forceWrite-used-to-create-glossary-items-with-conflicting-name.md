##  Case 12: forceWrite used to create glossary items with conflicting name
For glossary item synchronizations that go from SAP LeanIX to SAP Signavio, the configuration field forceWrite can be used to create or update glossary items that already exist on the SAP Signavio side in different glossary categories. In Signavio, it is possible to create entries with the same name in different categories. However, a confirmation step is required to proceed with the creation of the entry, maintaining the normal behavior of preventing duplicate glossary items.

```
{
 "glossaryCategorySyncDescriptors": [
  {
   "active": true,
   "forceWrite": true
  }
 ]
}

```



**Caution**
forceWrite should be only used after careful analysis of the SAP Signavio workspace
forceWrite should be only used after careful analysis of the SAP Signavio workspace as this will create duplicates in SAP Signavio GlossaryCategory.
