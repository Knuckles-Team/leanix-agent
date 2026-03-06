##  Guidelines and Best Practices
  * We recommend modeling the data object in a lean hierarchy, for example, Production as level 1 and Bill of Material as level 2. Another example would be Employee / Contract.
  * Avoid creating redundancies. Well-defined data objects do not overlap. They are mutually exclusive. A good test is to check whether you can assign Level 2 data objects without any ambiguity.
  * Rely on business capabilities. It is very easy to find which data objects exist once you have mapped your business capabilities. This is why we recommend creating a business capability map first.
  * Long-term stability. Properly defined data objects are fairly stable over time, persisting throughout any organizational changes. Only major business changes should affect them.
  * Cross-organizational. Stay specific. Data objects should remain the same, independent of any changes that might happen to the organizational structure.
  * Use existing data models. Many applications (e.g., SAP) will already have an existing data object model. Orient yourself with these when creating your own list.
  * Breadth rather than depth. While more levels can help to get a better structure, it comes at the cost of increased complexity. We recommend keeping it at two levels.
  * Involve relevant parties. Leverage insights from representatives throughout the business. Those responsible for different parts of the business are likely to have the best overviews of data objects. Consider using surveys to collect information.


In the poster below, you can also find tips, examples, and the aforementioned best practices on what is important for using data objects. You can [download![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fwww.leanix.net%2Fen%2Fwiki%2Fit-architecture%2Fenterprise-data-model "https://www.leanix.net/en/wiki/it-architecture/enterprise-data-model") a poster with best practices.
![Click on the image to see the full resolution.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2751b5937a441014a9088777cf20aedf_LowRes.png)
