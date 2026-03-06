##  Setting the Fields
The processor needs the "fields" section to define the names of the fields that will be read from each Fact Sheet and can then be used in the output section using "lx.factsheet.fieldName".
The "description" field was marked "optional". This means in case a Fact Sheet does not have any description, there will be no warning generated but the Description key silently omitted as it was configured to be expected that description may be missing.
The above configuration leads to a resulting LDIF similar to this.
Outbound processor:

```
{
 "scope": {
  "facetFilters": [],
  "ids": []
 },
 "processors": [
  {
   "processorType": "outboundFactSheet",
   "processorName": "Export to LDIF",
   "processorDescription": "This is an example how to use the processor",
   "enabled": true,
   "fields": [
    "createdAt",
    "description"
   ],
   "output": [
    {
     "key": {
      "expr": "content.id"
     },
     "values": [
      {
       "expr": "${lx.factsheet.id}"
      }
     ]
    },
    {
     "key": {
      "expr": "content.type"
     },
     "values": [
      {
       "expr": "${lx.factsheet.type}"
      }
     ]
    },
    {
     "key": {
      "expr": "Description"
     },
     "values": [
      {
       "expr": "${lx.factsheet.description}"
      }
     ],
     "optional": true
    },
    {
     "key": {
      "expr": "creationDateTime"
     },
     "mode": "selectFirst",
     "values": [
      {
       "expr": "${lx.factsheet.createdAt}"
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
LDIF output:

```
{
        "results": {
                "connectorType": "Test connector",
                "connectorId": "--",
                "connectorVersion": "1.0.0",
                "processingDirection": "INBOUND",
                "processingMode": "PARTIAL",
                "lxWorkspace": null,
                "lxVersion": "1.0.0",
                "description": "The resulting LDIF of the outbound run c86faf41-cac5-4309-a98a-bb01b8597752",
                "content": [
                        {
                                "type": "Application",
                                "id": "fc2b0641-6172-40cf-9dbb-10e514c7e341",
                                "data": {
                                        "Description": "",
                                        "creationDateTime": "2018-04-17T21:44:27.214Z"
                                }
                        },
                        {
                                "type": "Application",
                                "id": "716b9d27-3df7-42ca-ae6e-e2ef788064dd",
                                "data": {
                                        "Description": "SAP Supply Chain Management handles everything with regards to our supply chain, from planning, coordination with our supplier and customer. It is fully integrated with our Warehouse Management",
                                        "creationDateTime": "2018-04-17T21:44:27.214Z"
                                }
                        },
                        {
                                "type": "Application",
                                "id": "1a610104-6088-498a-856f-bb6a8298bcd4",
                                "data": {
                                        "Description": "Mailsnake is supporting newsletter mailing for different user groups for after-sales services ... announcing new features, small online training courses, ...",
                                        "creationDateTime": "2018-04-17T21:44:27.212Z"
                                }
                        },
                        {
                                "type": "BusinessCapability",
                                "id": "58aaff75-1649-447c-bdec-01860db7026f",
                                "data": {
                                        "Description": "",
                                        "creationDateTime": "2018-04-17T21:44:28.663Z"
                                }
                        }
                ],
                "chunkInformation": {
                        "firstDataObject": 0,
                        "lastDataObject": 394,
                        "maxDataObject": 394
                }
        },
        "warnings": [],
        "debugInfo": [],
        "debugVariables": [],
        "statistics": {
                "statusChanges": [
                        {
                                "status": "CREATED",
                                "timestamp": "2022-03-10T07:24:01.44829307Z"
                        },
                        {
                                "status": "PENDING",
                                "timestamp": "2022-03-10T07:24:01.768868487Z"
                        },
                        {
                                "status": "IN_PROGRESS",
                                "timestamp": "2022-03-10T07:24:03.194204924Z"
                        },
                        {
                                "status": "FINISHED",
                                "timestamp": "2022-03-10T07:24:04.614733108Z"
                        }
                ],
                "processorStatistics": [
                        {
                                "processorIndex": 0,
                                "processorName": "Export to LDIF",
                                "networkDuration": "PT0.955467958S",
                                "processingDuration": "PT0.085116706S",
                                "itemsInScopeCount": 395,
                                "processedContentCount": 395,
                                "errorCount": 0
                        }
                ],
                "totalBlockingTime": "PT0S"
        },
        "resultsUrl": {}
}
```



