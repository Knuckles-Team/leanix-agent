##  Azure CI/CD Discovery
The Azure pipeline outlined here automatically updates your microservices on each push to the main branch, ensuring your microservice fact sheets remain current.
To set up this pipeline, create a new azure-pipelines.yml file in your repository root. The following YAML script outlines the pipeline:

```
trigger:
- main

pool:
  vmImage: 'ubuntu-latest'

steps:
- task: UsePythonVersion@0
  inputs:
    versionSpec: '3.12'
    addToPath: true

- script: |
    python -m pip install --upgrade pip
    pip install requests pyyaml
  displayName: 'Install dependencies'

- script: python leanix_service_discovery.py
  displayName: 'Invoke Manifest Parser'

```



