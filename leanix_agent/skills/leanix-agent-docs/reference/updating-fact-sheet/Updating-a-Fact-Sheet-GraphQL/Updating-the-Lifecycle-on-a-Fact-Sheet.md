##  Updating the Lifecycle on a Fact Sheet
In the following example, we update the lifecycle on a fact sheet by changing the start dates of specific phases through the replace patch operation.
Ensure to include all phases and their corresponding values in the input, even if you only want to update a single phase. Any phases that are not included in the input are deleted. For example, if you only include the plan phase in the input, the mutation will update this phase and delete all others.
The remove patch operation deletes all phases, regardless of the specific phases included in the input.
Example mutation:

```
mutation ($patches: [Patch]!) {
  updateFactSheet(id: "85be63bf-6347-4f20-a306-2d06a10dc6f3", patches: $patches) {
    factSheet {
      ... on Initiative {
        lifecycle {
          phases {
            phase
            startDate
          }
        }
      }
    }
  }
}
```



Variables:

```
{
  "patches": [
    {
      "op": "replace",
      "path": "/lifecycle",
      "value": "{\"phases\":[{\"phase\":\"plan\",\"startDate\":\"2019-01-12\"}, {\"phase\":\"phaseIn\",\"startDate\":\"2020-03-12\"}, {\"phase\":\"active\",\"startDate\":\"2021-05-10\"}, {\"phase\":\"phaseOut\",\"startDate\":\"2025-03-30\"}, {\"phase\":\"endOfLife\",\"startDate\":\"2027-01-01\"}]}"
    }
  ]
}
```



Example response:

```
{
  "data": {
    "updateFactSheet": {
      "factSheet": {
        "lifecycle": {
          "phases": [
            {
              "phase": "plan",
              "startDate": "2019-01-12",
              "milestoneId": null
            },
            {
              "phase": "phaseIn",
              "startDate": "2020-03-12",
              "milestoneId": null
            },
            {
              "phase": "active",
              "startDate": "2021-05-10",
              "milestoneId": null
            },
            {
              "phase": "phaseOut",
              "startDate": "2025-03-30",
              "milestoneId": null
            },
            {
              "phase": "endOfLife",
              "startDate": "2027-01-01",
              "milestoneId": null
            }
          ]
        }
      }
    }
  }
}
```



