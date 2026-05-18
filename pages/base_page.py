"""
pages/base_page.py
Base Page Object for Parabank Automation Framework
"""

import time

from selenium.webdriver.common.by import By

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

    BASE_URL = (
        "http://parabank.parasoft.com/parabank"
    )

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            20
        )

    # ─────────────────────────────────────────────
    # Navigation Methods
    # ─────────────────────────────────────────────

    def open(self, path="index.htm"):

        self.driver.get(
            f"{self.BASE_URL}/{path}"
        )

    def get_current_url(self):

        return self.driver.current_url

    def get_title(self):

        return self.driver.title

    # ─────────────────────────────────────────────
    # Wait Methods
    # ─────────────────────────────────────────────

    def wait_for_element(
            self,
            by,
            locator,
            timeout=20
    ):

        return WebDriverWait(
            self.driver,
            timeout
        ).until(
            EC.presence_of_element_located(
                (by, locator)
            )
        )

    def wait_for_visible(
            self,
            by,
            locator,
            timeout=20
    ):

        return WebDriverWait(
            self.driver,
            timeout
        ).until(
            EC.visibility_of_element_located(
                (by, locator)
            )
        )

    def wait_for_clickable(
            self,
            by,
            locator,
            timeout=20
    ):

        return WebDriverWait(
            self.driver,
            timeout
        ).until(
            EC.element_to_be_clickable(
                (by, locator)
            )
        )

    def wait_for_text_in_element(
            self,
            by,
            locator,
            text,
            timeout=20
    ):

        return WebDriverWait(
            self.driver,
            timeout
        ).until(
            EC.text_to_be_present_in_element(
                (by, locator),
                text
            )
        )

    # ─────────────────────────────────────────────
    # Element Actions
    # ─────────────────────────────────────────────

    def click(self, by, locator):

        element = self.wait_for_clickable(
            by,
            locator
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def type_text(self, by, locator, text):

        element = self.wait_for_visible(
            by,
            locator
        )

        element.clear()

        element.send_keys(text)

    def get_text(self, by, locator):

        element = self.wait_for_visible(
            by,
            locator
        )

        return element.text

    def is_element_present(
            self,
            by,
            locator,
            timeout=5
    ):

        try:

            WebDriverWait(
                self.driver,
                timeout
            ).until(
                EC.presence_of_element_located(
                    (by, locator)
                )
            )

            return True

        except TimeoutException:

            return False

    def get_element_text_safe(
            self,
            by,
            locator,
            timeout=5
    ):

        try:

            element = WebDriverWait(
                self.driver,
                timeout
            ).until(
                EC.visibility_of_element_located(
                    (by, locator)
                )
            )

            return element.text

        except (
            TimeoutException,
            NoSuchElementException
        ):

            return ""

    def select_dropdown_by_index(
            self,
            by,
            locator,
            index
    ):

        element = self.wait_for_element(
            by,
            locator
        )

        Select(element).select_by_index(index)

    def scroll_to_element(self, by, locator):

        element = self.wait_for_element(
            by,
            locator
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            element
        )

        return element

    def take_screenshot(self, filename):

        self.driver.save_screenshot(
            f"reports/{filename}.png"
        )

        print(
            f"📸 Screenshot saved:"
            f" reports/{filename}.png"
        )

    def hard_wait(self, seconds):

        time.sleep(seconds)