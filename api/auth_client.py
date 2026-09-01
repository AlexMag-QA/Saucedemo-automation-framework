import time
import requests
import requests

from config.api_settings import DUMMYJSON_BASE_URL


class AuthClient:

    def __init__(self):
        self.session = requests.Session()

    def login(self, username, password):
        payload = {
            "username": username,
            "password": password
        }

        return self.session.post(
            f"{DUMMYJSON_BASE_URL}/auth/login",
            json=payload
        )

    def get_current_user(self, token=None):
        headers = {}

        if token:
            headers["Authorization"] = f"Bearer {token}"

        return self._get_with_retry(
            f"{DUMMYJSON_BASE_URL}/auth/me",
            headers=headers
        )

    def _get_with_retry(
            self,
            url,
            headers=None,
            max_attempts=3
    ):
        for attempt in range(max_attempts):
            response = self.session.get(
                url,
                headers=headers
            )

            if response.status_code != 429:
                return response

            print(
                f"Received 429. "
                f"Retry attempt {attempt + 1}/{max_attempts}"
            )
            
            if attempt < max_attempts - 1:
                delay = 2 ** attempt
                time.sleep(delay)

        return response