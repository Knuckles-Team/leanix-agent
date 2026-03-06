##  Step 6: Configure the Execution Status Calculation (Optional)
You have the option to use a calculation to automatically set the execution status based on the percentages reflected in the execution progress field in the initiative fact sheet.
To set up the calculation, do the following:
  1. Go to Administration > Calculations.
  2. Choose New Calculation.
  3. Under Create from Scratch, choose Create.
  4. Enter a name and description for the calculation.
**Example**
Name: Progress Tracking
Description: Defines progress statuses using simple, rule-based logic that maps specific execution progress percentage ranges to the execution status labels within an initiative fact sheet.
  5. Select Initiative as the target fact sheet type.
  6. Select Execution Status as the target field.
  7. Copy and paste following code snippet:
**Sample Code**

```
export function main() {
    const progress = data.lxExecutionProgress || 0;

    if (progress === 0 ) {
        return null;
    }

    if (progress >= 0 && progress <= 0.3) {
        return 'red';
    }

    if (progress > 0.3 && progress < 0.6) {
        return 'yellow';
    }

    if (progress >= 0.6) {
        return 'green';
    }

    return null;

}
```



  8. Choose Save and Activate.


**Tip**
If your organization has more complex needs, you can extend this logic using additional fields like due dates or custom tags. For more information on setting up advanced calculations, refer to [Calculations](https://help.sap.com/docs/leanix/ea/calculations?locale=en-US&state=PRODUCTION&version=CLOUD "Calculations let you populate fact sheet fields based on values from other fields. Use calculation templates for common scenarios or configure your own to define custom logic.").
