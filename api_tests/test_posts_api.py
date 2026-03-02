import pytest


BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_posts(api_session):
    response = api_session.get(f"{BASE_URL}/posts")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


def test_get_single_post(api_session):
    response = api_session.get(f"{BASE_URL}/posts/1")

    assert response.status_code == 200
    data = response.json()

    assert data["id"] == 1
    assert "title" in data
    assert "body" in data


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_multiple_posts(api_session, post_id):
    response = api_session.get(f"{BASE_URL}/posts/{post_id}")

    assert response.status_code == 200
    assert response.json()["id"] == post_id


#run test using pytest -v api_tests/