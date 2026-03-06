##  Explore Best Practices
Before you start adding relations, explore best practices for:
  * Relations between applications and business capabilities
  * Relations between applications and organizations


### Relations Between Applications and Business Capabilities
Follow these best practices:
  * Align applications with business functions: Use business capabilities from the reference catalog to align your application landscape with your business functions. This approach is beneficial when working with standard models like the SAP landscape.
  * Use precise level mappings: Always connect applications to business capabilities at the most detailed level possible. This ensures precise mapping and allows for more insightful analysis.
  * Create direct relations: Aim for a direct relationship between applications and business capabilities. Avoid inserting intermediate layers, such as processes within the business context fact sheet type, between them. If needed, model application-to-process relations in parallel, but don't use them as a replacement for direct business capabilities links.


![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2b93581bd7114501b13c6c4d2c7f1156_LowRes.png)
Relations Between Applications and Business Capabilities
### Relations Between Applications and Organizations
Follow these best practices:
  * Link to the lowest level: Whenever possible, relate applications to the lowest level in the organizational hierarchy. For shared or cross-functional applications, you can associate them with a level 1 (global) organization node to represent shared ownership.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio56619136fc35497c9b0e06faf6abf150_LowRes.png)
Relations Between Applications and Organizations: Linking to the Lowest Level
  * Use hierarchical structuring: You can structure organization subtypes hierarchically, linking applications to the lowest level. Alternatively, map them in parallel hierarchies. This approach allows more than one relation to applications, providing a better representation of ownership and usage.
To determine if the organization owns or only uses applications, specify this through the Usage Type field on the organization-to-application relation. For detailed information, see [Fields on Relations](https://help.sap.com/docs/leanix/ea/fact-sheet-relations?locale=en-US&state=PRODUCTION&version=CLOUD#loio275a0dc97a441014a475ddbf4c6de047__fields_on_relations).
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loiof94ae1b15d1a440381a585a09bc24274_LowRes.png)
Relations Between Applications and Organizations: Hierarchical Structuring
