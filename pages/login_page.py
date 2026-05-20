from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 10)

        self.url = (
            "http://parabank.parasoft.com/"
            "parabank/index.htm"
        )

        self.username_input = (
            By.NAME,
            "username"
        )

        self.password_input = (
            By.NAME,
            "password"
        )

        self.login_button = (
            By.XPATH,
            "//input[@value='Log In']"
        )

        self.logout_link = (
            By.LINK_TEXT,
            "Log Out"
        )

        self.error_message = (
            By.XPATH,
            "//p[@class='error']"
        )

    def open_application(self):

        self.driver.get(self.url)

    def enter_username(self, username):

        self.wait.until(
            EC.visibility_of_element_located(
                self.username_input
            )
        ).clear()

        self.driver.find_element(
            *self.username_input
        ).send_keys(username)

    def enter_password(self, password):

        self.driver.find_element(
            *self.password_input
        ).clear()

        self.driver.find_element(
            *self.password_input
        ).send_keys(password)

    def click_login(self):

        self.driver.find_element(
            *self.login_button
        ).click()

    def login(self, username, password):

        self.enter_username(username)

        self.enter_password(password)

        self.click_login()

    def is_logout_displayed(self):

        return self.wait.until(
            EC.presence_of_element_located(
                self.logout_link
            )
        ).is_displayed()

    def click_logout(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.logout_link
            )
        ).click()

    def get_error_message(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.error_message
            )
        ).text

    def get_current_url(self):

        return self.driver.current_url


if __name__ == "__main__":

    print(
        "Login Page executed successfully"
    )
