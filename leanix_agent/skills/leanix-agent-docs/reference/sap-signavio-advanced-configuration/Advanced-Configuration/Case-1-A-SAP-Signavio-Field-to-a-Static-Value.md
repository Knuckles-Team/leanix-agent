##  Case 1: A SAP Signavio Field to a Static Value
The synchronization that assigns a fixed value to a Fact Sheet field as shown in the Basic Section:
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274b4f387a44101495d3c8dfc8fab441_LowRes.png)
The equivalent configuration in JSON format is shown in the following listing:

```
 "inboundMappings": [
  {
   "leanixType": "factSheetField",
   "fields": [
    {
     "leanixFieldName": "comment",
     "inboundPropertyPath": "Synchronized by LeanIX Signavio Integration",
     "valueMappings": []
    }
   ]
  }
 ]
}

```



