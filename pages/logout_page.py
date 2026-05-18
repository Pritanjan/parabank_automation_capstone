from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogoutPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 20)

        self.logout_link = (
            By.PARTIAL_LINK_TEXT,
            "Log Out"
        )

        self.login_button = (
            By.NAME,
            "username"
        )

    def click_logout(self):

        logout_btn = self.wait.until(
            EC.visibility_of_element_located(
                self.logout_link
            )
        )

        logout_btn.click()

    def is_login_page_displayed(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.login_button
            )
        ).is_displayed()