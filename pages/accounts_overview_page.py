from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AccountsOverviewPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.url = "https://parabank.parasoft.com/parabank/index.htm"

        self.username = (By.NAME, "username")
        self.password = (By.NAME, "password")
        self.login_button = (By.XPATH, "//input[@value='Log In']")

        self.accounts_overview_text = (
            By.XPATH,
            "//h1[contains(text(),'Accounts Overview')]"
        )
        self.first_account_balance = (
            By.XPATH,
            "//table[@id='accountTable']//tbody//tr[1]//td[2]"
        )
        self.second_account_balance = (
            By.XPATH,
            "//table[@id='accountTable']//tbody//tr[2]//td[2]"
        )

    def open_accounts_overview_page(self):

        self.open_url(self.url)

        self.enter_text(self.username, "john")
        self.enter_text(self.password, "demo")

        self.click_element(self.login_button)

    def verify_accounts_page(self):
        return self.is_displayed(self.accounts_overview_text)

    def is_accounts_overview_displayed(self):
        return self.is_displayed(self.accounts_overview_text)

    def get_source_balance(self):
        return self._clean_balance(self.get_text(self.first_account_balance))

    def get_destination_balance(self):
        return self._clean_balance(self.get_text(self.second_account_balance))

    @staticmethod
    def _clean_balance(balance_text):
        return balance_text.replace("$", "").replace(",", "").strip()

# from selenium.webdriver.common.by import By
# from pages.base_page import BasePage
#
#
# class AccountsOverviewPage(BasePage):
#
#     def __init__(self, driver):
#         super().__init__(driver)
#
#         self.url = "https://parabank.parasoft.com/parabank/index.htm"
#
#         self.username = (By.NAME, "username")
#         self.password = (By.NAME, "password")
#         self.login_button = (By.XPATH, "//input[@value='Log In']")
#
#         self.accounts_overview_text = (
#             By.XPATH,
#             "//h1[contains(text(),'Accounts Overview')]"
#         )
#
#         self.account_rows = (
#             By.XPATH,
#             "//table[@id='accountTable']//tbody//tr"
#         )
#
#         self.first_account_balance = (
#             By.XPATH,
#             "//table[@id='accountTable']//tbody//tr[1]//td[2]"
#         )
#
#         self.second_account_balance = (
#             By.XPATH,
#             "//table[@id='accountTable']//tbody//tr[2]//td[2]"
#         )
#
#     def open_accounts_overview_page(self):
#
#         self.open_url(self.url)
#
#         self.enter_text(self.username, "john")
#         self.enter_text(self.password, "demo")
#
#         self.click_element(self.login_button)
#
#     def verify_accounts_page(self):
#         return self.is_displayed(self.accounts_overview_text)
#
#     def is_accounts_overview_displayed(self):
#         return self.is_displayed(self.accounts_overview_text)
#
#     def get_source_balance(self):
#         balance_text = self.get_text(self.first_account_balance)
#         return balance_text.replace("$", "").replace(",", "").strip()
#
#     def get_destination_balance(self):
#         balance_text = self.get_text(self.second_account_balance)
#         return balance_text.replace("$", "").replace(",", "").strip()
