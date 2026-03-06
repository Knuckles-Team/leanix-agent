##  Bookmarks to define search scope
It is possible to not hardcode the search scope into the Integration API configuration but allow users with access to specific bookmarks to dynamically change the scope of Integration API runs by modifying the Bookmark in the Frontend of the application. In Integration API the ID or name of a Bookmark can be configured to be used to set the scope for search based scoping as shown in the below example:
If a bookmark is used, the whole bookmark object is available to be used in JUEL expressions in the processor. The below example shows this by accessing the bookmark name in the updates section.
Example how to use a Bookmark to define the search based scope:

```
{
 "processors": [
  {
   "processorType": "inboundFactSheet",
   "processorName": "Apps from Deployments",
   "processorDescription": "Creates LeanIX Applications from Kubernetes Deployments",
   "type": "Application",
   "filter": {
    "exactType": "Deployment"
   },
   "identifier": {
    "search": {
     "filter": "${true}",
     "multipleMatchesAllowed": true,
     "scopeFromBookmark": "${integration.bookmarks.getBookmarkId('book-1')}"
    }
   },
   "updates": [
    {
     "key": {
      "expr": "description"
     },
     "values": [
      {
       "expr": "bookmark name: '${bookmark.name}' AND id=${integration.bookmarks.getBookmarkId('book-1')}"
      }
     ]
    }
   ]
  }
 ]
}
```



**Note**
Find out details about Bookmarks.
You may output the bookmark object into the description field to inspect the structure and available information in a Bookmark. Use the "test run" mode to not alter any Fact Sheets.
