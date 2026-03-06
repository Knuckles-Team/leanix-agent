##  Inbound To-dos
This processor can be used import to-dos into the workspace.
Keys specific to the inboundToDo Processor | Details
---|---
title | Title of the To-do
category | Category of the To-do (Sample values: ANSWER,ACTION_ITEM)
description | Description of the To-do
status | Status of the To-do (OPEN, CLOSED)
resolution | When closing you also have an option to provide the resolution(ACCEPTED,REJECTED,REVERTED)


Below example will need to be adapted as per specific type of To-dos.
Example inboundToDo processor:

```
{
  "processors": [
    {
      "processorType": "inboundToDo",
      "processorName": "Create toDos",
      "processorDescription": "Creates toDos from incoming data",
      "filter": {
        "exactType": "ActionItem"
      },
      "identifier": {
        "external": "${content.id}"
      },
      "run": 1,
      "updates": [
        {
          "key": {
            "expr": "factSheetId"
          },
          "values": [
            {
              "expr": "${data.factSheetId}"
            }
          ]
        },
        {
          "key": {
            "expr": "title"
          },
          "values": [
            {
              "expr": "${data.title}"
            }
          ]
        },
        {
          "key": {
            "expr": "description"
          },
          "values": [
            {
              "expr": "${data.description}"
            }
          ]
        },
        {
          "key": {
            "expr": "category"
          },
          "values": [
            {
              "expr": "${data.category}"
            }
          ]
        },
        {
          "key": {
            "expr": "dueDate"
          },
          "values": [
            {
              "expr": "${data.dueDate}"
            }
          ]
        }
      ],
      "variables": [
        {
          "key": "category",
          "value": "${lx.todo.id}_${lx.todo.category}"
        },
        {
          "key": "state",
          "value": "${lx.todo.state}"
        }
      ],
      "logLevel": "debug"
    }
  ],
  "variables": {}
}
```



Example input in LDIF format:

```
{
  "connectorType": "todoReadType",
  "connectorId": "todoReadId",
  "connectorVersion": "1.0.0",
  "lxVersion": "1.0.0",
  "description": "",
  "processingDirection": "inbound",
  "processingMode": "partial",
  "customFields": {},
  "content": [
    {
      "type": "ActionItem",
      "id": "E-100",
      "data": {
        "title": "test abc",
        "description": "Updated by iAPI",
        "todoId": "ec25a364-66df-4313-9127-44e429df81ad",
        "dueDate": "2021-08-19",
        "category": "ACTION_ITEM",
        "varValue": "value1",
        "creatorId": "275617d6-2538-466c-b210-961ef2cb554a",
        "factSheetId": "28fe4aa2-6e46-41a1-a131-72afb3acf256"
      }
    }
  ]
}
```



