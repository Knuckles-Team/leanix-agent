##  Antipatterns
This section addresses antipatterns involving ineffective or counterproductive ways of modeling business capability in SAP LeanIX.
  * Don’t confuse business capability with process
    * BC shows ‘What’ the business is doing, whereas processes show 'How' it is done
    * Example:
Capability = Accounting & Billing
Process (a subtype of the business context fact sheet ) = Create Purchase Order
  * Don’t confuse business capability with the organization fact sheet. An organizational unit is a group of people or departments within an organization that performs a specific function or task or represents a certain geography (e.g., Headquarter / Group Accounting). Organizational units can serve as an inspiration to model BCs, but BCs should be, in general, independent. You would model those units in the organization fact sheet type, and several units could be linked to the same business capability.
  * Don’t confuse with tech categories; Those are used to group IT components and to standardize/cluster application sourcing.
