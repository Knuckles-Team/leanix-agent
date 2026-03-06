##  Canceling Subsequent Actions in an Automation
You can cancel subsequent actions in an automation by throwing an error. This stops the automation flow and prevents the execution of all subsequent actions.

```
throw new Error("cancel automation flow");
```



