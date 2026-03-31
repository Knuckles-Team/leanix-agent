#!/usr/bin/python

"""GraphQL API Wrapper for LeanIX Agent.

Provides a GraphQL interface using the `gql` library that mirrors
REST API methods with GraphQL queries and mutations.

Requires: pip install gql[requests]
"""

import logging
from typing import Dict, Any, Optional
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from agent_utilities.decorators import require_auth
from agent_utilities.exceptions import (
    MissingParameterError,
    ParameterError,
)


class GraphQL:
    """A class to interact with LeanIX Agent's GraphQL API."""

    def __init__(
        self,
        url: str = None,
        token: str = None,
        proxies: Dict = None,
        verify: bool = True,
        debug: bool = False,
    ):
        if not url:
            raise MissingParameterError("URL is required")
        if not token:
            raise MissingParameterError("Token is required")

        self.url = f"{url.rstrip('/')}/services/pathfinder/v1/graphql"
        self.token = token
        self.proxies = proxies
        self.verify = verify
        self.debug = debug

        logging.basicConfig(
            level=logging.DEBUG if debug else logging.ERROR,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )

        headers = {"Authorization": f"Bearer {token}"}
        self.transport = RequestsHTTPTransport(
            url=self.url,
            headers=headers,
            verify=verify,
            proxies=proxies,
        )
        self.client = Client(transport=self.transport, fetch_schema_from_transport=True)

    @require_auth
    def execute_gql(
        self,
        query_str: str,
        variables: Optional[Dict[str, Any]] = None,
        operation_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Execute a GraphQL query or mutation.

        Args:
            query_str: The GraphQL query or mutation string.
            variables: Optional dictionary of variables for the query.
            operation_name: Optional name of the operation.

        Returns:
            Dict[str, Any]: The raw GraphQL response dictionary.
        """
        try:
            query = gql(query_str)
            result = self.client.execute(
                query, variable_values=variables, operation_name=operation_name
            )
            if "errors" in result:
                raise ParameterError(f"GraphQL errors: {result['errors']}")
            return result
        except Exception as e:
            logging.error(f"GraphQL execution failed: {str(e)}")
            raise ParameterError(f"Query execution failed: {str(e)}")

    @require_auth
    def query(
        self, query_str: str, variables: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Execute a generic GraphQL query for LeanIX.

        Args:
            query_str: The GraphQL query string.
            variables: Optional dictionary of variables for the query.

        Returns:
            Dict[str, Any]: The raw GraphQL response dictionary.
        """
        return self.execute_gql(query_str, variables=variables)
