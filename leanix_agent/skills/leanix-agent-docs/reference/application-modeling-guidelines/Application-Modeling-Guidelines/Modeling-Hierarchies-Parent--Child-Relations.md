##  Modeling Hierarchies (Parent / Child Relations)
Applications often consist of multiple entities or modules within a common ecosystem or platform (e.g., ERP systems, CRM systems). The following illustration shows modeling hierarchy using Adobe Creative Cloud as an example.
![Modeling Application Hierarchies](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2749f9a57a441014bf1e91cb51a22c8a_LowRes.png)
Modeling Application Hierarchies
  * Adobe Creative Cloud is a suite that bundles various applications to assist designers in producing visual content. It is modeled as the parent entity.
  * Specific applications within Adobe Creative Cloud, such as Adobe Photoshop for image editing, which support particular business tasks, are modeled as child entities.
  * Adobe Creative Cloud could also be part of a broader design platform that includes other applications for different functions, such as video editing. In this case, a platform fact sheet is used to represent the overarching design platform.
