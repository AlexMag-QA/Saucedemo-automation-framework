from locators.checkout_page_locators import CheckoutPageLocators
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def enter_first_name(self, first_name):
        self.type(*CheckoutPageLocators.FIRST_NAME_INPUT, first_name)

    def enter_last_name(self, last_name):
        self.type(*CheckoutPageLocators.LAST_NAME_INPUT, last_name)

    def enter_postal_code(self, postal_code):
        self.type(*CheckoutPageLocators.POSTAL_CODE_INPUT, postal_code)

    def click_continue(self):
        self.click(*CheckoutPageLocators.CONTINUE_BUTTON)

    def fill_checkout_information(
            self,
            first_name,
            last_name,
            postal_code
    ):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        self.click_continue()
