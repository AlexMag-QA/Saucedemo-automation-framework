import pytest
import allure

from data.checkout_data import (
    FIRST_NAME,
    LAST_NAME,
    POSTAL_CODE,
    EXPECTED_CHECKOUT_INFORMATION_TITLE,
    EXPECTED_CHECKOUT_OVERVIEW_TITLE,
    EXPECTED_CHECKOUT_COMPLETE_TITLE,
    EXPECTED_CHECKOUT_COMPLETE_TEXT,
    EXPECTED_PRODUCT_NAME,
)
from data.products import Products
from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_page import CheckoutPage


@allure.feature("Checkout")
@allure.story("Successful checkout")
@allure.title("Successful checkout")
@allure.description("Verify that a standard user can complete checkout successfully.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_successful_checkout(
        driver,
        authorized_inventory_page
):
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    overview_page = CheckoutOverviewPage(driver)
    complete_page = CheckoutCompletePage(driver)

    with allure.step("Add Backpack to cart"):
        authorized_inventory_page.add_to_cart(
            Products.BACKPACK
        )

    with allure.step("Open cart"):
        authorized_inventory_page.open_cart()

    with allure.step("Start checkout"):
        cart_page.checkout()

        checkout_page.wait_until_title_is(
            EXPECTED_CHECKOUT_INFORMATION_TITLE
        )

        assert (
                checkout_page.get_page_title()
                == EXPECTED_CHECKOUT_INFORMATION_TITLE
        )

    with allure.step("Fill checkout information"):
        checkout_page.enter_first_name(FIRST_NAME)
        checkout_page.enter_last_name(LAST_NAME)
        checkout_page.enter_postal_code(POSTAL_CODE)

        assert checkout_page.get_first_name_value() == FIRST_NAME
        assert checkout_page.get_last_name_value() == LAST_NAME
        assert checkout_page.get_postal_code_value() == POSTAL_CODE

        checkout_page.click_continue()

        overview_page.wait_until_title_is(
            EXPECTED_CHECKOUT_OVERVIEW_TITLE
        )

        assert (
                overview_page.get_overview_title()
                == EXPECTED_CHECKOUT_OVERVIEW_TITLE
        )

    with allure.step("Verify order details"):
        assert (
                overview_page.get_product_name()
                == EXPECTED_PRODUCT_NAME
        )

    with allure.step("Complete checkout"):
        overview_page.click_finish()

        complete_page.wait_until_title_is(
            EXPECTED_CHECKOUT_COMPLETE_TITLE
        )

        assert (
                complete_page.get_page_title()
                == EXPECTED_CHECKOUT_COMPLETE_TITLE
        )

        assert (
                complete_page.get_complete_message()
                == EXPECTED_CHECKOUT_COMPLETE_TEXT
        )
