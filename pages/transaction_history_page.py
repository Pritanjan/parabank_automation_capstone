from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TransactionHistoryPage(BasePage):

    ACCOUNTS_OVERVIEW_LINK = (By.LINK_TEXT, "Accounts Overview")
    FIND_TRANSACTIONS_LINK = (By.LINK_TEXT, "Find Transactions")
    FIRST_ACCOUNT_LINK = (By.XPATH, "//table[@id='accountTable']//a")
    ACCOUNT_DROPDOWN = (By.ID, "accountId")
    FIND_BY_AMOUNT = (By.ID, "amount")
    FIND_BY_AMOUNT_BUTTON = (By.ID, "findByAmount")
    TRANSACTION_TABLE = (By.ID, "transactionTable")
    TRANSACTION_ROWS = (By.XPATH, "//table[@id='transactionTable']//tbody/tr")

    def click_accounts_overview(self):
        self.click(self.ACCOUNTS_OVERVIEW_LINK)

    def select_first_account(self):
        self.click(self.FIRST_ACCOUNT_LINK)

    def click_find_transactions(self):
        self.click(self.FIND_TRANSACTIONS_LINK)

    def enter_transaction_amount(self, amount):
        self.send_keys(self.FIND_BY_AMOUNT, amount)

    def click_find_by_amount(self):
        self.click(self.FIND_BY_AMOUNT_BUTTON)

    def is_transaction_table_displayed(self):
        return self.is_displayed(self.TRANSACTION_TABLE)

    def get_transaction_count(self):
        return len(self.driver.find_elements(*self.TRANSACTION_ROWS))