##  Bitbucket CI/CD Discovery
The Bitbucket pipeline outlined here automatically updates your microservices on each push to the main branch, ensuring your microservice fact sheets remain current.
To set up this pipeline, create a new bitbucket-pipelines.yml file in your repository root. The following YAML script outlines the pipeline:

```
pipelines:
  default:
    - step:
        name: Update Microservice
        image: python:3.12
        script:
          - pip install --upgrade pip
          - pip install requests pyyaml
          - python leanix_service_discovery.py

```



