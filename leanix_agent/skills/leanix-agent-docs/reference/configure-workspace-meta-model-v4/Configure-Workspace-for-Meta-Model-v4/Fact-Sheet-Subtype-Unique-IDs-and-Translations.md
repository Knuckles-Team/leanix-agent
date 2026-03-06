##  Fact Sheet Subtype Unique IDs and Translations
**Note**
In the default meta model v4, the organization's subtype "Region" has the unique ID "country", which is in conflict to the translation. We're planning to resolve this conflict in the future. In the meantime, please don't deviate from our best practice by introducing or changing the unique ID "country".
Fact Sheet type |  Subtype Unique ID |  Subtype Translation |  Subtype status
---|---|---|---
Application | businessApplication | Business Application | Optional
microservice | Microservice | Optional
Initiative | idea | Idea | Default
program | Program | Default
project | Project | Default
epic | Epic | Default
Organization | businessUnit | Business Unit | Default
customer | Customer | Default
region | Region | Default
legalEntity | Legal Entity | Default
team | Team | Default
Business Context | customerJourney | Customer Journey | Default
process | Process | Default
businessProduct | Business Product | Default
valueStream  | Value Stream | Default
esgCapability | ESG Capability | Optional
Interface | api | API  | Default
logicalInterface | Logical Interface |  Default
IT Component (new additional) | iaas | IaaS  | Default
paas | PaaS | Default
saas | SaaS | Default


You might already be using “category” as a unique ID in some of your Fact Sheet types. In such cases, simply identify the field and add additional subtype values. At the same time, rename the field to “Subtype“ from the Manage Translation tab of the right-side panel.
![Unique ID already in use](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2755dcb67a441014b9cf8ec2ce144860_LowRes.gif)
Unique ID already in use
It's recommended to create a direct relation between Business Applications and other subtypes through a self-referencing relation. This relation will help to model how these subtypes indirectly support Business Capabilities through Business Applications. For more information, see [Self-Referencing Relations](https://help.sap.com/docs/leanix/ea/meta-model-configuration?locale=en-US&state=PRODUCTION&version=CLOUD "Configure the meta model to adjust it to your requirements.").
