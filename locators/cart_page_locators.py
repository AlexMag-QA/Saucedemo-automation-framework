from selenium.webdriver.common.by import By


class CartPageLocators:
    CHECKOUT_BUTTON = (
        By.CSS_SELECTOR,
        '[data-test="checkout"]'
    )
