from locators.inventory_page_locators import InventoryPageLocators
from pages.base_page import BasePage


class InventoryPage(BasePage):

    def get_page_title(self):
        return self.get_text(*InventoryPageLocators.PAGE_TITLE)

    def is_open(self):
        return self.driver.current_url.endswith("/inventory.html")

    def add_to_cart(self, product):
        locator = InventoryPageLocators.add_to_cart_button(product)
        self.click(*locator)

    def remove_from_cart(self, product):
        locator = InventoryPageLocators.remove_from_cart_button(product)
        self.click(*locator)

    def get_cart_items_count(self):
        return self.get_text(*InventoryPageLocators.CART_BADGE)

    def has_cart_badge(self):
        return self.is_element_visible(
            *InventoryPageLocators.CART_BADGE
        )

    def wait_until_cart_badge_is_hidden(self):
        self.wait_until_element_is_invisible(
            *InventoryPageLocators.CART_BADGE
        )

    def open_cart(self):
        self.click(*InventoryPageLocators.CART_LINK)