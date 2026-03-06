##  Model Endpoint
In this section, we are going to explain how to use the Developer Tools of the Chrome Browser to explore the data retrievable from the /p/model/(id)/info endpoint. The SAP Signavio model editor does not call the endpoint itself, that's why we are going to use the /p/directory/ endpoint to retrieve the same data as given by the /p/mode/(id)/info endpoint.
  1. Open up a process in SAP Signavio with the model editor.
  2. Open the Developer Tools (Customize and Control (three dots) > More Tools > Developer Tools).
  3. Select the Network tab in the Developer Tools and reload the model editor page.
  4. The Developer Tools now show all the calls the browser does when loading the model editor.
  5. Enter 'p/directory/' into the filter, to only see the call to the /p/directory/ endpoint.
  6. Select the entry and select to the Preview tab.
  7. The Preview tab will show the data that is available via the /p/directory/ endpoint.
  8. The data given from this endpoint is a list of all the processes in the same directory.
  9. Select the entry where href: "/model/(id)" matches the id of the current process which can be found in the url.
  10. The subsection rep contains the same data as provided via the /p/model/(id)/info endpoint.
  11. The data shown below the rep keyword is available to the integration via the model keyword.
  12. An example of the data that can be retrieved from this endpoint is the published status which would have the Information Source path model.status.publish.


![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2753ef577a441014bc5adc7e70f7e4be_LowRes.png)
