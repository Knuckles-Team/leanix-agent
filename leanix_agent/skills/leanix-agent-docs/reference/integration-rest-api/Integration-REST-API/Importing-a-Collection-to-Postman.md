##  Importing a Collection to Postman
To make API calls to the Integration REST API in Postman, you can import the following file into it.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2750bb187a44101499e1f0f84e5627a1_LowRes.png)

```
{
 "info": {
  "_postman_id": "d5fc07f1-cef1-4b28-b965-97f2c662eb4b",
  "name": "Connect Integration API with Sample Connector",
  "description": "Check documentation for more details :- https://docs-eam.leanix.net/reference/integration-api",
  "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
 },
 "item": [
  {
   "name": "Post LDIF to LeanIX",
   "request": {
    "method": "POST",
    "header": [
     {
      "key": "Content-Type",
      "name": "Content-Type",
      "type": "text",
      "value": "application/json"
     }
    ],
    "body": {
     "mode": "raw",
     "raw": ""
    },
    "url": {
     "raw": "https://{{base_url}}/services/integration-api/v1/synchronizationRuns",
     "protocol": "https",
     "host": [
      "{{base_url}}"
     ],
     "path": [
      "services",
      "integration-api",
      "v1",
      "synchronizationRuns"
     ]
    }
   },
   "response": []
  },
  {
   "name": "Start the Sync",
   "request": {
    "method": "POST",
    "header": [],
    "url": {
     "raw": "https://{{base_url}}/services/integration-api/v1/synchronizationRuns/:id/start",
     "protocol": "https",
     "host": [
      "{{base_url}}"
     ],
     "path": [
      "services",
      "integration-api",
      "v1",
      "synchronizationRuns",
      ":id",
      "start"
     ],
     "variable": [
      {
       "key": "id",
       "value": "e546e34b-cbe5-43f2-9f43-2cbcda4c5405"
      }
     ]
    }
   },
   "response": []
  },
  {
   "name": "Status of Sync",
   "request": {
    "auth": {
     "type": "oauth2",
     "oauth2": [
      {
       "key": "accessToken",
       "value": "",
       "type": "string"
      },
      {
       "key": "tokenType",
       "value": "bearer",
       "type": "string"
      },
      {
       "key": "addTokenTo",
       "value": "header",
       "type": "string"
      }
     ]
    },
    "method": "GET",
    "header": [],
    "url": {
     "raw": "https://{{base_url}}/services/integration-api/v1/synchronizationRuns/:id/status",
     "protocol": "https",
     "host": [
      "{{base_url}}"
     ],
     "path": [
      "services",
      "integration-api",
      "v1",
      "synchronizationRuns",
      ":id",
      "status"
     ],
     "variable": [
      {
       "key": "id",
       "value": "e546e34b-cbe5-43f2-9f43-2cbcda4c5405"
      }
     ]
    }
   },
   "response": []
  },
  {
   "name": "Results of Sync",
   "request": {
    "method": "GET",
    "header": [],
    "url": {
     "raw": "https://{{base_url}}/services/integration-api/v1/synchronizationRuns/:id/results",
     "protocol": "https",
     "host": [
      "{{base_url}}"
     ],
     "path": [
      "services",
      "integration-api",
      "v1",
      "synchronizationRuns",
      ":id",
      "results"
     ],
     "variable": [
      {
       "key": "id",
       "value": "e546e34b-cbe5-43f2-9f43-2cbcda4c5405"
      }
     ]
    }
   },
   "response": []
  },
  {
   "name": "Warnings of Sync",
   "request": {
    "method": "GET",
    "header": [],
    "url": {
     "raw": "https://{{base_url}}/services/integration-api/v1/synchronizationRuns/:id/warnings",
     "protocol": "https",
     "host": [
      "{{base_url}}"
     ],
     "path": [
      "services",
      "integration-api",
      "v1",
      "synchronizationRuns",
      ":id",
      "warnings"
     ],
     "variable": [
      {
       "key": "id",
       "value": "e546e34b-cbe5-43f2-9f43-2cbcda4c5405"
      }
     ]
    }
   },
   "response": []
  }
 ],
 "auth": {
  "type": "oauth2",
  "oauth2": [
   {
    "key": "accessToken",
    "value": "",
    "type": "string"
   },
   {
    "key": "tokenType",
    "value": "bearer",
    "type": "string"
   },
   {
    "key": "addTokenTo",
    "value": "header",
    "type": "string"
   }
  ]
 },
 "event": [
  {
   "listen": "prerequest",
   "script": {
    "id": "ec73502c-9e67-4cf0-85cf-cf8170200181",
    "type": "text/javascript",
    "exec": [
     ""
    ]
   }
  },
  {
   "listen": "test",
   "script": {
    "id": "74a45df7-6d1e-4161-9f91-cf050d515c92",
    "type": "text/javascript",
    "exec": [
     ""
    ]
   }
  }
 ],
 "variable": [
  {
   "id": "99861109-e4a2-4607-9ed3-75857900a6ab",
   "key": "base_url",
   "value": "app.leanix.net",
   "type": "string"
  }
 ],
 "protocolProfileBehavior": {}
}
```



Follow these steps:
  1. Import the collection to Postman.
  2. Within the Postman UI, edit the collection at the Parent level, updating the Authorization by clicking Get New Access Token, and providing an API token from your SAP LeanIX workspace.
  3. Updated the raw body of the 'Post LDIF to LeanIX 'step to reflect the identifiers of the Integration API connector you would like to test.
  4. Send the Post LDIF to LeanIX request, and notice that an id is returned in the response { "id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" }
  5. Pass this id to Start the Sync, and each subsequent step as a Path Variable, id. Note: Start the Sync returns no Body, just a status 200 OK.
