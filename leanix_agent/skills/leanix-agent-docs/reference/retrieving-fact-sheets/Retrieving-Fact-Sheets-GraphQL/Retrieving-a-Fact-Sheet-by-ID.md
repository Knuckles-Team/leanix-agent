##  Retrieving a Fact Sheet by ID
To retrieve a fact sheet by ID, use the factSheet query.
The id argument is required for this query. To find the ID of a fact sheet, navigate to the fact sheet page and copy the ID from the URL.
Example query:

```
{
  factSheet(id: "28fe4aa2-6e46-41a1-a131-72afb3acf256") {
    id
    name
    type
  }
}
```



Example response:

```
{
  "data": {
    "factSheet": {
      "id": "28fe4aa2-6e46-41a1-a131-72afb3acf256",
      "name": "AC Management",
      "type": "Application"
    }
  }
}
```



