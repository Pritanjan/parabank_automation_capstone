from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoanRequestPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    loan_amount_input = (By.ID, "amount")
    down_payment_input = (By.ID, "downPayment")
    from_account_dropdown = (By.ID, "fromAccountId")
    apply_now_button = (By.XPATH, "//input[@value='Apply Now']")

    # Methods to interact with the page
    def enter_loan_amount(self, amount):
        self.enter_text(self.loan_amount_input, amount)

    def enter_down_payment(self, down_payment):
        self.enter_text(self.down_payment_input, down_payment)

    def select_from_account(self, account_id):
        dropdown = self.driver.find_element(*self.from_account_dropdown)
        for option in dropdown.find_elements(By.TAG_NAME, 'option'):
            if option.get_attribute('value') == str(account_id):
                option.click()
                break

    def click_apply_now(self):
        self.click_element(self.apply_now_button)