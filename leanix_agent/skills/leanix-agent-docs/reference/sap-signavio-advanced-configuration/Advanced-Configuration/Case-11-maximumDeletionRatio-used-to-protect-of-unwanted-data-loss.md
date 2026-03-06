##  Case 11: maximumDeletionRatio used to protect of unwanted data loss
The configuration field maximumDeletionRatio specifies a ratio that is always checked before the synchronization decides whether or not to delete data in strict mode in SAP LeanIX or SAP Signavio. This feature is a kind of safety net used to protect your data when setting up or changing the synchronization configuration and this is not perfect and contains mistakes.
Before a deletion the synchronization computes for each process sync descriptor and glossary sync descriptor the ratio:
computed ratio = 100 * /
A deletion of items is only allowed in case of :
a) < 10 OR
b) <maximumDeletionRatio

```
{
 "active": true,
 "maximumDeletionRatio": 50,
 "timerBasedSync": true
}

```



