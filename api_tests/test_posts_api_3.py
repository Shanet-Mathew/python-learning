import pytest


@pytest.mark.api
def test_get_posts(api_session):
    response = api_session.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200