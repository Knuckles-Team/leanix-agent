##  Execution of the Started iAPI Runs
When triggering the start of an iAPI run via API call, the Integration API scheduled the run to be executed next when an available processing slot becomes available. While the Integration API service is able to scape on demand, there may be heavy load where the underlying system needs to be protected to be still available for standard user operations.
Integration API tries to add as much robustness to the process as possible. Most temporary outages of underlying infrastructure is covered and in case of issues, iAPI continues at the last "save point". Save points are generated behind the scenes and ensure, not all work has to be done again in case of a temporary failure.
When the customer calls a specific iAPI configuration multiple times, the order of execution is not guaranteed. The second call might be processed first and in case of a failure, a newer execution might be picked up first before the retry of the older one starts.
### Configuring the Order of Runs
For cases where the order of execution is important, administrators can add a key/value pair to the root path of the iAPI configuration to ensure that there is only one run for the same configuration executed at a time, and in case of failures, the first triggered run is always picked up first.
While this might be mandatory if an external system sends updates to same information shortly after each other, it may lead to small updates having to wait for big ones.
In case you want to ensure sequential processing in order of starting time of a run, please specify the below key value pair in your configuration
Example of using the sequentialExecution attribute for a sequential execution of runs:

```
{
  "processors": [...],
  "sequentialExecution": true
}
```



