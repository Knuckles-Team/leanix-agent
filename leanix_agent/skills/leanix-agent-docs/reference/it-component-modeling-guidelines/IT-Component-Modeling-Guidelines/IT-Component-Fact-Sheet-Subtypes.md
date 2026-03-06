##  IT Component Fact Sheet Subtypes
The IT component fact sheet has the following subtypes:
  * Hardware: Hardware refers to the physical components of a computer system or any IT device. It includes tangible, touchable parts you can see and interact with (e.g., servers, mainframe computers, storage devices).
Examples: IBM z15, HP ProLiant DL560, Dell EMC PowerEdge R750, NetApp AFF A900.
  * IaaS: IaaS (Infrastructure as a Service) refers to virtualized computing resources provided over the internet.
Examples: Amazon Web Services (AWS) EC2, Microsoft Azure Virtual Machines.
  * PaaS: PaaS (platform as a service) refers to cloud platforms for developers to build and deploy applications.
Examples: Google App Engine, Heroku, Salesforce (PaaS).
  * SaaS: SaaS (software as a service) refers to software applications accessed over the internet on a subscription basis. Examples: Salesforce B2B Commerce, Atlassian Confluence, SAP LeanIX. While an application fact sheet is used to model the SaaS application, the SaaS IT component subtype serves as a placeholder for the IT component to capture hosting, location, cost, and other implementation details.
  * Service: Services refer to the provisioning of services related to IT components (usually provided by a 3rd party). These are so-called managed IT services used to implement or run an application, which is not cloud services, software, or hardware. It involves activities like management, maintenance, or support.
Examples: Maintenance/Support Service, IT Transformation Services, Public Cloud Transformation Service, Hosting Service, Analytics Service (e.g., Accenture managing Application Support, Nordcloud managing AWS Hosting).
  * Software: Software refers to commercial or open-source software products that your application relies on, e.g., Operating Systems or Programming Languages.
Examples: Microsoft .NET Framework 4.8
  * AI model: Software components that implement artificial intelligence techniques, including machine learning, natural language processing, computer vision, and other forms of advanced analytics. AI models are used in applications to automate decision-making, pattern recognition, forecasting, and other predictive or generative tasks. AI models may be consumed directly as software artifacts, through APIs, or as integral parts of SaaS, PaaS, or custom technology stacks.
Examples: models by companies like OpenAI, Google, and Microsoft.
**Note**
The AI model subtype of the IT component fact sheet is available by default in new workspaces created after October 29, 2025. Previously, this subtype was available in workspaces with the [AI governance](https://help.sap.com/docs/leanix/ea/meta-model-ai-governance-extension?locale=en-US&state=PRODUCTION&version=CLOUD "Improve AI governance and adoption in your organization. Track and manage AI usage, evaluate risks, and assess AI potential.") extension activated and was named “LLM.” You can transition from the LLM to the new AI model subtype. For details, see [Scenarios for the AI Model Subtype](https://help.sap.com/docs/leanix/ea/it-component-modeling-guidelines?locale=en-US&state=PRODUCTION&version=CLOUD#loio275aaf847a441014af8a80b1657917b9__section_lhb_d1j_hhc).


**Example**
IT component examples: Chrome, Microsoft .NET Framework 4.8, Windows Server 2022
**Note**
For a step-by-step guide to create the fact sheet subtype, see [Add Fact Sheet Subtypes](https://help.sap.com/docs/leanix/ea/configure-workspace-meta-model-v4?locale=en-US&state=PRODUCTION&version=CLOUD#loio27595ce97a4410149c60a90e0f529a04__add_fact_sheet_subtypes_to_several_fact_sheet_types).
