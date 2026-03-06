##  Calculating the Total Number of Interfaces from Relations
This calculation determines the total number of interfaces associated with an application, including both provided and consumed interfaces. The function starts by retrieving the lengths of two data arrays from a fact sheet. The first array, data.relConsumerApplicationToInterface, contains the count of interfaces that applications consume, derived from relations between consumer applications and interfaces. The second array, data.relProviderApplicationToInterface, includes the count of interfaces that applications provide, derived from relations between provider applications and interfaces. By adding these values, the function returns the total number of interfaces linked to applications and writes it to the target field.
**Sample Code**

```
export function main() {
    const numberConsumedInterfaces = data.relConsumerApplicationToInterface.length;
    const numberProvidedInterfaces = data.relProviderApplicationToInterface.length;
    return numberConsumedInterfaces + numberProvidedInterfaces;
}
```



