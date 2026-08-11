from pathlib import Path

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from config.settings import DEFAULT_TIMEOUT
from pages.base_page import BasePage


def test_alert(driver):
    page = BasePage(driver)

    file_path = (
            Path(__file__).parent
            / "resources"
            / "alert_frame_test.html"
    )

    driver.get(file_path.resolve().as_uri())

    page.click(By.TAG_NAME, "button")

    assert page.get_alert_text() == "Test alert"

    page.accept_alert()


def test_iframe(driver):
    page = BasePage(driver)

    file_path = (
            Path(__file__).parent
            / "resources"
            / "alert_frame_test.html"
    )

    driver.get(file_path.resolve().as_uri())

    page.switch_to_frame(By.ID, "test-frame")

    page.type(
        By.ID,
        "frame-input",
        "Hello iframe",
    )

    page.switch_to_default_content()

def test_new_tab(driver):
    page = BasePage(driver)

    file_path = (
        Path(__file__).parent
        / "resources"
        / "alert_frame_test.html"
    )

    driver.get(file_path.resolve().as_uri())

    original_window = page.get_current_window()

    page.click(By.LINK_TEXT, "Open New Tab")

    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.number_of_windows_to_be(2)
    )

    windows = page.get_all_windows()

    new_window = [
        window
        for window in windows
        if window != original_window
    ][0]

    page.switch_to_window(new_window)

    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.url_contains("example.com")
    )

    assert "example.com" in driver.current_url

    page.close_current_window()

    page.switch_to_window(original_window)

def test_hover(driver):
    page = BasePage(driver)

    file_path = (
        Path(__file__).parent
        / "resources"
        / "alert_frame_test.html"
    )

    driver.get(file_path.resolve().as_uri())

    page.hover(By.ID, "hover-box")

    assert page.get_text(
        By.ID,
        "hover-box"
    ) == "Hovered!"

def test_select(driver):
    page = BasePage(driver)

    file_path = (
        Path(__file__).parent
        / "resources"
        / "alert_frame_test.html"
    )

    driver.get(file_path.resolve().as_uri())

    page.select_by_visible_text(
        By.ID,
        "test-select",
        "Firefox",
    )

    assert page.get_selected_text(
        By.ID,
        "test-select",
    ) == "Firefox"