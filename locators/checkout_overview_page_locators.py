from selenium.webdriver.common.by import By


class CheckoutOverviewPageLocators:
    PAGE_TITLE = (
        By.CSS_SELECTOR,
        "[data-test='title']"
    )

    INVENTORY_ITEM_NAME = (
        By.CSS_SELECTOR,
        "[data-test='inventory-item-name']"
    )

    FINISH_BUTTON = (
        By.CSS_SELECTOR,
        "[data-test='finish']"
    )

