from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TransferFundsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.transfer_funds_link = (
            By.LINK_TEXT,
            "Transfer Funds"
        )
        self.from_account_dropdown = (
            By.NAME,
            "fromAccountId"
        )
        self.to_account_dropdown = (
            By.NAME,
            "toAccountId"
        )
        self.amount_input = (
            By.NAME,
            "amount"
        )
        self.transfer_button = (
            By.XPATH,
            "//input[@value='Transfer']"
        )
        self.transfer_complete_header = (
            By.XPATH,
            "//h1[contains(text(),'Transfer Complete')]"
        )
        self.transfer_result_message = (
            By.XPATH,
            "//div[@id='rightPanel']//p"
        )

    def navigate_to_transfer_funds(self):
        try:
            self.click_element(self.transfer_funds_link)
        except Exception:
            self.open("transfer.htm")

    def transfer_funds(self, amount):
        self.select_dropdown_by_index(self.from_account_dropdown, 0)
        self.select_dropdown_by_index(self.to_account_dropdown, 1)
        self.type_text(self.amount_input, amount)
        self.click_element(self.transfer_button)

    def is_transfer_successful(self):
        if self.is_displayed(self.transfer_complete_header):
            return True

        result = self.get_transfer_result().lower()
        return (
            "complete" in result
            or "successful" in result
            or "successfully" in result
        )

    def get_transfer_result(self):
        return self.get_element_text_safe(self.transfer_result_message)
