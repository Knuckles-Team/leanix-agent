##  Mapping and Synchronization
  * Establish the source of truth
    * SAP Signavio masters the processes, and hence, it remains the source of truth for processes and their relations to other architectural elements.
    * Make SAP LeanIX the source of truth for all other architectural elements, including applications, business capabilities, data objects, and more.
  * Define the scope of the elements you want to synchronize
    * Start with the essentials and map processes, applications, business capabilities, and organizations for comprehensive reporting.
    * Additional elements can always be synchronized in the future if you need them.
  * Determine how detailed you want your mapping to be:
    * For processes, go down to the lowest level in your BPM architecture to provide maximum value for business users. While this level may not be necessary for enterprise architecture purposes, SAP LeanIX's reporting features allow Enterprise Architects to aggregate them to levels tailored to their specific needs.
    * Map business capabilities at least up to level 2 and till up to level 4 to get a meaningful insight yet manageable aggregation. But first, ensure you have created a relevant dictionary category for business capabilities, as there is no default dictionary category for business capabilities in SAP Signavio.
  * Create custom attributes
    * You can add custom attributes for improved insights and better alignment. For example, in SAP LeanIX, create a custom field on a business context fact sheet to store process owner information from SAP Signavio.
    * Similarly, you can create custom attributes in dictionary categories of type ‘text’, to store relevant information from SAP LeanIX.
    * To link imported dictionary items to processes, create custom attributes with the data type of corresponding dictionary categories, either at the process diagram level or the object level. We recommend creating the following custom attributes at a minimum:
      * Linked Applications (at the task level)
      * Linked Business Capabilities (at the diagram level)
      * Linked Organizations (at the diagram level)
For a step-by-step guide on creating such custom attributes, see [Creating Custom Attributes in Dictionary Categories](https://help.sap.com/docs/leanix/ea/best-practices-and-tutorials?locale=en-US&state=PRODUCTION&version=CLOUD#loio2758ecda7a4410148fc2e2c4b70df0d1__creating_custom_attributes_in_dictionary_categories).
  * Link the imported items to processes
    * After you have imported applications, business capabilities, and organizations into SAP Signavio, ensure they are linked to the processes. Relation between processes and architectural elements are synchronized to SAP LeanIX only when you have established the relation in SAP Signavio.
    * Linking business capabilities to processes is valuable in understanding how these capabilities are supported by the corresponding processes.
    * Link imported initiatives to the affected process.
