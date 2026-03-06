##  How It Works: Example
If a parent application has multiple child applications, the parent will inherit business context relations from all children. For example:
  * Child application A (Adobe Premiere Pro) has the business contexts "Video Production" and "Creative Services."
  * Child application B (Adobe After Effects) has the business contexts "Video Production" and "Motion Graphics."


The parent application (Adobe Creative Cloud) will have these business contexts:
  * “Video Production” [Auto-inherited from: Adobe Premiere Pro, Adobe After Effects]
  * “Creative Services” [Auto-inherited from: Adobe Premiere Pro]
  * “Motion Graphics” [Auto-inherited from: Adobe After Effects]


When a business context relation is removed:
  * If "Video Production" is removed from “Adobe Premiere Pro,” the parent's relation description updates to [Auto-inherited from: Adobe After Effects].
  * If "Creative Services" is removed from “Adobe Premiere Pro” (and no other child has it), it's removed from the parent entirely.


### Multi-Level Hierarchy
The automation cascades automatically through the hierarchy:

```
Parent level 2 (Creative Suite Portfolio)
    └── Parent level 1 (Adobe Creative Cloud)
          └── Child (Adobe Premiere Pro) ← business context added here
```



  1. A business context added to a child application triggers automation 1.
  2. The script adds the business context to the parent level 1 (marked as inherited).
  3. Adding the business context to the parent triggers automation 1 again.
  4. The script adds the business context to parent level 2 (marked as inherited).
