from selenium.webdriver.common.by import By


class InventoryPageLocators:

    PAGE_TITLE = (
        By.CSS_SELECTOR,
        "[data-test='title']"
    )

    CART_BADGE = (
        By.CSS_SELECTOR,
        "[data-test='shopping-cart-badge']"
    )

    CART_LINK = (
        By.CSS_SELECTOR,
        "[data-test='shopping-cart-link']"
    )

    @staticmethod
    def add_to_cart_button(product):
        return (
            By.ID,
            f"add-to-cart-{product}"
        )

    @staticmethod
    def remove_from_cart_button(product):
        return (
            By.ID,
            f"remove-{product}"
        )
