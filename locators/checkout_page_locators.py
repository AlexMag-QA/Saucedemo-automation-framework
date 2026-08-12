from selenium.webdriver.common.by import By


class CheckoutPageLocators:
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '[data-test="firstName"]')

    LAST_NAME_INPUT = (By.CSS_SELECTOR, '[data-test="lastName"]')

    POSTAL_CODE_INPUT = (By.CSS_SELECTOR, '[data-test="postalCode"]')

    CONTINUE_BUTTON = (By.CSS_SELECTOR, '[data-test="continue"]')
