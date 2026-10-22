def test_network_requests(page):
    requests = []

    page.on(
        "request",
        lambda request: requests.append(request.url)
    )

    page.goto("/")

    assert any(
        "saucedemo.com" in url
        for url in requests
    )