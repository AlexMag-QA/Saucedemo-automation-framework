import pytest

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

    authorized_inventory_page.add_to_cart(
        Products.BACKPACK
    )

    authorized_inventory_page.open_cart()

    cart_page.checkout()

    checkout_page.wait_until_title_is(
        EXPECTED_CHECKOUT_INFORMATION_TITLE
    )
    
    assert (
            checkout_page.get_page_title()
            == EXPECTED_CHECKOUT_INFORMATION_TITLE
    )

    checkout_page.submit_checkout_information(
        FIRST_NAME,
        LAST_NAME,
        POSTAL_CODE,
    )

    overview_page.wait_until_title_is(
        EXPECTED_CHECKOUT_OVERVIEW_TITLE
    )

    assert (
            overview_page.get_overview_title()
            == EXPECTED_CHECKOUT_OVERVIEW_TITLE
    )

    assert (
            overview_page.get_product_name()
            == EXPECTED_PRODUCT_NAME
    )

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
