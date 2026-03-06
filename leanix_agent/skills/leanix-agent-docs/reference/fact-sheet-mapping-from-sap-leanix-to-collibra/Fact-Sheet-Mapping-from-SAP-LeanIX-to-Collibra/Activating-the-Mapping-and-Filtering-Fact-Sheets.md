##  Activating the Mapping and Filtering Fact Sheets
To enable the synchronization of SAP LeanIX fact sheets to Collibra, begin by activating the mapping.
  1. In the Collibra Integration Configuration area, go to the desired fact sheet tab. In this guide, for illustration application mapping is depicted.
  2. Activate the mapping by selecting the Active check box.


In the settings, you have the option to either map all fact sheets of a particular fact sheet type from SAP LeanIX to Collibra, or you can selectively choose a subset of fact sheets to be mapped by using filters.
**Caution**
Data Deletion Risk
The synchronization mode of the integration is conservative. When you narrow down the list of fact sheets using the filter, any Collibra assets that were linked in a previous sync run but are now excluded due to the filter in the current sync will be deleted.
Collibra assets not created by the integration are not affected in anyway.
