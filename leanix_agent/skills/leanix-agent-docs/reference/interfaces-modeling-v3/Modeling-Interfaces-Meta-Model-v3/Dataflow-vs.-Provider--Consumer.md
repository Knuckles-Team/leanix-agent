##  Dataflow vs. Provider / Consumer
An Interface in LeanIX is related to Applications in two ways:
  * An Interface can have one Provider Application
  * An Interface can have many Consumer Applications


Provider / Consumer does not refer to the direction of data flow. There is a separate attribute for this which is used in the Data Flow report. Instead, it typically refers to ownership and change management. Examples include:
  * LeanIX is the Provider for the public LeanIX REST API (similar to any other public API). The API only changes if LeanIX is changed (e.g. updated to a new major version). Since this is a public API, there may be Consumers you are not aware of. In this situation, it is valid to leave the Consumers field blank.
  * If a system is providing a web service, then the system is the providing Application.
For other technologies (e.g. FTP), determining the Provider or Consumer(s) is not as straightforward. To deal with this, it is good practice to define clear conventions for your organization.
