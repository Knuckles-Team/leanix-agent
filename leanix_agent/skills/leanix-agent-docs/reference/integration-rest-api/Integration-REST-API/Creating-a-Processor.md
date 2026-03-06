##  Creating a Processor
Create a Processor under Integration API, with the below details:
  * Connector Type: importProjectsExample
  * Connector Id: importProjectsExample
  * Connector Version: 1.0.0
  * Processing Direction: inbound


Place the below details in the processor :

```
{
 "processors": [
  {
   "processorType": "inboundFactSheet",
   "processorName": "Projects from prj",
   "processorDescription": "Creates LeanIX Projects from external LDIF",
   "type": "Project",
   "filter": {
    "type": "prj|subp"
   },
   "identifier": {
    "external": {
     "id": {
      "expr": "${content.id}"
     },
     "type": {
      "expr": "externalId"
     }
    }
   },
   "run": 0,
   "updates": [
    {
     "key": {
      "expr": "name"
     },
     "values": [
      {
       "expr": "${data.displayName} (${content.id})"
      }
     ]
    },
    {
     "key": {
      "expr": "description"
     },
     "values": [
      {
       "expr": "${data.processDescription}"
      }
     ]
    },
    {
     "key": {
      "expr": "lifecycle.active"
     },
     "values": [
      {
       "expr": "${data.startActive}"
      }
     ]
    }
   ],
   "enabled": true,
   "variables": [],
   "logLevel": "warning"
  }
 ],
 "variables": {}
}
```



