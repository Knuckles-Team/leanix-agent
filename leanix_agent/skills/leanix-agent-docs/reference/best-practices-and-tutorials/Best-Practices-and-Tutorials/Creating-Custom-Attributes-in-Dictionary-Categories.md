##  Creating Custom Attributes in Dictionary Categories
In SAP Signavio, to link dictionary items imported from SAP LeanIX to processes and use them in process definition, we recommend creating custom attributes. These attributes must have the data type of the corresponding dictionary categories. You can create them either at the process diagram level or the object level.
To do so:
  1. In the explorer, go to Setup > Define notations/attributes.
  2. In the Modeling language tab, select a notation for which you want to link SAP LeanIX data, such as a Business Process Diagram (BPMN 2.0) or Value Chain.
  3. Select a diagram to link information at the diagram level, such as mapping business capabilities to processes, or choose a specific diagram element to link information at the object level, such as applications to process steps.
  4. In the Custom Attributes tab, click Add.
  5. To create a new attribute, choose Create new attribute.
  6. Fill in the Name and Description fields for at least one language offered.
  7. From the Data type dropdown, select Dictionary Link.
  8. From the Only for dropdown, choose the relevant dictionary category for the SAP LeanIX data being synced.
  9. You can create list attributes by activating As list. This allows you to assign multiple dictionary entries of the selected category to the attribute, such as for linking multiple applications or business capabilities.
  10. Click Create attribute to finalize.


YesNo
Send
![close icon](https://consent.trustarc.com/get?name=sapglow-close-icon.png)
This site uses cookies and related technologies, as described in our Cookie Statement, for purposes that may include site operation, analytics, enhanced user experience, or advertising. You may choose to consent to our use of these technologies, or manage your own preferences.
Understood Manage Settings
[Privacy Statement](https://help.sap.com/docs/privacy)|[Cookie Statement](https://www.sap.com/about/legal/privacy/cookies.html)
