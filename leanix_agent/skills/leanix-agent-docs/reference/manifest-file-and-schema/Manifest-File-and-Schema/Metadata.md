##  Metadata
The metadata section of the manifest file defines the characteristics of your microservice.
Attribute | Required | Description
---|---|---
name | Yes | The name of the microservice.
externalId | Required for [microservice discovery in your CI/CD pipeline](https://help.sap.com/docs/leanix/ea/microservice-discovery-in-your-ci-cd-pipeline?locale=en-US&state=PRODUCTION&version=CLOUD "Set up microservice discovery using a manifest file in your repository. This method, known as configuration-as-code, enables you to automatically discover microservices and update corresponding fact sheets in SAP LeanIX."). When using the [GitHub Enterprise integration](https://help.sap.com/docs/leanix/ea/github-enterprise-integration?locale=en-US&state=PRODUCTION&version=CLOUD "Set up self-built software discovery using our out-of-the-box integration with GitHub Enterprise Server."), the value is populated automatically. | The unique identifier of the microservice in the external system. It must be globally unique, ensuring that multiple microservices don't share the same external ID.
description | No | The description of the microservice.
type | No | The type of the microservice. It must match one of the values in the lxMicroserviceType field predefined in the meta model configuration, such as backend, ui, or data. If no type is passed, the default value backend is used.
repository | No | The details of the repository where the microservice is hosted, including url, status, and visibility.


We recommend a set of guidelines for formatting service names, especially for popular vendors. This uniform formatting helps maintain consistency and makes it easier to manage and locate services. The out-of-the-box Git integrations will follow this external ID schema. By adhering to this convention, you won't need any migration effort once we support that Git system.
Provider | Format | Example
---|---|---
GitHub |  {organization}/{repo-name}/{servicename} |  acme/banking-portal/payment-engine
GitLab |  {group}/{repo-name}/{servicename} |  acme/banking-portal/payment-engine
Bitbucket |  {workspace}/{repo-name}/{servicename} |  acme/banking-portal/payment-engine
Azure |  {organization}/{repo-name}/{servicename} |  acme/banking-portal/payment-engine


