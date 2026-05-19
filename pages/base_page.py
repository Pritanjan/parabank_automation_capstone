"""
Base Page for Parabank Framework
"""

import time

from selenium.webdriver.support.ui import (
    WebDriverWait,
    Select
)

from selenium.webdriver.support import (
    expected_conditions as EC
)

from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException
)


class BasePage:

    BASE_URL = "http://parabank.parasoft.com/parabank"

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # =========================
    # OPEN URL METHODS
    # =========================

    def open(self, path="index.htm"):

        self.driver.get(f"{self.BASE_URL}/{path}")

    # Compatibility Method
    def open_url(self, url):

        self.driver.get(url)

    def get_current_url(self):

        return self.driver.current_url

    def get_title(self):

        return self.driver.title

    # =========================
    # WAIT METHODS
    # =========================

    def wait_for_element(self, locator, timeout=20):

        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_visible(self, locator, timeout=20):

        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator, timeout=20):

        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    # =========================
    # ACTION METHODS
    # =========================

    def click(self, locator):

        element = self.wait_for_clickable(locator)

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    # Compatibility Method
    def click_element(self, locator):

        self.click(locator)

    def type_text(self, locator, text):

        element = self.wait_for_visible(locator)

        element.clear()
        element.send_keys(text)

    # Compatibility Method
    def enter_text(self, locator, text):

        self.type_text(locator, text)

    def get_text(self, locator):

        return self.wait_for_visible(locator).text

    # Compatibility Method
    def is_displayed(self, locator):

        try:

            return self.wait_for_visible(locator).is_displayed()

        except Exception:

            return False

    # =========================
    # VALIDATION METHODS
    # =========================

    def is_element_present(self, locator, timeout=5):

        try:

            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )

            return True

        except TimeoutException:

            return False

    def get_element_text_safe(self, locator, timeout=5):

        try:

            return WebDriverWait(
                self.driver,
                timeout
            ).until(
                EC.visibility_of_element_located(locator)
            ).text

        except (
            TimeoutException,
            NoSuchElementException
        ):

            return ""

    # =========================
    # DROPDOWN METHODS
    # =========================

    def select_dropdown_by_index(
            self,
            locator,
            index
    ):

        Select(
            self.wait_for_element(locator)
        ).select_by_index(index)

    # =========================
    # UTIL METHODS
    # =========================

    def take_screenshot(self, filename):

        self.driver.save_screenshot(
            f"reports/{filename}.png"
        )

    def hard_wait(self, seconds):

        time.sleep(seconds)