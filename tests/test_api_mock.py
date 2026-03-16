# tests/test_api_mock.py

from unittest.mock import patch
from utils.api_client import get_post


@patch("utils.api_client.requests.get")
def test_get_post_mock(mock_get):
    
    mock_response = {
        "userId": 1,
        "id": 1,
        "title": "mock title",
        "body": "mock body"
    }

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    result = get_post(1)

    assert result["id"] == 1
    assert result["title"] == "mock title"