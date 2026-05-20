"""
pages/transfer_funds_page.py
Page Object Model for Parabank Fund Transfer Page
URL: http://parabank.parasoft.com/parabank/transfer.htm
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class TransferFundsPage(BasePage):

    # ── Locators ─────────────────────────────────────────────────────────────

    TRANSFER_LINK    = (By.LINK_TEXT,    "Transfer Funds")
    AMOUNT_INPUT     = (By.ID,           "amount")
    FROM_ACCOUNT     = (By.ID,           "fromAccountId")
    TO_ACCOUNT       = (By.ID,           "toAccountId")
    TRANSFER_BUTTON  = (By.CSS_SELECTOR, "input[value='Transfer']")

    # Result
    RESULT_HEADER    = (By.CSS_SELECTOR, "#showResult h1")
    TRANSFER_AMOUNT  = (By.ID,           "amount")
    FROM_ACCOUNT_ID  = (By.ID,           "fromAccountId")
    TO_ACCOUNT_ID    = (By.ID,           "toAccountId")
    ERROR_MSG        = (By.CSS_SELECTOR, ".error")

    # ── Actions ───────────────────────────────────────────────────────────────

    # SAHI — tuple as-is pass karo
    def navigate_to_transfer(self):
        self.click(self.TRANSFER_LINK)

    def navigate_to_transfer_funds(self):
        self.navigate_to_transfer()

    def enter_amount(self, amount: str):
        self.type_text(self.AMOUNT_INPUT, amount)

    def select_from_account(self, index: int = 0):
        self.select_dropdown_by_index(self.FROM_ACCOUNT, index)

    def select_to_account(self, index: int = 1):
        try:
            self.select_dropdown_by_index(self.TO_ACCOUNT, index)
        except Exception:
            self.select_dropdown_by_index(self.TO_ACCOUNT, 0)

    def click_transfer(self):
        self.click(self.TRANSFER_BUTTON)

    def transfer_funds(self, amount: str, from_index: int = 0, to_index: int = 1):
        """Full fund transfer flow."""
        self.enter_amount(amount)
        self.select_from_account(from_index)
        self.select_to_account(to_index)
        self.click_transfer()

    # ── Assertions / Getters ─────────────────────────────────────────────────

    def get_transfer_result(self) -> str:
        try:
            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(self.RESULT_HEADER)
            )
            return self.driver.find_element(*self.RESULT_HEADER).text.strip()
        except Exception:
            return ""

    def is_transfer_successful(self) -> bool:
        result = self.get_transfer_result()
        return "Transfer Complete" in result or "Complete" in result

    def get_error_message(self) -> str:
        return self.get_element_text_safe(self.ERROR_MSG)