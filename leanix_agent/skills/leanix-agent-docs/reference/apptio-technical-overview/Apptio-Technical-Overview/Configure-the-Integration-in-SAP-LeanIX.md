##  Configure the Integration in SAP LeanIX
To configure the Apptio Integration, in the administration area, navigate to the Integrations section, then click Configure in the Apptio section.
To learn how to configure the Apptio connector, see [Configuration of the Apptio Connector](https://help.sap.com/docs/leanix/ea/configuration-of-apptio-connector?locale=en-US&state=PRODUCTION&version=CLOUD "Set up the Apptio connector, configure field mapping and synchronization settings to enrich the SAP LeanIX workspace with up-to-date cost information.").
The example below demonstrates what is possible to send outbound (export) to Apptio.
Apptio-Integration-Config

```
{
    "configId": "lxApptio",
    "workspaceId": "ea7d3162-b4c5-4dbf-b9fb-6ba8f050ce08",
    "name": "apptio-config-v2",
    "data": {
        "apptioConnectionConfig": {
            "loginUrl": "https://frontdoor.apptio.com/service/apikeylogin",
            "keyAccess": "48a3e006-8cc1-487b-a26e-ca020e8e097d",
            "keySecret": "xxxxxxxxxx-xxxxxxxxxx",
            "domain": "leanixpartner.com",
            "environmentName": "sandbox",
            "ulsUrl": "https://datalink-eu.apptio.com/uls/api/v1"
        },
        "apptioWriteConfigs": [
            {
                "type": "detailed",
                "host": "bizdev-r12.apptio.com",
                "project": "Cost Transparency",
                "tableName": "lxApps",
                "period": "current",
                "overwrite": true
            },
            {
                "type": "detailed",
                "project": "Cost Transparency",
                "tableName": "lxITComponents",
                "period": "current",
                "overwrite": true
            },
            {
                "type": "detailed",
                "host": "bizdev-r12.apptio.com",
                "project": "Cost Transparency",
                "tableName": "lxUserGroups",
                "period": "current",
                "overwrite": true
            },
            {
                "type": "detailed",
                "host": "bizdev-r12.apptio.com",
                "project": "Cost Transparency",
                "tableName": "lxBusinessCapabilities",
                "period": "current",
                "overwrite": true
            },
            {
                "type": "detailed",
                "host": "bizdev-r12.apptio.com",
                "project": "Cost Transparency",
                "tableName": "lxProviders",
                "period": "current",
                "overwrite": true
            },
            {
                "type": "detailed",
                "host": "bizdev-r12.apptio.com",
                "project": "Cost Transparency",
                "tableName": "lxProjects",
                "period": "current",
                "overwrite": true
            },
            {
                "type": "detailed",
                "host": "bizdev-r12.apptio.com",
                "project": "Cost Transparency",
                "tableName": "lxRelApplicationToBusinessCapability",
                "period": "current",
                "overwrite": true
            },
            {
                "type": "detailed",
                "host": "bizdev-r12.apptio.com",
                "project": "Cost Transparency",
                "tableName": "lxRelApplicationToITComponent",
                "period": "current",
                "overwrite": true
            },
            {
                "type": "detailed",
                "host": "bizdev-r12.apptio.com",
                "project": "Cost Transparency",
                "tableName": "lxRelApplicationToUserGroup",
                "period": "current",
                "overwrite": true
            },
            {
                "type": "detailed",
                "host": "bizdev-r12.apptio.com",
                "project": "Cost Transparency",
                "tableName": "lxRelITComponentToUserGroup",
                "period": "current",
                "overwrite": true
            },
            {
                "type": "detailed",
                "host": "bizdev-r12.apptio.com",
                "project": "Cost Transparency",
                "tableName": "lxApplicationRelToChild",
                "period": "current",
                "overwrite": true
            },
            {
                "type": "detailed",
                "host": "bizdev-r12.apptio.com",
                "project": "Cost Transparency",
                "tableName": "lxITComponentRelToChild",
                "period": "current",
                "overwrite": true
            },
            {
                "type": "detailed",
                "host": "bizdev-r12.apptio.com",
                "project": "Cost Transparency",
                "tableName": "lxBusinessCapabilityRelToChild",
                "period": "current",
                "overwrite": true
            },
            {
                "type": "detailed",
                "host": "bizdev-r12.apptio.com",
                "project": "Cost Transparency",
                "tableName": "lxUserGroupRelToChild",
                "period": "current",
                "overwrite": true
            },
            {
                "type": "detailed",
                "host": "bizdev-r12.apptio.com",
                "project": "Cost Transparency",
                "tableName": "lxRelITComponentToProvider",
                "period": "current",
                "overwrite": true
            },
            {
                "type": "detailed",
                "host": "bizdev-r12.apptio.com",
                "project": "Cost Transparency",
                "tableName": "lxRelProjectToApplication",
                "period": "current",
                "overwrite": true
            },
            {
                "type": "detailed",
                "host": "bizdev-r12.apptio.com",
                "project": "Cost Transparency",
                "tableName": "lxRelProjectToITComponent",
                "period": "current",
                "overwrite": true
            },
            {
                "type": "detailed",
                "host": "bizdev-r12.apptio.com",
                "project": "Cost Transparency",
                "tableName": "lxRelProjectToBusinessCapability",
                "period": "current",
                "overwrite": true
            },
            {
                "type": "detailed",
                "host": "bizdev-r12.apptio.com",
                "project": "Cost Transparency",
                "tableName": "lxRelProjectToUserGroup",
                "period": "current",
                "overwrite": true
            },
            {
                "type": "detailed",
                "host": "bizdev-r12.apptio.com",
                "project": "Cost Transparency",
                "tableName": "lxSubscriptions",
                "period": "current",
                "overwrite": true
            }
        ],
        "apptioReadConfigs": [],
        "dataConsumer": {
            "type": "leanixStorage"
        }
    },
    "createdAt": "2020-05-04T11:02:55.970136Z",
    "active": true
}

```



