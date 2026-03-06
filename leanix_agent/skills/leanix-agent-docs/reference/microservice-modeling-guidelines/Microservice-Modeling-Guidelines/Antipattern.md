##  Antipattern
SAP LeanIX is an enterprise architecture tool, and it is not intended for modeling individual microservice deployments across different technical environments, as in a Configuration Management Database (CMDB) system.
Modeling every microservice deployment across different technical environments is not recommended, as it creates unnecessary clutter in the workspace with hundreds of fact sheets that provide little value.
Instead, what could be useful is to model instances of microservices in different regions or business units where they are managed separately or have independent implications—e.g., for disaster recovery.
YesNo
Send
