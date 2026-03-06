##  Meta Model Extension
SAP LeanIX Technology Risk and Compliance extends the meta model by adding the microservice fact sheet subtype, along with additional fields and relations that offer more context about each microservice. The meta model extension as part of SAP LeanIX Technology Risk and Compliance includes the following:
  * Fact sheet subtypes:
    * Microservice subtype for the application fact sheet.
    * Business application subtype for the application fact sheet, if it's not yet configured.
    * Team subtype for the organization fact sheet, if it's not yet configured.
  * Relations:
    * Relation between microservice and business application fact sheet subtypes to indicate which business application uses a specific microservice.
    * Relation between microservice and team fact sheet subtypes to capture which team uses a specific microservice.
  * Fields on the microservice fact sheet subtype:
    * Repository Status: indicates if the underlying git repository is active or inactive
    * Repository Visibility: indicates if the underlying git repository is internal, public, or private
    * Repository URL: the URL of the underlying git repository
    * Technology Discovery ID: holds the external ID that uniquely identifies the microservice from an external source (e.g., GitHub).
    * Is SBOM attached: to indicate whether an SBOM is linked to the fact sheet. The number of SBOM components linked to the fact sheet is shown on the right side pane of the fact sheet.
    * Type: the type of microservice to help differentiate the different nuances, for example, UI (micro frontend), Backend, Data (ML/AI service), etc.
    * SBOM URL: the URL to the SBOM explorer for the particular microservice.
    * Last Updated (SBOM): The date when a microservice last received a new SBOM.
  * Field on the IT component fact sheet: Tech Stack Discovery ID


![Fields to Provide More Context to the Discovered Microservice](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27481a607a44101494e1abe4f3a85891_LowRes.png)
Fields to Provide More Context to the Discovered Microservice
YesNo
Send
