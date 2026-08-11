import pytest

from config.settings import DEFAULT_ENVIRONMENT, ENVIRONMENTS
from data.users import Users
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.browser_factory import create_driver
from utils.screenshot import save_screenshot


@pytest.fixture
def login_as(driver, base_url):
    def login(user):
        login_page = LoginPage(driver)

        login_page.open(base_url)
        login_page.login(
            user["username"],
            user["password"]
        )

    return login


@pytest.fixture
def driver(browser, headless):
    driver = create_driver(browser, headless)

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
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox"],
        help="Browser for test execution",
    )


@pytest.fixture
def environment(request):
    return request.config.getoption("--env")


@pytest.fixture
def base_url(environment):
    return ENVIRONMENTS[environment]


@pytest.fixture
def headless(request):
    return request.config.getoption("--headless")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


@pytest.hookimpl(hookwrapper=True) 
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when in ("setup", "call") and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            save_screenshot(
                driver,
                item.name,
            )