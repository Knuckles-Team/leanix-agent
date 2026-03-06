##  Lifecycle Management
Writing to fields of type lifecycle needs to be split into different write operations (lines in the data processor. The value of the "key" field has to use the "." syntax. E.g. "lifecycle.plan", "lifecycle.phaseIn". Other default values are "phaseOut" and "endOfLife".
Example inboundFactSheet processor with life cycle data:

```
{
 "processorType": "inboundFactSheet",
 "processorName": "Lifecycle Example",
 "processorDescription": "Creates an Application with lifecycle information",
 "type": "Application",
 "filter": {
  "exactType": "Application"
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
     "expr": "${data.name}"
    }
   ]
  },
  {
   "key": {
    "expr": "description"
   },
   "values": [
    {
     "expr": "${data.name} is an application that carries lifecycle information"
    }
   ]
  },
  {
   "key": {
    "expr": "lifecycle.plan"
   },
   "values": [
    {
     "expr": "${data.plan == null ? '2014-01-01' : data.plan}"
    }
   ]
  },
  {
   "key": {
    "expr": "lifecycle.phaseIn"
   },
   "values": [
    {
     "expr": "${data.phaseIn}"
    }
   ]
  },
  {
   "key": {
    "expr": "lifecycle.active"
   },
   "values": [
    {
     "expr": "${data.active}"
    }
   ]
  },
  {
   "key": {
    "expr": "lifecycle.phaseOut"
   },
   "values": [
    {
     "expr": "${data.phaseOut}"
    }
   ]
  },
  {
   "key": {
    "expr": "lifecycle.endOfLife"
   },
   "values": [
    {
     "expr": "${data.endOfLife}"
    }
   ]
  }
 ]
}
```



