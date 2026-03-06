##  Step 5: Configure Your CI/CD Pipeline
To complete the discovery and update process of your microservices, you need to establish a CI/CD workflow within your repository. This workflow will ensure that the system automatically detects and incorporates any changes made to your microservices, significantly reducing manual intervention and potential errors.
While it's possible to register microservices through API requests in any environment without a CI/CD pipeline, we strongly recommend using the CI/CD approach. The primary reason for this is to ensure that your data is always up to date. With this approach, your manifest file serves as the source of truth, and any changes made to it are automatically reflected in your microservices.
The CI/CD workflow setup may differ depending on your repository provider. The following table provides examples of how to establish a CI/CD workflow with various repository providers:
Repository Provider | Automation Workflow
---|---
Azure DevOps | For an Azure pipeline example, see [Azure CI/CD Discovery](https://help.sap.com/docs/leanix/ea/configuring-your-ci-cd-pipeline?locale=en-US&state=PRODUCTION&version=CLOUD#loio275951497a44101486a5e1c824ffb2dd__azure_ci_cd_discovery)
Bitbucket | For a Bitbucke pipeline example, see [Bitbucket CI/CD Discovery](https://help.sap.com/docs/leanix/ea/configuring-your-ci-cd-pipeline?locale=en-US&state=PRODUCTION&version=CLOUD#loio275951497a44101486a5e1c824ffb2dd__bitbucket_ci_cd_discovery)
GitHub | For a GitHub actions example, see [GitHub CI/CD Discovery](https://help.sap.com/docs/leanix/ea/configuring-your-ci-cd-pipeline?locale=en-US&state=PRODUCTION&version=CLOUD#loio275951497a44101486a5e1c824ffb2dd__github_ci_cd_discovery)
GitHub Enterprise Server | For a GitHub actions example, see [GitHub CI/CD Discovery](https://help.sap.com/docs/leanix/ea/configuring-your-ci-cd-pipeline?locale=en-US&state=PRODUCTION&version=CLOUD#loio275951497a44101486a5e1c824ffb2dd__github_ci_cd_discovery)
GitLab | For a GitLab pipelines example, see [GitLab CI/CD Discovery](https://help.sap.com/docs/leanix/ea/configuring-your-ci-cd-pipeline?locale=en-US&state=PRODUCTION&version=CLOUD#loio275951497a44101486a5e1c824ffb2dd__gitlab_ci_cd_discovery)


**Note**
The CI/CD approach is designed with flexibility in mind. If you decide to migrate to a Git integration down the line, the current setup effortlessly transitions. Your existing manifest file will seamlessly synchronize with the microservice fact sheet, eliminating the need for additional configuration or rework.
