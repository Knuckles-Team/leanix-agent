##  Editordata Endpoint
In this section we are going to explain how to use the Developer Tools of the Chrome Browser to explore the data retrievable from the /p/editordata?id=(id) endpoint.
  1. Open up a process in SAP Signavio with the model editor
  2. Open the Developer Tools (Customize and Control (three dots) > More Tools > Developer Tools)
  3. Select the Network tab in the Developer Tools and reload the model editor page
  4. The Developer Tools now show all the calls the browser does when loading the model editor
  5. Enter 'editordata' into the filter, to only see the call to the /p/editordata?id=(id) endpoint
  6. Select the entry and select the Preview tab
  7. The Preview tab will show the data that is available via the /p/editordata?id=(id) endpoint
  8. The complete data that is shown is available to the integration via the editordata keyword
  9. One of the more interesting sections of this map is the model.properties map, which for example contains custom fields
