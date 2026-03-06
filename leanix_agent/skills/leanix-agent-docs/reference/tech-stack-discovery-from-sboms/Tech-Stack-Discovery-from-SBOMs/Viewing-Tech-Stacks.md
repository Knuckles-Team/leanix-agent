##  Viewing Tech Stacks
To view tech stacks, go to the inventory, then choose Inventory Tools > Tech Stack Discovery. On the Tech Stack Discovery page, you can view tech stacks and their corresponding fact sheets. The status indicates whether a matching tech stack from the reference catalog is found for an ingested SBOM component. Possible statuses include:
  * Discovered: A matching tech stack from the reference catalog is found for an SBOM component. An IT component fact sheet is automatically created and linked to the reference catalog. Relations between an IT component and the corresponding microservice fact sheets are created.
For tech stacks you add manually, relations are created for the IT component you specify. No new IT components are automatically created in this case.
  * Not Discovered: No matching tech stack from the reference catalog is found for an SBOM component.


To view details for a tech stack, select it on the Tech Stack Discovery page. If discovered, a matching IT component fact sheet and linked microservices appear in the right pane.
SBOM components are matched with tech stacks from the reference catalog based on their unique [purls![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fgithub.com%2Fpackage-url%2Fpurl-spec%2Fblob%2Fmain%2Fpurl-specification.md "https://github.com/package-url/purl-spec/blob/main/purl-specification.md") (package URLs). You can view purl matching rules for a component in the right pane under Purl Matching Rule. For each rule, the count of microservices is displayed when applicable.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio4469667226c1422285a4f7f6e4f31df5_LowRes.png)
Viewing Tech Stack Details
