import pytest
import requests


@pytest.mark.parametrize(
    "invalid_token",
    [
        "invalid_token",
        "wrong_token",
        "expired_token",
    ]
)
def test_invalid_tokens(invalid_token):
    headers = {
        "Authorization": f"Bearer {invalid_token}"
    }

    response = requests.get(
        "https://dummyjson.com/auth/me",
        headers=headers
    )

    assert response.status_code == 401

def test_login():
    payload = {
        "username": "emilys",
        "password": "emilyspass"
    }

    response = requests.post(
        "https://dummyjson.com/auth/login",
        json=payload,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["username"] == payload["username"]
    assert data["accessToken"]
    assert data["refreshToken"]

def test_get_current_user():
    login_payload = {
        "username": "emilys",
        "password": "emilyspass"
    }

    login_response = requests.post(
        "https://dummyjson.com/auth/login",
        json=login_payload
    )

    assert login_response.status_code == 200

    login_data = login_response.json()

    token = login_data["accessToken"]

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        "https://dummyjson.com/auth/me",
        headers=headers
    )

    print(response.status_code)
    print(response.json())

def test_get_current_user_without_token():
    response = requests.get(
        "https://dummyjson.com/auth/me"
    )

    assert response.status_code == 401

    data = response.json()

    assert data["message"] == "Access Token is required"

def test_get_current_user_with_invalid_token():
    headers = {
        "Authorization": "Bearer invalid_token"
    }

    response = requests.get(
        "https://dummyjson.com/auth/me",
        headers=headers
    )

    assert response.status_code == 401

    data = response.json()

    assert data["message"] == "Invalid/Expired Token!"

def test_current_user_with_fixture(auth_token):
    headers = {
        "Authorization": f"Bearer {auth_token}"
    }

    response = requests.get(
        "https://dummyjson.com/auth/me",
        headers=headers
    )

    assert response.status_code == 200

    data = response.json()

    assert data["username"] == "emilys"