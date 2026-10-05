import pytest
import allure
import os

from config.settings import DEFAULT_ENVIRONMENT, ENVIRONMENTS
from data.users import Users
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.browser_factory import create_driver
from utils.screenshot import save_screenshot


@pytest.fixture
def login_as(driver, selenium_base_url):
    def login(user):
        login_page = LoginPage(driver)

        login_page.open(selenium_base_url)
        login_page.login(
            user["username"],
            user["password"]
        )

    return login


@pytest.fixture
def driver(selenium_browser, headless, remote_url):
    driver = create_driver(
        selenium_browser,
        headless,
        remote_url
    )

    yield driver

    driver.quit()


@pytest.fixture
def authorized_inventory_page(driver, login_as):
    login_as(Users.STANDARD)

    return InventoryPage(driver)


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default=DEFAULT_ENVIRONMENT,
        choices=ENVIRONMENTS.keys(),
        help="Environment for test execution",
    )

    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode",
    )

    parser.addoption(
        "--selenium-browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox"],
        help="Browser for Selenium test execution",
    )


@pytest.fixture
def environment(request):
    return request.config.getoption("--env")


@pytest.fixture
def selenium_base_url(environment):
    return ENVIRONMENTS[environment]


@pytest.fixture
def headless(request):
    return request.config.getoption("--headless")


@pytest.fixture
def selenium_browser(request):
    return request.config.getoption("--selenium-browser")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when in ("setup", "call") and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            screenshot_path = save_screenshot(
                driver, item.name,
            )

            allure.attach.file(
                str(screenshot_path),
                name="Screenshot on failure",
                attachment_type=allure.attachment_type.PNG,
            )

@pytest.fixture
def remote_url():
    return os.getenv("SELENIUM_REMOTE_URL")