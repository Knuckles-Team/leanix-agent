##  Overview
You can set up microservice discovery by adopting the configuration-as-code approach. This involves using a configuration file, often referred to as a manifest file, to define the characteristics and metadata of each microservice. The manifest file is stored in a version-controlled repository, typically alongside the source code of the microservice.
The process of discovering microservices through a manifest file ensures that any modifications made to this file in your repository are mirrored in SAP LeanIX, keeping your inventory up to date. The manifest file serves as a single source of truth, ensuring all microservices along with their details remain current.
The configuration-as-code approach for microservice discovery offers several key benefits:
  * Alignment with established practices: This approach is in line with established practices within the software development field, making it intuitive for developers and reducing the learning curve.
  * In-context contribution: Technical stakeholders, including developers, can contribute to the architectural design within their usual development environment.
  * Collaboration: This approach fosters collaboration between enterprise architects and developers, leading to more efficient and cohesive development processes.
  * Up-to-date inventory: Changes made to a manifest file are automatically reflected in SAP LeanIX, ensuring your microservice fact sheets are always up to date.


This guide provides detailed instructions on how to set up microservice discovery using a YAML manifest file and a Python script.
**Note**
We're working on an out-of-the-box integration with GitHub Enterprise for microservice discovery. If your organization uses GitHub Enterprise for source code hosting, you can take advantage of this integration instead of setting up microservice discovery manually, as described in this guide. For more information, see [GitHub Enterprise Integration](https://help.sap.com/docs/leanix/ea/github-enterprise-integration?locale=en-US&state=PRODUCTION&version=CLOUD "Set up self-built software discovery using our out-of-the-box integration with GitHub Enterprise Server.").
