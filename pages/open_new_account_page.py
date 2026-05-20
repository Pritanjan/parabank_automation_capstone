from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import (
    Select,
    WebDriverWait
)

from selenium.webdriver.support import (
    expected_conditions as EC
)


class OpenNewAccountPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            30
        )

        self.open_account_link = (
            By.LINK_TEXT,
            "Open New Account"
        )

        self.account_type_dropdown = (
            By.ID,
            "type"
        )

        self.from_account_dropdown = (
            By.ID,
            "fromAccountId"
        )

        self.open_account_button = (
            By.XPATH,
            "//input[@value='Open New Account']"
        )

        self.success_message = (
            By.XPATH,
            "//div[@id='openAccountResult']"
        )

    def click_open_new_account(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.open_account_link
            )
        ).click()

    def select_account_type(
        self,
        account_type
    ):

        dropdown = Select(

            self.wait.until(
                EC.presence_of_element_located(
                    self.account_type_dropdown
                )
            )
        )

        dropdown.select_by_visible_text(
            account_type
        )

    def select_from_account(self):

        dropdown = Select(

            self.wait.until(
                EC.presence_of_element_located(
                    self.from_account_dropdown
                )
            )
        )

        dropdown.select_by_index(0)

    def click_open_account_button(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.open_account_button
            )
        ).click()

    def get_success_message(self):

        element = self.wait.until(
            EC.visibility_of_element_located(
                self.success_message
            )
        )

        return element.text