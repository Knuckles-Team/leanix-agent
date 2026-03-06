##  Enhanced Response Payload
The following fields are added to the data object in the response payload:
Field | Description
---|---
jobId | Identifier of the processing job.
workspaceId | Identifier of the workspace.
status | Current status of the job.
errorMessage | Error message provided when the job fails.
created_at | Timestamp indicating when the job was created.
plannedExecutionAt | Timestamp indicating the scheduled execution time.
updatedAt | Timestamp indicating when the job was last updated.


Current payload:

```
{
  "data": {
    "message": "SBOM file successfully processed"
  }
}
```



New payload:

```
{
  "data": {
    "jobId": "5e28492a-5d0e-4dfb-9935-503b0463d0c5",
    "workspaceId": "56f7d2ae-4b03-4c4d-bfbb-b6aae4aa1eb9",
    "status": "SCHEDULED",
    "errorMessage": null,
    "createdAt": "2025-01-28T07:53:25.358Z",
    "plannedExecutionAt": "2025-01-28T07:55:22.102Z",
    "updatedAt": "2025-01-28T07:53:25.358Z"
  }
}
```



