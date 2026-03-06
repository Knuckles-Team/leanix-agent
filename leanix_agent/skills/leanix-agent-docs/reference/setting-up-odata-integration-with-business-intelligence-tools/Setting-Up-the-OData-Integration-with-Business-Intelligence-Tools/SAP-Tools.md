##  SAP Tools
If you use SAP tools such as SAP Analytics Cloud or SAP Datasphere, do the following:
  1. Rename your saved searches to use the saved search ID as the name. You can obtain this ID by navigating to the saved search page and copying the ID from the page URL.
  2. To import saved searches, use the BookmarkDataService.svc endpoint, which supports technical field keys.

```
https://{SUBDOMAIN}.leanix.net/services/import-export/v1/odata/BookmarkDataService.svc/
```



