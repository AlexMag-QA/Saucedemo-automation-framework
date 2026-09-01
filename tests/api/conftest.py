import pytest

from api.posts_client import PostsClient
from api.auth_client import AuthClient


@pytest.fixture
def auth_client():
    return AuthClient()

@pytest.fixture
def auth_token(auth_client):
    response = auth_client.login(
        username="emilys",
        password="emilyspass"
    )

    assert response.status_code == 200

    data = response.json()

    return data["accessToken"]

@pytest.fixture
def posts_client():
    return PostsClient()