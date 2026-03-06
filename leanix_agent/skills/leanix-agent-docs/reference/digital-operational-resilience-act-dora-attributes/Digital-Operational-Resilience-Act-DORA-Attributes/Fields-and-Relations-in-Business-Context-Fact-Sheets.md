##  Fields and Relations in Business Context Fact Sheets
Two new subtypes are introduced to support DORA compliance tracking:
  * Continuity Plan: This subtype groups continuity plans, like recovery strategies, crisis communication plans, and the like, that are in place to stay DORA compliant.
  * Training & Awareness: This subtype groups trainings that helps the organization to remain DORA compliant.


They allow you to document which processes are critical for operational resilience (for example, due to their sensitivity) and to track relevant business continuity strategies and training initiatives that help ensure ongoing DORA compliance.
Attributes for Business Continuity Management Attribute Name | Type | Description
---|---|---
DORA Critical | Single Select | A binary field to indicate whether the given process is considered critical for DORA compliance or not.
IT Disaster Recovery Plan | Single Select | 3-point scale status to track whether a disaster recovery plan has been developed.
IT Disaster Recovery Description | Text area | Description of the IT disaster recovery process.
Crisis Communication Plan | Single Select | 3-point scale status to track whether a crisis communication plan has been developed.
Crisis Communication Description | Text area | Description of the communication plan for crisis management.
Business Continuity Plan (BCP) | Single Select | 3-point scale status to track whether a business continuity plan has been developed.
Business Continuity Plan Description | Text area | Description of the business continuity plan detailing the processes and procedures to be followed in the event of a disruption or disaster.
Recovery Strategy | Single Select | 3-point scale status to track whether a recovery strategy has been developed.
Recovery Strategy Description | Text area | Description of the strategy and procedures for business continuity and disaster recovery.


Attributes for "Continuity Plans for Applications" and "Training Available For" Attribute Name | Type | Description
---|---|---
Continuity Plans for Applications | Many-to-many | This relation is conditional to—meaning only available in—the "Continuity Plans’" subtype of the business context fact sheet. It is used to track the specific applications to which this continuity plan applies.
Training Available For | Many-to-many | This relation is conditional to—meaning only available in—the "Training & Awareness" subtype of the business context fact sheet. It is used to track all applications for which a specific training is relevant. A field on the relation tracks the last time the training was conducted.


