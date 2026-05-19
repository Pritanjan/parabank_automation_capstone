from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class LoanApprovalPage(BasePage):

    LOAN_AMOUNT = (By.ID, "amount")

    DOWN_PAYMENT = (By.ID, "downPayment")

    FROM_ACCOUNT = (By.ID, "fromAccountId")

    APPLY_NOW_BUTTON = (By.XPATH, "//input[@value='Apply Now']")

    LOAN_STATUS = (By.XPATH, "//td[@id='loanStatus']")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_loan_amount(self, amount):
        self.enter_text(self.LOAN_AMOUNT, amount)

    def enter_down_payment(self, payment):
        self.enter_text(self.DOWN_PAYMENT, payment)

    def select_from_account(self):

        dropdown = Select(
            self.find_element(self.FROM_ACCOUNT)
        )

        dropdown.select_by_index(0)

    def click_apply_now(self):
        self.click_element(self.APPLY_NOW_BUTTON)

    def get_result_message(self):

        element = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(
                self.LOAN_STATUS
            )
        )

        return element.text.strip()