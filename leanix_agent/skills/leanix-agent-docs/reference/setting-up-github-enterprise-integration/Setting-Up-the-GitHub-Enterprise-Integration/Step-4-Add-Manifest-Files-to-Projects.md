##  Step 4: Add Manifest Files to Projects
Manifest files, specifically leanix.yaml files, are essential tools in the config-as-code practice. They enable you to describe and discover microservices from GitHub in SAP LeanIX. Place leanix.yaml files in the projects that correspond to the microservice or software artifact you want to describe. One manifest file is used to describe one microservice.
To view the structure and schema of the leanix.yaml file, see [Manifest File and Schema](https://help.sap.com/docs/leanix/ea/manifest-file-and-schema?locale=en-US&state=PRODUCTION&version=CLOUD "Manifest file for microservice discovery and the manifest schema.").
When configuring the manifest file, you can start with basic elements first (such as name and description) and then gradually evolve your governance to include more aspects (like linking to teams). Any changes made to the YAML file will be reflected in SAP LeanIX in near real-time.
For monorepos, where multiple deployed microservices are contained in a single repository, you can place the leanix.yaml file in the directories where a deployed service resides. The integration will find and process them accordingly. Here’s an YAML example configuration:

```
backend
  Dockerfile
  leanix.yaml
  src
    main.py
    requirements.txt
frontend
  Dockerfile
  leanix.yaml
  package.json
  src
    index.js
    ...

```



