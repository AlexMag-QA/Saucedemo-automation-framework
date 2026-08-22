import requests


def test_get_posts_by_user():
    params = {
        "userId": 1
    }

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        params=params
    )

    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]

    data = response.json()

    assert len(data) > 0

    for post in data:
        assert post["userId"] == params["userId"]

def test_get_post_by_user_and_id():
    params = {
        "userId": 1,
        "id": 5
    }

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        params=params
    )

    print(response.url)

    data = response.json()

    print(data)

def test_get_posts_with_headers_and_params():
    headers = {
        "Accept": "application/json",
    }

    params = {
        "userId": 1,
    }

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        headers=headers,
        params=params
    )

    print(response.request.headers)
    print(response.url)
    print(response.status_code)