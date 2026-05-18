"""
pages/base_page.py
Base Page Object - All pages inherit from this.
Contains common Selenium helper methods.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time


class BasePage:
    BASE_URL = "http://parabank.parasoft.com/parabank"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # ── Navigation ──────────────────────────────────────────────────────────

    def open(self, path=""):
        self.driver.get(f"{self.BASE_URL}/{path}")

    def get_current_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    # ── Wait Helpers ─────────────────────────────────────────────────────────

    def wait_for_element(self, by, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, locator))
        )

    def wait_for_clickable(self, by, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, locator))
        )

    def wait_for_visible(self, by, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, locator))
        )

    def wait_for_text_in_element(self, by, locator, text, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((by, locator), text)
        )

    # ── Element Actions ──────────────────────────────────────────────────────

    def click(self, by, locator):
        element = self.wait_for_clickable(by, locator)
        element.click()

    def type_text(self, by, locator, text):
        element = self.wait_for_element(by, locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, by, locator):
        element = self.wait_for_visible(by, locator)
        return element.text

    def is_element_present(self, by, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, locator))
            )
            return True
        except TimeoutException:
            return False

    def get_element_text_safe(self, by, locator, timeout=5):
        """Returns text or empty string if element not found."""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, locator))
            )
            return element.text
        except (TimeoutException, NoSuchElementException):
            return ""

    def select_dropdown_by_index(self, by, locator, index):
        from selenium.webdriver.support.ui import Select
        element = self.wait_for_element(by, locator)
        Select(element).select_by_index(index)

    def take_screenshot(self, filename):
        self.driver.save_screenshot(f"reports/{filename}.png")
        print(f"📸 Screenshot: reports/{filename}.png")

    def scroll_to_element(self, by, locator):
        element = self.wait_for_element(by, locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element

    def wait(self, seconds):
        time.sleep(seconds)
