import requests

from config.api_settings import JSONPLACEHOLDER_BASE_URL


class PostsClient:
    TIMEOUT = 10

    def __init__(self):
        self.session = requests.Session()

    def get_post(self, post_id):
        return self.session.get(
            f"{JSONPLACEHOLDER_BASE_URL}/posts/{post_id}",
            timeout=self.TIMEOUT
        )

    def create_post(self, payload):
        return self.session.post(
            f"{JSONPLACEHOLDER_BASE_URL}/posts",
            json=payload,
            timeout=self.TIMEOUT
        )

    def update_post(self, post_id, payload):
        return self.session.put(
            f"{JSONPLACEHOLDER_BASE_URL}/posts/{post_id}",
            json=payload,
            timeout=self.TIMEOUT
        )

    def patch_post(self, post_id, payload):
        return self.session.patch(
            f"{JSONPLACEHOLDER_BASE_URL}/posts/{post_id}",
            json=payload,
            timeout=self.TIMEOUT
        )

    def delete_post(self, post_id):
        return self.session.delete(
            f"{JSONPLACEHOLDER_BASE_URL}/posts/{post_id}",
            timeout=self.TIMEOUT
        )

    def get_posts(self):
        return self.session.get(
            f"{JSONPLACEHOLDER_BASE_URL}/posts",
            timeout=self.TIMEOUT
        )