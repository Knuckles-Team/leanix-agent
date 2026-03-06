##  Applications
Microservices play a crucial role in supporting business applications. They are essentially small, independent services that work together to run a complex application. Each microservice is a self-contained unit that performs a unique function within the broader application ecosystem.
The applications section is necessary to establish the correct association between the microservice and the corresponding business applications. Microservices can be linked to multiple business applications, so you can provide multiple different business application fact sheets.
Attribute | Required | Description
---|---|---
factSheetId | Required if name is not provided | The IDs of business application fact sheets.
name | Required if factSheetId is not provided | The names of business application fact sheets, corresponding to the full names.
externalId | Required if factSheetId and name are not provided | The externalId of business application fact sheets.


**Note**
If you provide the factSheetId, name, and externalId attributes, the system prioritizes them in this order: factSheetId first, followed by externalId, and then name.
