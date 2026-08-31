from locators.checkout_overview_page_locators import CheckoutOverviewPageLocators
from pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):
    def get_overview_title(self):
        return self.get_text(*CheckoutOverviewPageLocators.PAGE_TITLE)

    def get_product_name(self):
        return self.get_text(*CheckoutOverviewPageLocators.INVENTORY_ITEM_NAME)

    def click_finish(self):
        self.click(*CheckoutOverviewPageLocators.FINISH_BUTTON)
        self.wait_until_url_contains(
            "checkout-complete.html"
        )

    def wait_until_title_is(self, expected_title):
        self.wait_for_text(
            *CheckoutOverviewPageLocators.PAGE_TITLE,
            expected_title
        )
