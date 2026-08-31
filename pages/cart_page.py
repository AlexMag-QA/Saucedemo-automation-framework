from locators.cart_page_locators import CartPageLocators
from pages.base_page import BasePage


class CartPage(BasePage):

    def checkout(self):
        self.click(*CartPageLocators.CHECKOUT_BUTTON)
        self.wait_until_url_contains(
            "checkout-step-one.html"
        )
