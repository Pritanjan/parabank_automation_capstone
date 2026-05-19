from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    URL = "https://parabank.parasoft.com/parabank/index.htm"

    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Log In']")
    ERROR_MESSAGE = (By.CLASS_NAME, "error")

    def open_application(self):
        self.open_url(self.URL)

    def login(self, username, password):

        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)

        self.click_element(self.LOGIN_BUTTON)