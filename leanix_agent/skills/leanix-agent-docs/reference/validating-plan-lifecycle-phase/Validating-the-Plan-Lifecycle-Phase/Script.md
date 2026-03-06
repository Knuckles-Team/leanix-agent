##  Script
**Sample Code**

```
export function main() {
  const planDateText = data.factSheet?.lifecycle?.plan;
  if (!planDateText) throw new Error("cancel automation flow");

  const todayText = new Date().toISOString().slice(0, 10); // "YYYY-MM-DD"

  if (planDateText > todayText) {
    return { lifecycle: { ...data.factSheet.lifecycle, plan: todayText } };
  }

  throw new Error("cancel automation flow");
}
```



