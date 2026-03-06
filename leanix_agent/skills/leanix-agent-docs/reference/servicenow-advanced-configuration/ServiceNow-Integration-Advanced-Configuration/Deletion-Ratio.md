##  Deletion Ratio
To avoid accidentally the deletion of of Fact Sheets or ServiceNow records because of an erroneous configuration, a deletion ratio threshold can be configured.
The maximumDeletionRatio specifies the deletion ratio in percent. The default value is 50. If the total candidate records for deletion are higher than 50%, then the Integration will not delete those records and output an error in the synclog to review.
If a maximumDeletionRatio is specified and the number of items to delete / synchronized items is less than maximumDeletionRatio, then the synchronization is allowed to delete.
