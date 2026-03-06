##  Adding Custom Tech Stacks Manually
Users with "Write" permission for tech stack discovery can manually add custom tech stacks and specify purl matching rules for incoming purls. This lets you capture tech stacks that are not automatically discovered from ingested SBOMs based on reference catalog data, which is particularly useful for:
  * Your organization’s custom frameworks.
  * Tech stacks not present in the reference catalog.


By adding custom tech stacks, you complete your technology portfolio in SAP LeanIX. You can also exclude specific tech stacks to prevent capturing unwanted technologies. This increases data transparency and lets you manage your self-built software items in one place.
When adding a custom tech stack, you select an IT component fact sheet and define a purl matching rule. The system uses this rule to match incoming SBOMs and containing purls to reference catalog items. If there are matches, the system creates a tech stack and links the IT component you selected to the relevant microservice fact sheets.
**Note**
When you add or update custom tech stacks, the system processes new ingested SBOMs based on the defined rules. Existing imported SBOMs are processed retroactively.
### Purl Matching Rules
With purl matching rules, you can curate your tech stack portfolio. You can include technologies that aren't automatically discovered or exclude those that shouldn't be imported.
Users with "View" permission for tech stack discovery can view purl matching rules. This ensures transparency in how tech stacks are derived from SBOM data.
The image below provides an example of a purl matching rule and the matched items.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio8ad37243a0cb499ebaa971da99c59fb0_LowRes.png)
Purl Matching Rule
### Adding a Custom Tech Stack
  1. On the **Tech Stack Discovery** page, choose **Add Tech Stack**.
  2. Follow the steps in the tech stack creation modal.


### Managing Custom Tech Stacks
Users with "Write" permission for tech stack discovery can do the following:
  * Edit custom tech stacks, including purl matching rules.
  * Delete custom tech stacks. When you delete a custom tech stack or a purl matching rule, the relations between an IT component and microservices are removed. However, no fact sheets are deleted in this scenario. The **Tech Stack Discovery ID** value on the IT component is also removed.


To perform these actions, select a custom tech stack on the **Tech Stack Discovery** page by applying a filter, then choose an action on the right-side pane.
