##  GitHub CI/CD Discovery
The GitHub pipeline outlined here automatically updates your microservices on each push or pull request to the main branch, ensuring your microservice fact sheets remain current.
To set up this workflow, create a new GitHub workflow in your repository under .github/workflows. For instructions, refer to the [GitHub documentation![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fdocs.github.com%2Fen%2Factions%2Fusing-workflows%2Fabout-workflows "https://docs.github.com/en/actions/using-workflows/about-workflows").
The following YAML script outlines the workflow:

```
name: Microservice Workflow
on:
  pull_request:
    types:
      - closed
    branches: [main]
env:
  LEANIX_API_TOKEN: ${{ secrets.LEANIX_API_TOKEN }}
  LEANIX_SUBDOMAIN: ${{ vars.LEANIX_SUBDOMAIN }}

jobs:
  update_microservice:
    runs-on: ubuntu-latest
    env:
      REPOSITORY_URL: ${{ github.repositoryUrl }}
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: "3.12"
      - name: Install Python dependencies
        run: |
          python -m pip install --upgrade pip
          pip install requests pyyaml
      - name: Invoke Manifest Parser
        run: python leanix_service_discovery.py

```



