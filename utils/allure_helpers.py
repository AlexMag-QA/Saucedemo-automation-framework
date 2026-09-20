import json

import allure


def attach_response(response):
    allure.attach(
        str(response.status_code),
        name="Response status code",
        attachment_type=allure.attachment_type.TEXT,
    )

    try:
        response_body = json.dumps(
            response.json(),
            indent=2,
            ensure_ascii=False,
        )
        attachment_type = allure.attachment_type.JSON
    except ValueError:
        response_body = response.text
        attachment_type = allure.attachment_type.TEXT

    allure.attach(
        response_body,
        name="Response body",
        attachment_type=attachment_type,
    )

def attach_request(response):
    request = response.request

    allure.attach(
        request.method,
        name="Request method",
        attachment_type=allure.attachment_type.TEXT,
    )

    allure.attach(
        request.url,
        name="Request URL",
        attachment_type=allure.attachment_type.TEXT,
    )

    if request.body:
        body = request.body

        if isinstance(body, bytes):
            body = body.decode("utf-8")

        try:
            body = json.dumps(
                json.loads(body),
                indent=2,
                ensure_ascii=False,
            )
            attachment_type = allure.attachment_type.JSON
        except (json.JSONDecodeError, TypeError):
            attachment_type = allure.attachment_type.TEXT

        allure.attach(
            body,
            name="Request body",
            attachment_type=attachment_type,
        )

def attach_api_exchange(response):
    attach_request(response)
    attach_response(response)