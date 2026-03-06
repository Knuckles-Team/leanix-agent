##  Synchronizing Hierarchy and Process Relations
The integration manages process hierarchies with variants in the following way:
  * Process templates that are children of other templates are synchronized normally, maintaining the hierarchy.
  * Templates that are children of process variants are not automatically synchronized, preventing data loss and avoiding recursive complexity. Variants of these undiscovered templates are also not synchronized.
  * Child processes of variants are not discovered.
