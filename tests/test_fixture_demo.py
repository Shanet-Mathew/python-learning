import pytest


@pytest.fixture
def sample_user():
    """
    Function-scoped fixture (default scope).
    Runs before every test function.
    """
    print("\n[FUNCTION SETUP] Creating sample user")
    user = {
        "username": "test_user",
        "role": "admin",
        "active": True
    }
    yield user
    print("\n[FUNCTION TEARDOWN] Cleaning up sample user")


def test_user_name(sample_user):
    assert sample_user["username"] == "test_user"


def test_user_role(sample_user):
    assert sample_user["role"] == "admin"


def test_user_is_active(sample_user):
    assert sample_user["active"] is True


def test_module_configuration(module_config):
    assert module_config["environment"] == "staging"
    assert module_config["version"] == "1.0"


def test_api_base_url(api_base_url):
    assert api_base_url.startswith("https")
    assert "jsonplaceholder" in api_base_url