##  Additional Configuration Details
Configure Details is a button that is only offered for some special mapping types to provide more configuration, like a mapping of fixed values for choices.
One example of the use of the Configure Details section is the VALUE_MAPPING. VALUE_MAPPING is used when fixed values from SINGLE_SELECT fields must be mapped to choices in the CHOICE field type in ServiceNow.
The example below shows VALUE_MAPPING configuration of SAP LeanIX's businessCriticality field with ServiceNow's business_criticality attribute.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2749c7467a4410149e6aee4b8a132495_LowRes.png)
Here the left side indicates the Meta Model name values of within the businessCriticality field in SAP LeanIX. Similarly, the right side is mapped to the value of the choices within the business_criticality attribute in ServiceNow.
![The left column contains the strings used on the SAP LeanIX side, and the right column contains the values used in ServiceNow choice fields.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2755d0157a441014990cb1c55c6afe51_LowRes.png)
The left column contains the strings used on the SAP LeanIX side, and the right column contains the values used in ServiceNow choice fields.
**Tip**
Use Fact Sheet configuration menu to get the meta model key of the fields in SAP LeanIX. Translations are not relevant in the VALUE_MAPPING section
The meta model keys are visible within brackets, as seen below -
![The `data-model` values in -](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27448a3a7a441014997bd42ab9b0264a_LowRes.png)
The Meta Model values in - "()"
Similarly, within ServiceNow, they can be seen by right-clicking on the field and selecting "Show Choice List"(Admin access required) -
![3496](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274c846e7a441014814592f77f1fd252_LowRes.png)
Select - Show Choice List
Only the VALUES section is required for the mapping -
![3496](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274b3f5a7a44101485d1ed75070c4241_LowRes.png)
Only the Value section is required for the mapping
Each VALUE_MAPPING is validated when you save the configuration, and during every synchronization, to ensure only valid values are used for mapping from SAP LeanIX to ServiceNow.
**Note**
n:1 Value Mapping Supported only when the source of truth is SAP LeanIX
Attaching multiple values in the SINGLE_SELECT field to 1 VALUE in the Choice List field in ServiceNow is supported, provided the source of truth is SAP LeanIX.
![`n:1` Value Mapping support. Business Operational and Administrative Service Criticality both get mapped to the Low choice in ServiceNow.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274c52d17a441014854ef2cd40952514_LowRes.png)
n:1 Value Mapping support. Business Operational and Administrative Service Criticality both get mapped to the Low choice in ServiceNow.
