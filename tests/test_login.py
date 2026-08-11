import pytest

from data.test_data import (
    EXPECTED_INVALID_LOGIN_ERROR_TEXT,
    EXPECTED_INVENTORY_TITLE,
    INVALID_LOGIN,
    INVALID_PASSWORD,
    LOGIN,
    PASSWORD,
)
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.smoke
@pytest.mark.regression
def test_login(driver,base_url):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open(base_url)
    login_page.login(LOGIN, PASSWORD)

    assert inventory_page.is_open()
    assert inventory_page.get_page_title() == EXPECTED_INVENTORY_TITLE


@pytest.mark.regression
@pytest.mark.negative
def test_invalid_login(driver, base_url):
    login_page = LoginPage(driver)

    login_page.open(base_url)
    login_page.login(INVALID_LOGIN, INVALID_PASSWORD)

    actual_error = login_page.get_error_message()

    assert EXPECTED_INVALID_LOGIN_ERROR_TEXT in actual_error


