def test_mock_api_response(page):

    def mock_response(route):
        route.fulfill(
            status=200,
            content_type="application/json",
            body='{"id": 1, "title": "Mocked product"}'
        )

    page.route(
        "**/posts/1",
        mock_response
    )

    response = page.goto(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    assert response.status == 200

    data = response.json()

    assert data["title"] == "Mocked product"