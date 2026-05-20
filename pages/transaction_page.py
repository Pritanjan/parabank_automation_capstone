# from selenium.webdriver.common.by import By
# from pages.base_page import BasePage
#
#
# class TransactionPage(BasePage):
#
#     def __init__(self, driver):
#         super().__init__(driver)
#
#         self.accounts_overview_link = (
#             By.LINK_TEXT,
#             "Accounts Overview"
#         )
#
#         self.account_table = (
#             By.ID,
#             "accountTable"
#         )
#
#     def navigate_to_accounts_overview(self):
#         self.click(self.accounts_overview_link)
#
#     def is_account_table_visible(self):
#         return self.is_displayed(self.account_table)
# #