##  FAQs
### What happens if I delete a leanix.yaml file?
Deleting a leanix.yaml file will unlink the corresponding fact sheet in SAP LeanIX. The external ID for GitHub will be removed, and the fact sheet will no longer be linked to GitHub. However, the fact sheet itself will not be automatically deleted, as it may contain other relevant information. If the fact sheet is no longer needed, you can archive it manually.
### What happens if I manually add or overwrite information in fact sheets linked to a manifest file?
The manifest file is considered the source of truth for all the information it contains. Therefore, any manual changes made to fields owned by the integration will be overwritten on the next update to ensure consistency with the manifest file. However, you can manually update fields or relations not managed by the integration.
### How do you ensure that two manifest files don't write information to the same fact sheet?
The GitHub integration uses the location of the leanix.yaml file as a unique identifier for the microservice, which is then used to create the external ID in the fact sheet. Therefore, even if you copy an identical manifest to two locations, it will create two separate fact sheets. However, if the name attribute in the manifest is identical, the integration will fail to process the second manifest file, as name in the manifest file corresponds to displayName in SAP LeanIX, which is unique.
### I want to restructure a repository with synced leanix.yaml files. What should I consider before doing that?
The location of the manifest file in your repository serves as a unique identifier within SAP LeanIX. If you're planning to restructure a repository and move a leanix.yaml file, you should:
  1. Move the leanix.yaml file to your desired new location. For example, if the file used to reside in acme-org/sample-repo/src, you might move it to acme-org/sample-repo/new_sub_directory.
  2. Manually update the externalId in the manifest file to point to the old external ID (acme-org/sample-repo/src). This ensures the connection between the fact sheet and the moved leanix.yaml file remains intact.

```
version: 1
metadata:
  name: disputes-service-v1
  externalId: acme-org/sample-repo/src
  description: |
    A microservice responsible for payment disputes.
    This service handles payment transaction disputes and is an integral part of our payment ecosystem.
```



