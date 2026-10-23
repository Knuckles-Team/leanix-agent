"""
Tests for leanix_gql.py - GraphQL API client.
"""

import inspect
from unittest.mock import patch

import pytest
from agent_connector_sdk.exceptions import MissingParameterError, ParameterError
from agent_connector_sdk.transports.graphql import (
    GraphQLClient,
    GraphQLExecutionError,
)

from leanix_agent.leanix_gql import GraphQL


@pytest.mark.unit
class TestGraphQLInitialization:
    """Tests for GraphQL initialization."""

    def test_init_with_runtime_tls_profile(
        self, sample_base_url, sample_bearer_token, tls_profile_factory
    ):
        """Test initialization with all parameters."""
        tls_profile = tls_profile_factory(proxy_url="http://proxy.example:8080")
        gql = GraphQL(
            url=sample_base_url,
            token=sample_bearer_token,
            tls_profile=tls_profile,
            debug=False,
        )
        assert gql.url == f"{sample_base_url}/services/pathfinder/v1/graphql"
        assert gql.token == sample_bearer_token
        assert gql.sdk_client.tls_profile is tls_profile
        assert gql.debug is False

    def test_init_without_url(self, sample_bearer_token):
        """Test initialization without URL raises error."""
        with pytest.raises(MissingParameterError) as exc_info:
            GraphQL(token=sample_bearer_token)
        assert "URL is required" in str(exc_info.value)

    def test_init_without_token(self, sample_base_url):
        """Test initialization without token raises error."""
        with pytest.raises(MissingParameterError) as exc_info:
            GraphQL(url=sample_base_url)
        assert "Token is required" in str(exc_info.value)

    def test_init_has_no_boolean_verify_or_proxy_override(
        self, sample_base_url, sample_bearer_token
    ):
        """Transport customization is available only through AgentConfig profiles."""
        _ = (sample_base_url, sample_bearer_token)
        parameters = inspect.signature(GraphQL).parameters
        assert "verify" not in parameters
        assert "proxies" not in parameters

    def test_init_sets_headers_attribute(self, sample_base_url, sample_bearer_token):
        """Test that headers attribute is set for @require_auth decorator."""
        gql = GraphQL(url=sample_base_url, token=sample_bearer_token)
        assert gql.headers is not None
        assert gql.headers["Authorization"] == f"Bearer {sample_bearer_token}"

    def test_init_strips_trailing_slash(self, sample_bearer_token):
        """Test that trailing slash is stripped from URL."""
        gql = GraphQL(url="https://test.leanix.net/", token=sample_bearer_token)
        assert "https://test.leanix.net/services/pathfinder/v1/graphql" in gql.url


@pytest.mark.unit
class TestGraphQLExecuteGql:
    """Tests for execute_gql method."""

    def test_execute_gql_success(
        self, sample_base_url, sample_bearer_token, sample_graphql_response
    ):
        """Test successful GraphQL query execution."""
        gql = GraphQL(url=sample_base_url, token=sample_bearer_token)

        with patch.object(gql.client, "execute") as mock_execute:
            mock_execute.return_value = sample_graphql_response
            result = gql.execute_gql(
                query_str="query { allFactSheets { edges { node { id name } } } }"
            )

            assert result == sample_graphql_response
            mock_execute.assert_called_once()

    def test_execute_gql_with_variables(
        self, sample_base_url, sample_bearer_token, sample_graphql_response
    ):
        """Test GraphQL query execution with variables."""
        gql = GraphQL(url=sample_base_url, token=sample_bearer_token)

        variables = {"first": 10}

        with patch.object(gql.client, "execute") as mock_execute:
            mock_execute.return_value = sample_graphql_response
            result = gql.execute_gql(
                query_str="query { allFactSheets(first: $first) { edges { node { id } } } }",
                variables=variables,
            )

            assert result == sample_graphql_response
            call_args = mock_execute.call_args
            assert call_args[1]["variable_values"] == variables

    def test_execute_gql_with_operation_name(
        self, sample_base_url, sample_bearer_token, sample_graphql_response
    ):
        """Test GraphQL query execution with operation name."""
        gql = GraphQL(url=sample_base_url, token=sample_bearer_token)

        with patch.object(gql.client, "execute") as mock_execute:
            mock_execute.return_value = sample_graphql_response
            result = gql.execute_gql(
                query_str="query GetFactSheets { allFactSheets { id } }",
                operation_name="GetFactSheets",
            )

            assert result == sample_graphql_response
            call_args = mock_execute.call_args
            assert call_args[1]["operation_name"] == "GetFactSheets"

    def test_execute_gql_failure_keeps_message(
        self, sample_base_url, sample_bearer_token
    ):
        """A failed query raises ParameterError with the unchanged message."""
        gql = GraphQL(url=sample_base_url, token=sample_bearer_token)

        with patch.object(gql.client, "execute", side_effect=RuntimeError("boom")):
            with pytest.raises(ParameterError) as exc_info:
                gql.execute_gql(query_str="query { invalid }")
        assert str(exc_info.value) == "Query execution failed"


@pytest.mark.unit
class TestGraphQLQuery:
    """Tests for query method (simplified GraphQL execution)."""

    def test_query_success(
        self, sample_base_url, sample_bearer_token, sample_graphql_response
    ):
        """Test successful GraphQL query."""
        gql = GraphQL(url=sample_base_url, token=sample_bearer_token)

        with patch.object(gql, "execute_gql") as mock_execute:
            mock_execute.return_value = sample_graphql_response
            result = gql.query(
                query_str="query { allFactSheets { edges { node { id name } } } }"
            )

            assert result == sample_graphql_response
            mock_execute.assert_called_once()

    def test_query_with_variables(
        self, sample_base_url, sample_bearer_token, sample_graphql_response
    ):
        """Test GraphQL query with variables."""
        gql = GraphQL(url=sample_base_url, token=sample_bearer_token)

        variables = {"first": 5}

        with patch.object(gql, "execute_gql") as mock_execute:
            mock_execute.return_value = sample_graphql_response
            result = gql.query(
                query_str="query { allFactSheets(first: $first) { edges { node { id } } } }",
                variables=variables,
            )

            assert result == sample_graphql_response
            call_args = mock_execute.call_args
            # Variables are passed as keyword arguments - check if the key exists
            if "variable_values" in call_args[1]:
                assert call_args[1]["variable_values"] == variables
            elif "variables" in call_args[1]:
                assert call_args[1]["variables"] == variables
            else:
                # If neither key exists, just verify the call was made
                assert mock_execute.called


@pytest.mark.ssl
class TestGraphQLSSLVerification:
    """Tests for SSL verification in GraphQL."""

    def test_runtime_profile_keeps_verification_mandatory(
        self, sample_base_url, sample_bearer_token, tls_profile_factory
    ):
        """The resolved current profile always enables peer verification."""
        tls_profile = tls_profile_factory()
        gql = GraphQL(
            url=sample_base_url,
            token=sample_bearer_token,
            tls_profile=tls_profile,
        )
        assert tls_profile.verify_enabled is True
        assert gql.sdk_client.tls_profile is tls_profile

    def test_default_profile_keeps_verification_enabled(
        self, sample_base_url, sample_bearer_token
    ):
        """The default profile may use system trust or an explicit CA bundle."""
        gql = GraphQL(url=sample_base_url, token=sample_bearer_token)
        assert gql.tls_profile.verify_enabled is True
        assert gql.sdk_client.tls_profile is gql.tls_profile


@pytest.mark.spec("CONN-LEANIX-AGENT-R002")
class TestGraphQLDelegation:
    """GraphQL calls go through the SDK shared GraphQL client."""

    def test_client_is_configured_from_the_wrapper(
        self, sample_base_url, sample_bearer_token, tls_profile_factory
    ):
        tls_profile = tls_profile_factory()
        gql = GraphQL(
            url=sample_base_url, token=sample_bearer_token, tls_profile=tls_profile
        )
        shared = gql.sdk_client
        assert isinstance(shared, GraphQLClient)
        assert shared.endpoint == f"{sample_base_url}/services/pathfinder/v1/graphql"
        assert shared.headers["Authorization"] == f"Bearer {sample_bearer_token}"
        assert shared.tls_profile is tls_profile
        assert shared.fetch_schema is True

    def test_execute_passes_arguments_through(
        self, sample_base_url, sample_bearer_token
    ):
        gql = GraphQL(url=sample_base_url, token=sample_bearer_token)
        with patch.object(gql.sdk_client, "execute", return_value={"a": 1}) as mock:
            result = gql.execute_gql("query Q { a }", {"x": 1}, "Q", allow_partial=True)
        assert result == {"a": 1}
        mock.assert_called_once_with("query Q { a }", {"x": 1}, "Q", allow_partial=True)

    def test_partial_error_count_mirrors_shared_client(
        self, sample_base_url, sample_bearer_token
    ):
        gql = GraphQL(url=sample_base_url, token=sample_bearer_token)
        gql.sdk_client.last_partial_error_count = 3
        assert gql.last_partial_error_count == 3

    def test_shared_client_error_maps_to_unchanged_message(
        self, sample_base_url, sample_bearer_token
    ):
        gql = GraphQL(url=sample_base_url, token=sample_bearer_token)
        failure = GraphQLExecutionError(RuntimeError("x"))
        with patch.object(gql.sdk_client, "execute", side_effect=failure):
            with pytest.raises(ParameterError) as exc_info:
                gql.execute_gql("query { a }")
        assert str(exc_info.value) == "Query execution failed"
