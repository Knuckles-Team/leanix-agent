##  Updating multi_select fields from an array
This processor supports updating multi_select fields in SAP LeanIX.
Example. Pre-requisite: Have the multi-select field myMultiSelect available in the workspace with options: FOO and BAR. Update myMultiSelect field with values from myField in input.
Connector:

```
{
        "processors": [
                {
                        "processorType": "inboundFactSheet",
                        "processorName": "Apps from Deployments",
                        "processorDescription": "Creates LeanIX Applications from Kubernetes Deployments",
                        "type": "Application",
                        "filter": {
                                "exactType": "Deployment"
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
                        "updates": [
                                {
                                        "key": {
                                                "expr": "name"
                                        },
                                        "values": [
                                                {
                                                        "expr": "${data.app}"
                                                }
                                        ]
                                },
                                {
                                        "key": {
                                                "expr": "myMultiSelect"
                                        },
                                        "values": [
                                                {
                                                        "expr": "${integration.output.valueOfForEach}",
                                                        "forEach": {
                                                                "elementOf": "${data['myField']}"
                                                        }
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
LDIF input:

```
{
        "connectorType": "Kubernetes",
        "connectorId": "Kub Dev-001",
        "connectorVersion": "1.2.0",
        "lxVersion": "1.0.0",
        "description": "Imports Kubernetes data into LeanIX",
        "processingDirection": "inbound",
        "processingMode": "partial",
        "customFields": {},
        "content": [
                {
                        "type": "Deployment",
                        "id": "634c16bf-198c-1129-9d08-92630b573fbf",
                        "data": {
                                "app": "HR Service",
                                "tags": [],
                                "myField": [
                                        "FOO"
                                ],
                                "version": "1.8.4",
                                "maturity": "3",
                                "clusterName": "westeurope"
                        }
                },
                {
                        "type": "Deployment",
                        "id": "784616bf-198c-11f9-9da8-9263b0573fbe",
                        "data": {
                                "app": "Finance Service",
                                "tags": [
                                        "Important"
                                ],
                                "myField": [
                                        "FOO",
                                        "BAR"
                                ],
                                "version": "10.5",
                                "maturity": "5",
                                "clusterName": "westeurope"
                        }
                }
        ]
}
```



