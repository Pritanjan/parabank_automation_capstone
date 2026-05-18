from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.url = "http://parabank.parasoft.com/parabank/index.htm"

        self.logout_link = (By.LINK_TEXT, "Log Out")
        self.login_button = (By.XPATH, "//input[@value='Log In']")

    def open_application(self):
        self.driver.get(self.url)

    def click_logout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.logout_link)
        ).click()

    def is_login_page_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.login_button)
        ).is_displayed()

    def get_current_url(self):
        return self.driver.current_url


if __name__ == "__main__":
    print("Logout Page executed successfully")