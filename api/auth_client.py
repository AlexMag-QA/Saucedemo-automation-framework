import time
import requests

from utils.logger import get_logger
from config.api_settings import DUMMYJSON_BASE_URL

from requests.exceptions import (
    ConnectionError,
    SSLError,
    Timeout,
)

class AuthClient:
    logger = get_logger("AuthClient")

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
            try:
                response = self.session.get(
                    url,
                    headers=headers,
                    timeout=(5, 10)
                )

                if response.status_code != 429:
                    return response

                if attempt < max_attempts - 1:
                    delay = 2 ** attempt

                    self.logger.warning(
                        f"Received HTTP 429. "
                        f"Retrying in {delay}s "
                        f"(attempt {attempt + 1}/{max_attempts})"
                    )

                    time.sleep(delay)

            except (ConnectionError, SSLError, Timeout) as error:
                if attempt < max_attempts - 1:
                    delay = 2 ** attempt

                    self.logger.warning(
                        f"Network error: {error}. "
                        f"Retrying in {delay}s "
                        f"(attempt {attempt + 1}/{max_attempts})"
                    )

                    time.sleep(delay)
                else:
                    raise

        return response