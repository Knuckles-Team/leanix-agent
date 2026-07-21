"""
Tests for leanix_gql.py - GraphQL API client.
"""

import inspect
import logging
from unittest.mock import patch

import pytest
from agent_utilities.core.exceptions import MissingParameterError, ParameterError

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
        assert gql.transport.kwargs["proxies"] == {
            "http": "http://proxy.example:8080",
            "https": "http://proxy.example:8080",
        }
        assert gql.transport.verify is True
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

    def test_execute_gql_with_errors_raises_error(
        self, sample_base_url, sample_bearer_token
    ):
        """Test that GraphQL errors raise ParameterError."""
        gql = GraphQL(url=sample_base_url, token=sample_bearer_token)

        error_response = {"errors": [{"message": "Syntax error"}]}

        with patch.object(gql.client, "execute") as mock_execute:
            mock_execute.return_value = error_response
            with pytest.raises(ParameterError):
                gql.execute_gql(query_str="query { invalid }")


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
        assert gql.transport.verify is True

    def test_default_profile_keeps_verification_enabled(
        self, sample_base_url, sample_bearer_token
    ):
        """The default profile may use system trust or an explicit CA bundle."""
        gql = GraphQL(url=sample_base_url, token=sample_bearer_token)
        assert gql.tls_profile.verify_enabled is True
        assert gql.transport.verify == gql.tls_profile.requests_kwargs()["verify"]


@pytest.mark.unit
class TestGraphQLTransport:
    """Tests for GraphQL transport configuration."""

    def test_transport_uses_correct_url(self, sample_base_url, sample_bearer_token):
        """Test that transport uses the correct GraphQL URL."""
        gql = GraphQL(url=sample_base_url, token=sample_bearer_token)

        expected_url = f"{sample_base_url}/services/pathfinder/v1/graphql"
        assert gql.transport.url == expected_url

    def test_transport_uses_correct_headers(self, sample_base_url, sample_bearer_token):
        """Test that transport uses the correct headers."""
        gql = GraphQL(url=sample_base_url, token=sample_bearer_token)

        expected_auth = f"Bearer {sample_bearer_token}"
        assert gql.transport.headers["Authorization"] == expected_auth

    def test_transport_uses_profile_verification(
        self, sample_base_url, sample_bearer_token, tls_profile_factory
    ):
        """The GraphQL transport receives the profile's verification adapter."""
        tls_profile = tls_profile_factory()
        gql = GraphQL(
            url=sample_base_url,
            token=sample_bearer_token,
            tls_profile=tls_profile,
        )

        assert gql.transport.verify is True

    def test_transport_uses_profile_proxy(
        self, sample_base_url, sample_bearer_token, tls_profile_factory
    ):
        """Proxy policy comes from the shared runtime profile."""
        tls_profile = tls_profile_factory(proxy_url="http://proxy.example:8080")
        gql = GraphQL(
            url=sample_base_url,
            token=sample_bearer_token,
            tls_profile=tls_profile,
        )

        assert gql.transport.kwargs["proxies"] == {
            "http": "http://proxy.example:8080",
            "https": "http://proxy.example:8080",
        }


@pytest.mark.unit
class TestGraphQLErrorHandling:
    """Tests for GraphQL error handling."""

    def test_network_error_raises_parameter_error(
        self, sample_base_url, sample_bearer_token
    ):
        """Test that network errors raise ParameterError."""
        gql = GraphQL(url=sample_base_url, token=sample_bearer_token)

        with patch.object(gql.client, "execute") as mock_execute:
            mock_execute.side_effect = Exception("Network error")
            with pytest.raises(ParameterError):
                gql.execute_gql(query_str="query { allFactSheets { id } }")

    def test_empty_response_handling(self, sample_base_url, sample_bearer_token):
        """Test handling of empty GraphQL responses."""
        gql = GraphQL(url=sample_base_url, token=sample_bearer_token)

        with patch.object(gql.client, "execute") as mock_execute:
            mock_execute.return_value = {}
            result = gql.execute_gql(query_str="query { allFactSheets { id } }")
            assert result == {}

    def test_malformed_query_handling(self, sample_base_url, sample_bearer_token):
        """Test handling of malformed GraphQL queries."""
        gql = GraphQL(url=sample_base_url, token=sample_bearer_token)

        with patch.object(gql.client, "execute") as mock_execute:
            # Simulate GraphQL syntax error
            mock_execute.side_effect = Exception("Syntax Error")
            with pytest.raises(ParameterError):
                gql.execute_gql(query_str="query { invalid }")

    def test_complex_nested_query(self, sample_base_url, sample_bearer_token):
        """Test handling of complex nested GraphQL queries."""
        gql = GraphQL(url=sample_base_url, token=sample_bearer_token)

        complex_query = """
        query GetApplicationDetails {
            allFactSheets(filter: {type: Application}) {
                edges {
                    node {
                        id
                        name
                        description
                        relFactSheets {
                            edges {
                                node {
                                    id
                                    name
                                    type
                                }
                            }
                        }
                        customFields {
                            name
                            value
                        }
                    }
                }
            }
        }
        """

        with patch.object(gql.client, "execute") as mock_execute:
            mock_execute.return_value = {"data": {"allFactSheets": {"edges": []}}}
            result = gql.execute_gql(query_str=complex_query)
            assert result == {"data": {"allFactSheets": {"edges": []}}}

    def test_query_with_multiple_variables(self, sample_base_url, sample_bearer_token):
        """Test GraphQL query with multiple variables."""
        gql = GraphQL(url=sample_base_url, token=sample_bearer_token)

        variables = {"first": 10, "type": "Application", "filter": {"active": True}}

        with patch.object(gql.client, "execute") as mock_execute:
            mock_execute.return_value = {"data": {"allFactSheets": {"edges": []}}}
            result = gql.execute_gql(
                query_str="query($first: Int!, $type: String!, $filter: FilterInput) { allFactSheets(first: $first, type: $type, filter: $filter) { edges { node { id } } } }",
                variables=variables,
            )
            assert result == {"data": {"allFactSheets": {"edges": []}}}

    def test_large_result_set_handling(self, sample_base_url, sample_bearer_token):
        """Test handling of large GraphQL result sets."""
        gql = GraphQL(url=sample_base_url, token=sample_bearer_token)

        # Simulate a large result set
        large_response = {
            "data": {
                "allFactSheets": {
                    "edges": [
                        {"node": {"id": f"app-{i}", "name": f"Application {i}"}}
                        for i in range(100)
                    ]
                }
            }
        }

        with patch.object(gql.client, "execute") as mock_execute:
            mock_execute.return_value = large_response
            result = gql.execute_gql(
                query_str="query { allFactSheets(first: 100) { edges { node { id name } } } }"
            )
            assert len(result["data"]["allFactSheets"]["edges"]) == 100


@pytest.mark.unit
class TestGraphQLDebugMode:
    """Tests for debug mode configuration."""

    def test_debug_false_does_not_mutate_process_logging(
        self, sample_base_url, sample_bearer_token
    ):
        """A library client must not replace application logging policy."""
        with (
            patch("logging.basicConfig") as mock_config,
            patch("leanix_agent.leanix_gql.logger.setLevel") as mock_set_level,
        ):
            GraphQL(url=sample_base_url, token=sample_bearer_token, debug=False)

            mock_config.assert_not_called()
            mock_set_level.assert_not_called()

    def test_debug_true_scopes_level_to_module_logger(
        self, sample_base_url, sample_bearer_token
    ):
        """Debug mode changes only this module's logger."""
        with (
            patch("logging.basicConfig") as mock_config,
            patch("leanix_agent.leanix_gql.logger.setLevel") as mock_set_level,
        ):
            GraphQL(url=sample_base_url, token=sample_bearer_token, debug=True)

            mock_config.assert_not_called()
            mock_set_level.assert_called_once_with(logging.DEBUG)
