from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class BillPaymentPage(BasePage):
    BILL_PAY_LINK       = (By.LINK_TEXT, "Bill Pay")
    PAYEE_NAME          = (By.NAME, "payee.name")
    ADDRESS             = (By.NAME, "payee.address.street")
    CITY                = (By.NAME, "payee.address.city")
    STATE               = (By.NAME, "payee.address.state")
    ZIP_CODE            = (By.NAME, "payee.address.zipCode")
    PHONE               = (By.NAME, "payee.phoneNumber")
    ACCOUNT_NUMBER      = (By.NAME, "payee.accountNumber")
    VERIFY_ACCOUNT      = (By.NAME, "verifyAccount")
    AMOUNT              = (By.NAME, "amount")
    FROM_ACCOUNT        = (By.NAME, "fromAccountId")
    SEND_PAYMENT_BUTTON = (By.XPATH, "//input[@value='Send Payment']")
    SUCCESS_MESSAGE     = (By.XPATH, "//h1[contains(text(),'Bill Payment Complete')]")
    VALIDATION_ERROR    = (By.CLASS_NAME, "error")

    def click_bill_pay(self):
        self.click(*self.BILL_PAY_LINK)

    def enter_payee_details(self):
        self.type_text(*self.PAYEE_NAME,    "Electricity Board")
        self.type_text(*self.ADDRESS,        "MG Road")
        self.type_text(*self.CITY,           "Bangalore")
        self.type_text(*self.STATE,          "Karnataka")
        self.type_text(*self.ZIP_CODE,       "560001")
        self.type_text(*self.PHONE,          "9876543210")
        self.type_text(*self.ACCOUNT_NUMBER, "12345")
        self.type_text(*self.VERIFY_ACCOUNT, "12345")

    def enter_payment_amount(self, amount):
        self.type_text(*self.AMOUNT, amount)

    def select_from_account(self):
        self.select_dropdown_by_index(*self.FROM_ACCOUNT, 1)

    def click_send_payment(self):
        self.click(*self.SEND_PAYMENT_BUTTON)

    def is_payment_successful(self):
        return self.is_element_present(*self.SUCCESS_MESSAGE)

    def get_success_message(self):
        return self.get_text(*self.SUCCESS_MESSAGE)

    def get_validation_error(self):
        return self.get_element_text_safe(*self.VALIDATION_ERROR)