"""
Pytest configuration and shared fixtures for LeanIX agent tests.
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from requests import Response


@pytest.fixture
def mock_response():
    """Create a mock response object."""
    response = Mock(spec=Response)
    response.status_code = 200
    response.headers = {"Content-Type": "application/json"}
    response.text = ""
    response.json.return_value = {}
    return response


@pytest.fixture
def mock_session():
    """Create a mock requests session."""
    session = Mock()
    session.verify = True
    session.headers = {}
    return session


@pytest.fixture
def sample_token():
    """Sample API token for testing."""
    return "LXT_test_token_12345678"


@pytest.fixture
def sample_bearer_token():
    """Sample bearer token for testing."""
    return "eyJraWQiOiJmNzZjNjQyNGQzZTE5NT"


@pytest.fixture
def sample_base_url():
    """Sample base URL for testing."""
    return "https://test-workspace.leanix.net"


@pytest.fixture
def sample_workspace_base_url():
    """Sample workspace base URL for testing."""
    return "https://test-workspace.leanix.net"


@pytest.fixture
def sample_service_base_url():
    """Sample service base URL for testing."""
    return "https://test-workspace.leanix.net/services/pathfinder/v1"


@pytest.fixture
def sample_factsheet_data():
    """Sample FactSheet data for testing."""
    return {
        "id": "test-id-123",
        "name": "Test Application",
        "type": "Application",
        "description": "A test application",
        "displayName": "Test Application",
        "fullName": "Test Application",
        "tags": [],
        "fields": [],
        "relations": [],
        "milestones": [],
        "status": "ACTIVE",
    }


@pytest.fixture
def sample_factsheets_response():
    """Sample FactSheets list response."""
    return {
        "status": "OK",
        "errors": [],
        "total": 2,
        "data": [
            {
                "id": "test-id-1",
                "name": "Test Application 1",
                "type": "Application",
                "description": "First test application",
                "displayName": "Test Application 1",
                "fullName": "Test Application 1",
                "tags": [],
                "fields": [],
                "relations": [],
                "milestones": [],
                "status": "ACTIVE",
            },
            {
                "id": "test-id-2",
                "name": "Test Application 2",
                "type": "Application",
                "description": "Second test application",
                "displayName": "Test Application 2",
                "fullName": "Test Application 2",
                "tags": [],
                "fields": [],
                "relations": [],
                "milestones": [],
                "status": "ACTIVE",
            },
        ],
    }


@pytest.fixture
def sample_graphql_response():
    """Sample GraphQL response."""
    return {
        "allFactSheets": {
            "edges": [
                {
                    "node": {
                        "id": "test-id-1",
                        "name": "Test Application 1",
                        "type": "Application",
                    }
                },
                {
                    "node": {
                        "id": "test-id-2",
                        "name": "Test Application 2",
                        "type": "Application",
                    }
                },
            ]
        }
    }


@pytest.fixture
def mock_auth_response(sample_bearer_token):
    """Create a mock successful authentication response."""
    response = Mock(spec=Response)
    response.status_code = 200
    response.json.return_value = {
        "access_token": sample_bearer_token,
        "token_type": "Bearer",
        "expires_in": 3600,
    }
    return response


@pytest.fixture
def mock_auth_error_response():
    """Create a mock authentication error response."""
    response = Mock(spec=Response)
    response.status_code = 401
    response.text = '{"error": "Invalid token"}'
    return response


@pytest.fixture
def mock_forbidden_response():
    """Create a mock forbidden response."""
    response = Mock(spec=Response)
    response.status_code = 403
    response.text = '{"error": "Access forbidden"}'
    return response


@pytest.fixture
def mock_not_found_response():
    """Create a mock not found response."""
    response = Mock(spec=Response)
    response.status_code = 404
    response.text = '{"error": "Not found"}'
    return response
