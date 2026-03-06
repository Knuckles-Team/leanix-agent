##  General Configuration parts
Mandatory configuration fields are:
  * configId (optional): string identifier for each configuration. Default value is "lxApptio" if not included
  * active: true/false. Activates/deactivates the configuration. A configuration must be active in order to use it for a run, and only valid configurations can be saved as active=true
  * data: main section containing connection, read and write configuration. The field apptioConnectionConfig needs to be specified at least
