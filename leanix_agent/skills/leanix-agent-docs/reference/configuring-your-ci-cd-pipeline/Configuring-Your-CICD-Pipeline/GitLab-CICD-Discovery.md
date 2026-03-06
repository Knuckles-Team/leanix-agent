##  GitLab CI/CD Discovery
The GitLab CI/CD pipeline outlined here automatically updates your microservices on each push or merge request to the main branch, ensuring your microservice fact sheets remain current.
To set up this pipeline, create or update your .gitlab-ci.yml file in your repository root. The following YAML script outlines the pipeline:

```
stages:
  - update_microservice

update_microservice:
  image: python:3.12
  script:
    - pip install --upgrade pip
    - pip install requests pyyaml
    - python leanix_service_discovery.py
  only:
    - main

```



YesNo
Send
