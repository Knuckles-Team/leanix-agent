##  Mapping Type
![Mapping Type dropdown](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27460e547a441014941cc265b15d65c0_LowRes.png)
Mapping Type dropdown
The following table contains mapping types.
Mapping Type | Description | Mandatory Fields | Supported ServiceNow Attribute Type | Supported SAP LeanIX Field Type
---|---|---|---|---
FOREIGN_FIELD | Maps the (untranslated) value (ignoring any labels in SN or SAP LeanIX) of a field to the corresponding field in the child system. |
  * Fact Sheet Field
  * Foreign Field

|
  * String
  * Choice (will send untranslated values)

| Text, Location (will map the raw location address), Lifecycle (will map the name of the current phase), Lifecycle Phase (will map the start date of the respective phase). Location and Lifecycle (current phase) fields can only be used as a source of data, synchronizing from SAP LeanIX to ServiceNow.
URL | Used to map the URL of the SAP LeanIX Fact Sheet to the foreign object. | Foreign Field | String | n/a
FIXED_VALUE | Only to be used to set a constant string value to be sent on every synchronized object. | Fact Sheet Field or Foreign Field | String | n/a
VALUE_MAPPING | Used to map fields with multiple choices. |
  * Fact Sheet Field
  * Foreign Field

| Choice (1:1 mapping only)* certain exceptions explained below | Single Select, Multiple Select (See Advanced Information section)
SUBSCRIPTION |  Used to map subscription values between the systems. When the data sync direction is from SAP LeanIX to ServiceNow, the following options are available:
  * Subscription type
  * Subscription role
  * Subscription role and type

| Fact sheet field |
  * Reference fields that directly refer to the sys_user or sys_user_group table, for example, business_owner field.
  * Glide list fields that directly refer to the sys_user table.

| Fact sheet subscriptions
ARCHIVED_STATUS_MAPPING | Only Allowed when SAP LeanIX is the source. If a fact sheet is archived, then a special value is written to ServiceNow | Foreign Field | Choice. e.g. operational_status field updated with 6. Which has the labelRetired. | n/a
TAG_GROUP_FIELD | Used to map tag group fields | Fact Sheet Field (Tags only / Other Tags) Foreign Field | String | Tag Groups, Other Tags
TAG_GROUP_MAPPING | Used to map tag groups with multiple tags within them. |
  * Fact Sheet Field (Tags Groups)
  * Foreign Field

| Choice | Tag Groups
EXTERNAL_ID | This type is used to map an SAP LeanIX ExternalId field to a ServiceNow column. |
  * Fact Sheet Field (Tags Groups)
  * Foreign Field

| String | External ID Fields
RELATED_FACTSHEETS | Maps a comma-separated list of Display Names of the related Fact Sheets found for the selected relation. |
  * Fact Sheet Field (relation name)
  * Foreign Field

| String (Limited to 100 fact sheets. Once the limit is reached, text is added in the end (+X more). | Relation


To learn more about field types in ServiceNow, refer to the [ServiceNow documentation.![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fdocs.servicenow.com%2Fbundle%2Frome-platform-administration%2Fpage%2Fadminister%2Freference-pages%2Freference%2Fr_FieldTypes.html?locale=en-US&state=PRODUCTION&version=CLOUD "https://docs.servicenow.com/bundle/rome-platform-administration/page/administer/reference-pages/reference/r_FieldTypes.html").
