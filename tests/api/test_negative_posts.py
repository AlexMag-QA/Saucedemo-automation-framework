import pytest


def test_get_nonexistent_post(posts_client):
    response = posts_client.get_post(999999)

    assert response.status_code == 404

    data = response.json()

    assert data == {}


def test_create_post_with_partial_payload(posts_client):
    payload = {
        "title": "QA Automation"
    }

    response = posts_client.create_post(payload)

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == payload["title"]
    assert "id" in data


@pytest.mark.parametrize(
    "post_id",
    [
        0,
        -1,
        999999,
    ]
)
def test_get_nonexistent_posts(posts_client, post_id):
    response = posts_client.get_post(post_id)

    assert response.status_code == 404
    assert response.json() == {}
