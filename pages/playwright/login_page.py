from playwright.sync_api import Page, Locator


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        self.username_input: Locator = page.get_by_placeholder(
            "Username"
        )
        self.password_input: Locator = page.get_by_placeholder(
            "Password"
        )
        self.login_button: Locator = page.get_by_role(
            "button", name="Login"
        )
        self.error_message: Locator = page.locator(
            "[data-test='error']"
        )

    def open(self):
        self.page.goto("/")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()