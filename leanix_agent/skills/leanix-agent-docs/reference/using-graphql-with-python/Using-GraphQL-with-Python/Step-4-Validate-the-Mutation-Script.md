##  Step 4: Validate the Mutation Script
To validate the mutation script, you can retrieve the comment that you added using the factSheet GraphQL query. To do this, we'll modify our existing query.py script.
Follow these steps:
  1. In the query.py file, replace the main function with the following code:
query.py

```
def main():
    """Executes a query against the LeanIX GraphQL API and prints
    the output.
    """
    factsheet_id = '13f60713-4b8e-40b3-b680-64262d0e0e64'
    access_token = _obtain_access_token()
    graphql_query = """
    {
        factSheet(id: "%s") {
            comments {
                edges {
                    node {
                        id
                        message
                    }
                }
            }
        }
    }
    """ % (factsheet_id)

    data = {'query': graphql_query}
    auth_header = f'Bearer {access_token}'

    response = requests.post(
        url=LEANIX_GRAPHQL_URL,
        headers={'Authorization': auth_header},
        data=json.dumps(data)
    )
    response.raise_for_status()
    print(response.json())
```



  2. Run the query.py script.

```
LEANIX_SUBDOMAIN="{{YOUR_LEANIX_SUBDOMAIN}}" LEANIX_API_TOKEN="{{YOUR_LEANIX_API_TOKEN}}" poetry run python query.py
```





You get a response in your console that contains the comment id and message, which confirms that the mutation script works as expected.
Example response:

```
{
  "data": {
    "factSheet": {
      "comments": {
        "edges": [
          {
            "node": {
              "id": "4f45247c-fdc5-4650-a4c7-6af39e3d7d64",
              "message": "What successor is planned for this?"
            }
          }
        ]
      }
    }
  }
}
```



To view comments in the application user interface, navigate to the Comments tab on a Fact Sheet.
