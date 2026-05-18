from selenium.webdriver.common.by import By
#from pages.base_page import BasePage
import time

class LoanRequestPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    loan_amount_input = (By.ID, "amount")
    down_payment_input = (By.ID, "downPayment")
    from_account_dropdown = (By.ID, "fromAccountId")
    apply_now_button = (By.XPATH, "//input[@value='Apply Now']")

    # Methods to interact with the page
    def enter_loan_amount(self, amount):
        self.driver.find_element(*self.loan_amount_input).clear()
        self.driver.find_element(*self.loan_amount_input).send_keys(amount)

    def enter_down_payment(self, down_payment):
        self.driver.find_element(*self.down_payment_input).clear()
        self.driver.find_element(*self.down_payment_input).send_keys(down_payment)

    def select_from_account(self, account_id):
        dropdown = self.driver.find_element(*self.from_account_dropdown)
        for option in dropdown.find_elements(By.TAG_NAME, 'option'):
            if option.get_attribute('value') == str(account_id):
                option.click()
                break

    def click_apply_now(self):
        self.driver.find_element(*self.apply_now_button).click()