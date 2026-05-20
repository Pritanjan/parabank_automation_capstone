from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class TransactionHistoryPage(BasePage):

    # Accounts Overview
    ACCOUNTS_OVERVIEW_LINK = (By.LINK_TEXT, "Accounts Overview")
    FIRST_ACCOUNT_LINK     = (By.XPATH, "//table[@id='accountTable']//a")
    TRANSACTION_TABLE      = (By.ID, "transactionTable")
    TRANSACTION_ROWS       = (By.XPATH, "//table[@id='transactionTable']//tbody/tr")
    TRANSACTION_DATE       = (By.XPATH, "//table[@id='transactionTable']//tbody/tr[1]/td[1]")
    TRANSACTION_DESC       = (By.XPATH, "//table[@id='transactionTable']//tbody/tr[1]/td[2]")
    TRANSACTION_DEBIT      = (By.XPATH, "//table[@id='transactionTable']//tbody/tr[1]/td[3]")
    TRANSACTION_CREDIT     = (By.XPATH, "//table[@id='transactionTable']//tbody/tr[1]/td[4]")

    FIND_TRANSACTIONS_URL  = "http://parabank.parasoft.com/parabank/findtrans.htm"

    def click_accounts_overview(self):
        time.sleep(1)
        self.click(self.ACCOUNTS_OVERVIEW_LINK)

    def select_first_account(self):
        self.click(self.FIRST_ACCOUNT_LINK)

    def is_transaction_table_displayed(self):
        return self.is_element_present(self.TRANSACTION_TABLE)

    def get_transaction_count(self):
        return len(self.driver.find_elements(*self.TRANSACTION_ROWS))

    def are_transaction_details_visible(self):
        date   = self.is_element_present(self.TRANSACTION_DATE)
        desc   = self.is_element_present(self.TRANSACTION_DESC)
        debit  = self.is_element_present(self.TRANSACTION_DEBIT)
        credit = self.is_element_present(self.TRANSACTION_CREDIT)
        return date and desc and debit and credit

    def go_to_find_transactions(self):
        self.driver.get(self.FIND_TRANSACTIONS_URL)
        time.sleep(3)