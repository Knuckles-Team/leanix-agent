##  Manifest File
Here's an example SAP LeanIX manifest file:

```
version: 1
metadata:
  name: disputes-service-v1
  externalId: disputes-service-v1
  description: |
    A microservice responsible for payment disputes.
    This service handles payment transaction disputes and is an integral part of our payment ecosystem.
  type: Backend
  repository:
    url: https://example.com
    status: active
    visibility: private

  applications:
    - factSheetId: fa787383-7233-4896-8fad-c1f1bef30dd2
    - externalId:
        id: applicationId
        value: app-002

  tags:
    - tagGroupName: Domain
      tagNames:
        - Payments

    - tagGroupName: Location
      tagNames:
        - AWS-EU1
        - AWS-EU2

  teams:
    - factSheetId: 63eda74c-57f7-4768-b1c9-3b2813b11504
    - externalId:
        id: teamId
        value: team-002

  resources:
    - name: Disputes Process Flow
      type: documentation
      url: https://myorg.atlassian.net/wiki/spaces/disputes
      description: Disputes process flow and diagrams

  subscriptions:
    - email: test@test.com
      type: OBSERVER
      rolesId:
        - 550e8400-e29b-41d4-a716-446655440000
        - 6ba7b810-9dad-11d1-80b4-00c04fd430c8
```



