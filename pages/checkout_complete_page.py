from locators.checkout_complete_page_locators import CheckoutCompletePageLocators
from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):

    def get_page_title(self):
        return self.get_text(*CheckoutCompletePageLocators.PAGE_TITLE)


    def get_complete_message(self):
        return self.get_text(*CheckoutCompletePageLocators.COMPLETE_MESSAGE)

    def wait_until_title_is(self, expected_title):
        self.wait_for_text(
            *CheckoutCompletePageLocators.PAGE_TITLE,
            expected_title
        )
        