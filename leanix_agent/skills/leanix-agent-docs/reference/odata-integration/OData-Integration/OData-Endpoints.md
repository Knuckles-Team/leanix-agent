##  OData Endpoints
**Caution**
Add a trailing slash to the endpoint URL as shown below. The ID of a saved search is appended to the URL. A missing trailing slash results in an unsuccessful request.
The integration supports two REST API endpoints that adhere to the OData standard. These endpoints let you export your saved searches, known as bookmarks within APIs. Both endpoints deliver the same data but differ in their representation of field names:
  * BookmarkService.svc: Uses readable field names, also called labels (for example, Display Name).

```
https://{SUBDOMAIN}.leanix.net/services/import-export/v1/odata/BookmarkService.svc/
```



  * BookmarkDataService.svc: Uses technical field keys (for example, Application_displayName).

```
https://{SUBDOMAIN}.leanix.net/services/import-export/v1/odata/BookmarkDataService.svc/
```



