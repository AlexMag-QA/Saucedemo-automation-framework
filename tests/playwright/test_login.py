from playwright.sync_api import expect

from pages.playwright.inventory_page import InventoryPage
from pages.playwright.login_page import LoginPage


def test_successful_login(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("/inventory.html")
    expect(inventory_page.title).to_have_text("Products")

def test_invalid_login(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("wrong_user", "wrong_password")

    expect(login_page.error_message).to_contain_text(
        "Username and password do not match"
    )
    expect(page).to_have_url("/")
