##  Antipatterns
This section addresses antipatterns involving ineffective or counterproductive ways of modeling organizations in SAP LeanIX.
  * Data centers should not be modeled as organizations but as IT components in SAP LeanIX.
  * Don’t try to reflect your fine-granular organizational structure to avoid failing because of complexity. It is always a trade-off between the degree of detail and data maintenance. E.g., going down to such detail as teams might be well thought through since teams might merge/split/change names often.
  * Don’t confuse organizations with subscriptions. Subscribers/subscription roles are not modeled as a fact sheet type but maintained as an attribute of the fact sheet.
