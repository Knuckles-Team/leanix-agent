##  Creating a URL from a String
This calculation generates a URL by concatenating a base URL with an external identifier (externalId) from a fact sheet. The function starts by defining a baseUrl constant https://www.external-system.com/. It then checks if a fact sheet contains a valid externalId. If an externalId exists, the function concatenates the baseUrl with the externalId to create the complete URL and returns it. If the externalId is explicitly set to null, the function returns null, and the target field is set to empty.
**Sample Code**

```
export function main() {
    if (data.externalId == null) {
        return null;
    }

    const baseUrl = "https://www.external-system.com/";
    const url = baseUrl.concat(data.externalId);
    return url;
}
```



