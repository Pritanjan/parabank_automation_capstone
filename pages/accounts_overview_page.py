from selenium.webdriver.common.by import By

class AccountsOverviewPage:

    def __init__(self, driver):

        self.driver = driver

        self.accounts_overview_link = (
            By.LINK_TEXT,
            "Accounts Overview"
        )

        self.accounts_table = (
            By.ID,
            "accountTable"
        )

        self.account_details = (
            By.XPATH,
            "//table[@id='accountTable']"
        )

    def open_accounts_overview_page(self):

        self.driver.find_element(
            *self.accounts_overview_link
        ).click()

    def verify_accounts_overview_displayed(self):

        return self.driver.find_element(
            *self.accounts_table
        ).is_displayed()

    def get_account_information(self):

        return self.driver.find_element(
            *self.account_details
        ).text