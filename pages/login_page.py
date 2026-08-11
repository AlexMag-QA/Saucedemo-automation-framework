from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    def open(self, base_url):
        self.driver.get(base_url)

    def enter_username(self, username):
        self.type(*LoginPageLocators.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.type(*LoginPageLocators.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(*LoginPageLocators.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(*LoginPageLocators.ERROR_MESSAGE)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
