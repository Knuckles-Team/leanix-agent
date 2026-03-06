##  Completion Score Calculation
The fact sheet completion score is calculated hierarchically, beginning at the field level, then aggregating through subsections and sections, and finally to the entire fact sheet. Each level's score is based on the weighted completion of its components.
The weight of each component determines how much that component contributes to the completion score of that level, but it does not alter the weight of the level itself. For example, changing the weight of a field affects how much that field contributes to the completion score of its parent subsection, but it does not alter the weight of the subsection itself.
The completion score is calculated using the formula:
Completion Score = (Σ(CW × S) / Σ(CW)) × 100%
Where:
  * CW: Completion weight of the child component.
  * S: The state or completion score of the child component. For fields, this can be 0 (empty) or 1 (completed). For subsections or sections, it represents the completion score of child components, which can be any float number reflecting partial completion.


Completion scores are rounded down to the nearest whole number. For instance, scores between 99.5% and 99.9% appear as 99%, not 100%.
### At the Field Level
Each field's completion weight (CW) is multiplied by its state (S). For example, consider the following fields in a subsection:
Field | Completion Weight (CW) | State (S) | CWxS
---|---|---|---
Name | 5 | 1 (completed) | 5x1=5
Description | 3 | 0 (empty) | 3x0=0
Product Category | 2 | 1 (completed) | 2x1=2
Alias | 0 | 0 (empty) | 0x0=0


### At the Subsection Level
The completion scores of individual fields are summed up. This sum is then divided by the total weight of all fields in the subsection.
Continuing with the same example from above, the completion score of the subsection would be:
The sum of completion scores of all individual fields Σ(CW × S): 5+0+2+0 = 7.
The sum of all field weights Σ(CW): 5+3+2+0 = 10.
The subsection completion score (Σ(CW × S) / Σ(CW)) × 100%: (7/10) x 100% = 70%.
### At the Section Level
The completion scores of subsections within a section are summed up. This sum is divided by the total weight of all subsections in the section.
For example, consider the following subsections in a section:
Subsection | Completion Weight (CW) | State (S) | CWxS
---|---|---|---
Name & Description | 1 | 70% | 1x0.7=0.7
Lifecycle | 1 | 90% | 1x0.9=0.9
Successors | 0 | 50% | 0x0.5=0
Predecessors | 1 | 0% | 1x0=0


The completion score of the section would be:
The sum of completion scores of all subsections Σ(CW × S): 0.7+0.9+0+0=1.6
The sum of all subsection weights Σ(CW): 1+1+0+1=3.
The section completion score (Σ(CW × S) / Σ(CW)) × 100%: (1.6/3) * 100% = 53.33%.
### At the Fact Sheet Level
The completion scores of all sections are summed up. This sum is divided by the total weight of all sections in the fact sheets.
For example:
Section | Completion Weight (CW) | State (S) | CWxS
---|---|---|---
Information | 1 | 53.33% | 1x0.5333=0.5333
Dependencies | 1 | 68.5% | 1x0.685=0.685
Business Support | 1 | 90% | 1x0.9=0.9
Sourcing | 1 | 46.67% | 1x0.4667=0.4667


The completion score of the fact sheet would be:
The sum of completion scores of all sections Σ(CW × S): 0.5333+0.685+0.9+0.4667=2.585
The sum of all section weights Σ(CW): 1+1+1+1=4.
The fact sheet completion score (Σ(CW × S) / Σ(CW)) × 100%: (2.585/4) * 100% = 64.62%.
