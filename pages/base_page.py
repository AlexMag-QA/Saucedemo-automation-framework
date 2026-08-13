from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from config.settings import DEFAULT_TIMEOUT, ELEMENT_CHECK_TIMEOUT
from utils.logger import get_logger


class BasePage:
    logger = get_logger("BasePage")

    def __init__(self, driver):
        self.driver = driver

    def find(self, by, value):
        self.logger.debug(
            f"Finding element: by={by}, value={value}"
        )

        try:
            return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
                EC.visibility_of_element_located((by, value))
            )

        except TimeoutException:
            self.logger.error(
                f"Element was not found: by={by}, value={value}"
            )
            raise

    def click(self, by, value):
        self.logger.info(
            f"Clicking element: by={by}, value={value}"
        )

        self.find(by, value).click()

    def type(self, by, value, text):
        self.logger.info(
            f"Typing text into element: by={by}, value={value}"
        )

        self.find(by, value).send_keys(text)

    def get_text(self, by, value):
        return self.find(by, value).text

    def wait_for_text(self, by, value, text):
        WebDriverWait(
            self.driver,
            DEFAULT_TIMEOUT
        ).until(
            EC.text_to_be_present_in_element(
                (by, value),
                text
            )
        )

    def is_element_visible(self, by, value, timeout=ELEMENT_CHECK_TIMEOUT):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            return True
        except TimeoutException:
            return False

    def wait_for_alert(self):
        return WebDriverWait(
            self.driver,
            DEFAULT_TIMEOUT
        ).until(
            EC.alert_is_present()
        )

    def accept_alert(self):
        alert = self.wait_for_alert()
        alert.accept()

    def dismiss_alert(self):
        alert = self.wait_for_alert()
        alert.dismiss()

    def get_alert_text(self):
        alert = self.wait_for_alert()
        return alert.text

    def switch_to_frame(self, by, value):
        WebDriverWait(
            self.driver,
            DEFAULT_TIMEOUT
        ).until(
            EC.frame_to_be_available_and_switch_to_it(
                (by, value)
            )
        )

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def get_current_window(self):
        return self.driver.current_window_handle

    def get_all_windows(self):
        return self.driver.window_handles

    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)

    def close_current_window(self):
        self.driver.close()

    def hover(self, by, value):
        element = self.find(by, value)

        ActionChains(self.driver).move_to_element(
            element
        ).perform()

    def select_by_visible_text(
            self,
            by,
            value,
            text
    ):
        element = self.find(by, value)

        Select(element).select_by_visible_text(text)

    def get_selected_text(self, by, value):
        element = self.find(by, value)

        return Select(element).first_selected_option.text
