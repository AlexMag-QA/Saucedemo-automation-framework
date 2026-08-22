import pytest
from pydantic import ValidationError

from models.post_model import PostModel


def test_get_post(posts_client):
    response = posts_client.get_post(1)

    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]

    data = response.json()

    assert data["id"] == 1
    assert "title" in data
    assert "body" in data
    assert "userId" in data


def test_create_post(posts_client):
    payload = {
        "title": "QA Automation",
        "body": "API Client",
        "userId": 1
    }

    response = posts_client.create_post(payload)

    assert response.status_code == 201
    assert "application/json" in response.headers["Content-Type"]

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data


def test_update_post_with_put(posts_client):
    payload = {
        "id": 1,
        "title": "Updated API Automation",
        "body": "Updated with PUT",
        "userId": 1
    }

    response = posts_client.update_post(
        1,
        payload
    )

    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]

    data = response.json()

    assert data["id"] == payload["id"]
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]


def test_patch_post(posts_client):
    payload = {
        "title": "Patched via API Client"
    }

    response = posts_client.patch_post(
        1,
        payload
    )

    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["id"] == 1
    assert data["userId"] == 1
    assert "body" in data


def test_delete_post(posts_client):
    response = posts_client.delete_post(1)

    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]

    data = response.json()

    assert data == {}


def test_get_post_schema(posts_client):
    response = posts_client.get_post(1)

    assert response.status_code == 200

    data = response.json()

    post = PostModel.model_validate(
        data,
        strict=True
    )

    assert post.id == 1


def test_get_posts_schema(posts_client):
    response = posts_client.get_posts()

    assert response.status_code == 200

    data = response.json()

    posts = [
        PostModel.model_validate(
            post,
            strict=True
        )
        for post in data
    ]

    assert len(posts) > 0


def test_pydantic_rejects_wrong_id_type():
    data = {
        "id": "1",
        "title": "QA Automation",
        "body": "API testing",
        "userId": 1
    }

    with pytest.raises(ValidationError):
        PostModel.model_validate(
            data,
            strict=True
        )

@pytest.mark.parametrize(
    "post_id, expected_status",
    [
        (1, 200),
        (2, 200),
        (999999, 404),
    ]
)
def test_get_post_status(
    posts_client,
    post_id,
    expected_status
):
    response = posts_client.get_post(post_id)

    assert response.status_code == expected_status