def test_get_post(playwright):
    api_context = playwright.request.new_context()

    try:
        response = api_context.get(
            "https://jsonplaceholder.typicode.com/posts/1"
        )

        assert response.status == 200

        data = response.json()

        assert data["id"] == 1
        assert data["userId"] == 1

    finally:
        api_context.dispose()