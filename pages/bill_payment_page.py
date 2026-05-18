from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class BillPaymentPage(BasePage):

    BILL_PAY_LINK = (By.LINK_TEXT, "Bill Pay")
    PAYEE_NAME = (By.NAME, "payee.name")
    ADDRESS = (By.NAME, "payee.address.street")
    CITY = (By.NAME, "payee.address.city")
    STATE = (By.NAME, "payee.address.state")
    ZIP_CODE = (By.NAME, "payee.address.zipCode")
    PHONE = (By.NAME, "payee.phoneNumber")
    ACCOUNT_NUMBER = (By.NAME, "payee.accountNumber")
    VERIFY_ACCOUNT = (By.NAME, "verifyAccount")
    AMOUNT = (By.NAME, "amount")
    FROM_ACCOUNT = (By.NAME, "fromAccountId")
    SEND_PAYMENT_BUTTON = (By.XPATH, "//input[@value='Send Payment']")
    SUCCESS_MESSAGE = (By.XPATH, "//h1[contains(text(),'Bill Payment Complete')]")

    def click_bill_pay(self):
        self.click(self.BILL_PAY_LINK)

    def enter_payee_details(self):
        self.send_keys(self.PAYEE_NAME, "Electricity Board")
        self.send_keys(self.ADDRESS, "MG Road")
        self.send_keys(self.CITY, "Bangalore")
        self.send_keys(self.STATE, "Karnataka")
        self.send_keys(self.ZIP_CODE, "560001")
        self.send_keys(self.PHONE, "9876543210")
        self.send_keys(self.ACCOUNT_NUMBER, "12345")
        self.send_keys(self.VERIFY_ACCOUNT, "12345")

    def enter_payment_amount(self, amount):
        self.send_keys(self.AMOUNT, amount)

    def click_send_payment(self):
        self.click(self.SEND_PAYMENT_BUTTON)

    def is_payment_successful(self):
        return self.is_displayed(self.SUCCESS_MESSAGE)