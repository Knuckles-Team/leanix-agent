##  Handling of Process Variant Dimensions
Scenario | Handling
---|---
A process variant has multiple dimensions assigned. For example, ‘Organizational Unit: US’ and 'Product Line: Software' |
  * If all dimensions map to fact sheets that have constraining relations with applications, then all constraints are applied.  In the standard meta model, it is the organization and business capability that can constrain relations with applications.
  * For dimensions that don't map to fact sheets that have constraining relations, the dimensions are ignored.
  * The integration logs ignored dimensions in the sync log.


A process variant dimension value has no corresponding fact sheet in SAP LeanIX. |
  * The process variant is treated as if it has no dimension, or ignored, depending on the configuration.
  * Applications linked to this variant are treated as if they are linked to the template.
  * A warning is logged in the sync log.


A process variant uses the application as a dimension. |
  * The application dimension is ignored, and synchronization continues with any remaining dimensions. If no other dimensions are present, the variant is treated as if it has no dimension.


A variant exists but has no dimension values assigned. |
  * The process variant cannot be distinguished from the template without the dimension, and hence it is not mapped.
  * Applications linked only to this variant are treated as if they are linked to the process template.
  * A warning is logged in the sync log.




YesNo
Send
