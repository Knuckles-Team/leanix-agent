##  Glossary Endpoint
In this section we are going to explain how to use the the Developer Tools of the Chrome Browser to explore the data retrievable from the /p/glossary/(id)/info endpoint. The /p/glossary/(id)/info endpoint itself is not used by the browser when loading a glossary item but it is still possible to explore the data via the /p/glossary endpoint that is used to get the data.
  1. Open up SAP Signavio dictionary.
  2. Open the Developer Tools (Customize and Control (three dots) > More Tools > Developer Tools).
  3. Select the Network tab in the Developer Tools.
  4. Select a Glossary Item.
  5. The Developer Tools now show all the calls the browser does when loading the Glossary Item.
  6. Enter 'glossary' into the filter to get a subset of the calls.
  7. Select the last call and select the preview tab.
  8. Select the entry with the key value pair rel: "info".
  9. The subsection rep contains the same data as provided via the /p/glossary/(id)/info endpoint.
  10. The data shown below the rep keyword is available to the integration via the glossary keyword.
  11. An example of the data that can be retrieved from this endpoint is the category name which would have the Information Source path glossary.categoryName.


![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274f39477a4410148693b7225b31b6c3_LowRes.png)
