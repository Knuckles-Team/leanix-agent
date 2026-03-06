##  Fields and Relations in Provider Fact Sheet
Attributes for Name & Description Attribute Name | Type | Description
---|---|---
DORA Critical | Single Select | A binary field to indicate whether the given provider is considered critical for DORA compliance or not.
ICT Provider Category | Single Select | Indicates whether the provider is internal or external.
Provider Type | Single Select | It classifies the type of provider based on the nature of services they offer, such as cloud service providers, software providers, risk management providers, among others.
Legal Entity Identifier | External ID | The Legal Entity Identifier (LEI) is an alphanumeric code based on the ISO 17442 standard.


Attributes for Critcality & Quality Attribute Name | Type | Description
---|---|---
Financial Stability | Single Select | Indicates whether the vendor's financial health has been assessed to ensure they have the resources to deliver their services effectively and handle potential disruptions.
Integration Capabilities | Single Select | Indicates the evaluation of the vendor's ability to integrate their services with your existing enterprise architecture, including their use of standard protocols and APIs.
Reputation | Single Select | Indicates the assessment of the vendor's reputation in the market, including any past incidents, legal issues, or negative publicity.
Operational Resilience | Single Select | Indicates the assessment of the vendor's ability to maintain operations during disruptive incidents. This includes their business continuity plans, disaster recovery plans, and incident response plans.
Sourcing Risk | Single Select | Classifies sourcing risk from low to critical, indicating potential issues if a provider fails to meet obligations. Risks may arise from financial instability, regulatory issues, operational failures, or geopolitical factors—leading to disruptions, financial losses or reputational damage.
NPS | Integer Number | Net Promoter Score is a measure of customer satisfaction that ranges from -100 to 100, with a higher score indicating a more positive perception of the provider.
Exit Criteria | Single Select | Exit criteria refer to predefined conditions that, when met, mark the conclusion of a contract, project, or phase. They ensure both parties have a shared understanding of when and how an engagement should formally end.


Attributes for Contract Details Attribute Name | Type | Description
---|---|---
Contract Type | Single Select | Specifies the type of contract associated with the provider.
Currency | Single Select | The currency used in the contract details.
Renewal Status | Single Select | Indicates the status of the contract renewal process.
Duration (per Year) | Integer Number | The contract duration in years.
Payments Term | Single Select | Specifies the frequency of payment for the provider's services.
Cost (per Year) | Integer - Costs | The cost associated with the provider's contract details.
Service-Level Agreement | Single Select | An SLA is a contract between a service provider and a client that defines the expected quality and type of service. It includes measurable metrics—like system availability, response times, and performance—and outlines remedies if those standards aren’t met.
Service-Level Agreement Description | Text area |  To summarize key items of the agreement.  **Tip** Add all additional resources for the SLA in the resource tab of this fact sheet.
Data Processing Agreement (DPA) | Single Select | A Data Processing Agreement (DPA) is a legally binding contract between a data controller and a data processor that outlines how personal data will be handled and protected. It ensures both parties comply with data protection laws and specifies responsibilities regarding data security, privacy, and breach notifications.
Data Processing Agreement Description | Text area |  To summarize key items of the agreement.  **Tip** Add all additional resources for the DPA in the resource tab of the fact sheet.


