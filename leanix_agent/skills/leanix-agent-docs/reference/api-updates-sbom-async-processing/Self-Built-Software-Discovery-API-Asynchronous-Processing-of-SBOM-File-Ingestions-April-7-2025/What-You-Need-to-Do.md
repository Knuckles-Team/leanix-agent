##  What You Need to Do
If your current implementation of /factSheets/{factSheetId}/sboms does not rely on the HTTP status code or the payload, these changes will not affect you. Otherwise, you will need to update your integrations as detailed below.
### Adjust Your Integrations for the New Response Code and Payload
Update your systems to recognize the new 202 HTTP response status code and parse additional response payload fields.
Pseudo code to handle the new status code:

```
function handleApiResponse(response):
  if response.statusCode == 202:
    print("Request accepted. Processing asynchronously.")
    jobId = response.payload.data.jobId
    jobStatus = response.payload.data.status
    jobCreationTime = response.payload.data.created_at
    print("Job ID:", jobId)
    print("Job Status:", jobStatus)
    print("Job Created At:", jobCreationTime)
    return jobId # Save Job ID for status checks
  elif response.statusCode == 201:
    print("Request processed successfully.")
  else:
  print("Error with request. Status Code:", response.statusCode)

# Example of using the function with a hypothetical API response
apiResponse = {
  "statusCode": 202,
  "payload": {
    "data": {
      "jobId": "5e28492a-5d0e-4dfb-9935-503b0463d0c5",
      "status": "In Progress",
      "created_at": "2021-07-01T12:00:00Z"
    }
  }
}
jobId = handleApiResponse(apiResponse)
```



### Adapt Your Requests for Asynchronous Processing
Implement logic to periodically check the job status, accommodating the change from synchronous to asynchronous processing.
Pseudo code to handle the job status:

```
function checkJobStatus(jobId):
  statusEndpoint = "https://api.example.com/job/status/" + jobId
  response = makeHttpRequest(statusEndpoint)
  if response.statusCode == 200:
    jobStatus = response.payload.jobStatus
    print("Current Job Status:", jobStatus)
    return jobStatus
  else:
    print("Failed to retrieve job status. Status Code:", response.statusCode)

function periodicStatusCheck(jobId, interval):
  import time
  jobComplete = False
  while not jobComplete:
    jobStatus = checkJobStatus(jobId)
    if jobStatus == "SUCCEEDED" or jobStatus == "FAILED":
      jobComplete = True
      print("Final Job Status:", jobStatus)
    else:
      print("Continuing to monitor job status...")
      time.sleep(interval) # Delay next check by 'interval' seconds

# Example usage with a job ID and a check interval of 30 seconds
periodicStatusCheck(jobId, 30)
```



