##  Calculating the Total Number of Users from Fields on Relations
This calculation determines the total number of users associated with an application by summing up the number of users from relations to organizations. numberOfUsers is a field on the relApplicationToOrganization relation.
The function starts by initializing a variable, sumOfUsers, to zero to store the total user count. It then iterates over each relation between an application and organization through the relApplicationToOrganization relation to capture the number of users. The function returns the total number of users and writes it to the target field.
**Sample Code**

```
export function main() {
    let sumOfUsers = 0;
    for (const org of data.relApplicationToOrganization) {
        if (org.numberOfUsers != null) {
            sumOfUsers += org.numberOfUsers;
        }
    }
    return sumOfUsers;
}
```



