from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):

    def __init__(self, driver):

        super().__init__(driver)

        self.url = "https://parabank.parasoft.com/parabank/index.htm"

        self.username = (By.NAME, "username")
        self.password = (By.NAME, "password")
        self.login_button = (By.XPATH, "//input[@value='Log In']")

        self.accounts_overview_link = (
            By.LINK_TEXT,
            "Accounts Overview"
        )

    def open_application(self):

        self.open_url(self.url)

    def login(self, username, password):

        self.enter_text(self.username, username)
        self.enter_text(self.password, password)

        self.click_element(self.login_button)

    def dashboard_displayed(self):

        return self.is_displayed(
            self.accounts_overview_link
        )