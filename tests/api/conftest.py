import pytest
import requests

from api.posts_client import PostsClient


@pytest.fixture
def auth_token():
    payload = {
        "username": "emilys",
        "password": "emilyspass"
    }

    response = requests.post(
        "https://dummyjson.com/auth/login",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    return data["accessToken"]

@pytest.fixture
def posts_client():
    return PostsClient()