##  Fields and Relations in Application and IT Component Fact Sheets
Attributes for Name & Description Attribute Name | Type | Description
---|---|---
DORA Critical | Single Select | A binary field to indicate whether an application is considered critical for DORA compliance or not.


Attributes for Impact Assessment  Attributes are evaluated on a 4-point scale. Attribute Name | Type | Description
---|---|---
Service Disruption | Single Select | Manual assessment of the potential disruption time in the event of service disruption.
Financial Impact | Single Select | Manual assessment of how high the financial impact would be in the event of an incident.
Reputational Damage | Single Select | Manual assessment of the potential damage to the organization's reputation in the event of an incident.
Regulatory Impact | Single Select | Manual assessment of potential regulatory sanctions in the event of data leaks.
Impact Classification | Single Select | Overall impact based on the severity level of the other attributes.


Attributes for Resilience Testing Attribute Name | Type | Description
---|---|---
Training & Awareness | Multi-Select | Available training delivery methods for the service regarding data classification, DORA, infosec, and related topics.
Test Date | Date Field | The date when resilience testing was last conducted for this application.
Confidentiality | Single Select | This field classifies the sensitivity of the information handled by the service. Ranging from public to highly confidential.
Integrity | Single Select | This field classifies the accuracy and consistency of data handled by the service. In the context of the CIA triad, "Integrity" ensures that data is accurate, consistent, and protected from unauthorized modification throughout its lifecycle.
Availability | Single Select | Classifies the level of service availability during resilience testing, indicating how disruptions or failures affect the application's availability.
Scalability | Single Select | Indicates how well the application can adjust to varying load and usage levels.
Fault Tolerance | Single Select | The capability of a service to continue operating in the event of a fault or failure.
Robustness | Single Select | The ability of the service to maintain its functionality under stressed conditions, such as high load or temporary failure of its components.
Risk Types | Multi-Select | Potential types of risks associated with the application or IT component.
Cyber Security Measures | Multi-Select | Cybersecurity measures to address risks, including identity and access management policies.


Optional Attributes Designed to dependencies and impacts of the affected application and IT component. Attribute Name | Type | Description
---|---|---
Recovery Plan Business Contexts | Many-to-many | A relation to the new fact sheet subtype "Continuity Plan" of the business context fact sheet type. These are the recovery processes that can be executed based on the type of incident and are ideally maintained in SAP Signavio.
Affected Application | Many-to-many | Applications that are likely to be affected if this application is impacted.
Affected By Applications | Many-to-many | This application is likely to be affected if these applications are impacted.
Processing Location | Many-to-many | Relation to the subtype "region" of the organization fact sheet type. This captures the region(s) where the application processes data.


