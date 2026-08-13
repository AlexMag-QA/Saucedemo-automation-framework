from selenium.webdriver.common.by import By


class CheckoutCompletePageLocators:
    PAGE_TITLE = (
        By.CSS_SELECTOR,
        "[data-test='title']"
    )

    COMPLETE_MESSAGE = (
        By.CSS_SELECTOR,
        "[data-test='complete-header']"
    )
