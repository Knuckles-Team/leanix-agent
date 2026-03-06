##  Introduction
SAP LeanIX facilitates the automated discovery of technology stacks from ingested SBOMs. This operation is conducted automatically in the background, eliminating the need for additional configurations.
SAP LeanIX uses a curated reference catalog to match detailed SBOM components with corresponding tech stack items. When a library matches a tech stack, an IT component is created and linked to the relevant microservice. If multiple libraries match a single tech stack, they are consolidated. Currently, tech stack discovery supports the identification of frameworks and databases.
This automatic and continuous detection and cataloging of tech stacks aid in streamlining your organization's technology stack. The tech radar report further supports this effort by offering a comprehensive visual representation of your technology landscape. For more information, refer to [Radar Report](https://help.sap.com/docs/leanix/ea/radar-report?locale=en-US&state=PRODUCTION&version=CLOUD "A Radar report offers a visual representation of fact sheets categorized in rings and sectors. It aids in understanding an organization's tech landscape and evaluate technology standards.").
In addition to automated discovery, you can also add custom tech stacks manually to complete your technology portfolio.
The following image illustrates how tech stack discovery works.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio3143d6929bce40e6b2e1a23f5f71469f_LowRes.png)
Tech Stack Discovery Process
