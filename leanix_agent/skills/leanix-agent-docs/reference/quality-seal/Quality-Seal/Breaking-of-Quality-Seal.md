##  Breaking of Quality Seal
As a rule of thumb, users who have permission to update the quality seal do not automatically break it when they change fact sheet fields.
The following table provides information on who can or can not break the quality seal as per the default settings:
Role | Breaking Quality Seal
---|---
Admins | Admins can edit any fact sheet without breaking the quality seal.
Members | Responsible or accountable subscribers of a fact sheet can edit information on that fact sheet without breaking the quality seal. Conversely, a fact sheet's quality seal is broken when members who are not responsible or accountable subscribers for that fact sheet update its attributes.
Viewer | Viewers cannot break the quality seal as they do not have the right to make any changes to fact sheets.


The quality seal breaks when attributes are updated, including:
  * base fields like name, description, etc.
  * updates to fields such as alias, release, etc.
  * updates to mandatory and non-mandatory fields
  * updates to ExternalID
  * updates to resources
  * updates to relations, such as ApplicationToBusinessCapabilityRelation, ParentChildRelation, etc.
  * However, operations under the subscriptions, comments, metrics, and surveys sections do not break the quality seal.


Additionally, the workspace administrator can configure a renewal interval (e.g., 30 days, 3 months, etc.), after which the quality seal automatically breaks, ensuring continuous data quality maintenance. The renewal interval only considers changes to the quality seal status. The interval resets and starts counting when the quality seal is approved. It does not take into account any other updates or modifications made to the fact sheet itself. To learn how to configure the renewal interval, see [Enabling or Disabling the Quality Seal](https://help.sap.com/docs/leanix/ea/quality-seal?locale=en-US&state=PRODUCTION&version=CLOUD#loio275bf80d7a4410148ac1c4fbce489213__enabling_or_disabling_the_quality_seal).
