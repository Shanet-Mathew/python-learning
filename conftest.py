import pytest
import requests


@pytest.fixture(scope="session")
def api_session():
    """
    Session-scoped API session.
    Reuses TCP connection across tests.
    """
    print("\n[SESSION SETUP] Creating API session")
    session = requests.Session()
    session.headers.update({
        "Content-Type": "application/json"
    })

    yield session

    print("\n[SESSION TEARDOWN] Closing API session")
    session.close() 


@pytest.fixture
def module_config():
    return {
        "environment": "staging",
        "version": "1.0"
    }


@pytest.fixture
def api_base_url():
    """
    Base URL for API tests
    """
    return "https://jsonplaceholder.typicode.com"


# import pytest


# @pytest.fixture(scope="session")
# def api_base_url():
#     """
#     Session-scoped fixture.
#     Created once per test session.
#     """
#     print("\n[SESSION SETUP] Initializing API base URL")
#     base_url = "https://jsonplaceholder.typicode.com"
#     yield base_url
#     print("\n[SESSION TEARDOWN] Test session finished")


# @pytest.fixture(scope="module")
# def module_config():
#     """
#     Module-scoped fixture.
#     Created once per test module.
#     """
#     print("\n[MODULE SETUP] Loading module configuration")
#     config = {
#         "environment": "staging",
#         "version": "1.0"
#     }
#     yield config
#     print("\n[MODULE TEARDOWN] Module execution complete")