from utils.response_validator import (
    validate_status_code,
    validate_json_key,
    validate_json_value
)

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_single_post(api_session):
    response = api_session.get(f"{BASE_URL}/posts/1")

    validate_status_code(response, 200)
    validate_json_key(response, "title")
    validate_json_key(response, "body")
    validate_json_value(response, "id", 1)