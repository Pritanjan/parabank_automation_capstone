from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.url = "https://parabank.parasoft.com/parabank/index.htm"

        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//input[@value='Log In']")
        self.logout_link = (By.LINK_TEXT, "Log Out")
        self.error_message = (By.XPATH, "//p[@class='error']")

    def open_application(self):
        self.open_url(self.url)

    def enter_username(self, username):
        self.enter_text(self.username_input, username)

    def enter_password(self, password):
        self.enter_text(self.password_input, password)

    def click_login(self):
        self.click_element(self.login_button)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def click_logout(self):
        self.click_element(self.logout_link)

    def get_error_message(self):
        return self.get_text(self.error_message)

    def get_current_url(self):
        return self.driver.current_url