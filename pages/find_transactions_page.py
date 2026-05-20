from selenium.webdriver.common.by import By


class FindTransactionsPage:

    FIND_TRANSACTIONS_LINK = (By.LINK_TEXT, "Find Transactions")

    TRANSACTION_DATE = (By.ID, "criteria.onDate")
    FIND_BY_DATE_BUTTON = (By.XPATH, "//button[@id='findByDate']")

    TRANSACTION_AMOUNT = (By.ID, "criteria.amount")
    FIND_BY_AMOUNT_BUTTON = (By.XPATH, "//button[@id='findByAmount']")

    TRANSACTION_ID = (By.ID, "criteria.transactionId")
    FIND_BY_ID_BUTTON = (By.XPATH, "//button[@id='findById']")

    RESULT_TABLE = (By.ID, "transactionTable")
    NO_RESULT_MESSAGE = (By.XPATH, "//*[contains(text(),'No transactions found')]")

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_find_transactions(self):
        self.driver.find_element(*self.FIND_TRANSACTIONS_LINK).click()

    def search_by_date(self, date):
        self.driver.find_element(*self.TRANSACTION_DATE).send_keys(date)
        self.driver.find_element(*self.FIND_BY_DATE_BUTTON).click()

    def search_by_amount(self, amount):
        self.driver.find_element(*self.TRANSACTION_AMOUNT).send_keys(amount)
        self.driver.find_element(*self.FIND_BY_AMOUNT_BUTTON).click()

    def search_by_id(self, transaction_id):
        self.driver.find_element(*self.TRANSACTION_ID).send_keys(transaction_id)
        self.driver.find_element(*self.FIND_BY_ID_BUTTON).click()

    def is_transaction_displayed(self):
        return self.driver.find_element(*self.RESULT_TABLE).is_displayed()

    def is_no_transaction_message_displayed(self):
        return self.driver.find_element(*self.NO_RESULT_MESSAGE).is_displayed()