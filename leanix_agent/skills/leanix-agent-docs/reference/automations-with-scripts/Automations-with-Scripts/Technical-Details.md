##  Technical Details
  * The script editor supports JavaScript as per the ECMAScript 2023 (ES2023) specification.
  * Supported operations:
    * Read: Reading a field value
    * Update: Updating a field value
    * Delete: Setting a field value to empty
  * Target attributes: All fact sheet fields. For some fields, update and delete operations are not supported. For details, see [Limitations for Fields](https://help.sap.com/docs/leanix/ea/automations-with-scripts?locale=en-US&state=PRODUCTION&version=CLOUD#loio4e7f882df68543b788886781a078b5c2__section_hkh_2k4_vgc).
  * Unsupported attributes:
    * Relations
    * Fields on relations
    * Subscriptions
    * Fields of type Location
