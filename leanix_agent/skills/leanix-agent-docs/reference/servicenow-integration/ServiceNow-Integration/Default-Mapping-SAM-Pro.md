##  Default Mapping (SAM Pro)
Connecting IT Component Software in SAP LeanIX with the Software Discovery Model table in ServiceNow is recommended in cases where the Software Product Model table does not contain enough information or the ServiceNow Instance connected is too large to perform dynamic link matching as described in Figure 1.
**Tip**
Review record size
One way to ascertain if this case applies is to check if the total number records collectively within the cmdb_rel_ci , cmdb_sam_sw_install and cmdb_sam_sw_discovery_model table are larger than 1 million records.
In such a case, for customers with ServiceNow SAM Pro, the table of cmdb_sam_sw_discovery_model (Software Discovery Model) should be linked instead to IT Components Software.
However, to ensure only records relevant within SAP LeanIX come through, it is mandatory to have a filter applied to only pull relevant Discovery Models. An example of such a filter to be applied on the Discovery Model table is as follows -
Text

```
statusINmanually normalized,normalized,partially normalized^norm_versionISNOTEMPTY^norm_publisherISNOTEMPTY^norm_typeINlicensable,not licensable,unknown

```



The fields of Product Classification,Main Category, and Product Type within the Software Discovery Model table help in further rationalizing the list of records while setting the filter.
**Restriction**
Review the number of records left with the filter applied
As the table can easily store hundreds and thousands of records, it is important to review the filter applied and the records that remain with it. A good estimate is to ensure that the records remaining in the table are less than <20k records.
![1887](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2757da467a441014b2b6cfcbd658115a_LowRes.png)
Flow that can be used with the filters outlined above for ServiceNow SAM Pro users.
