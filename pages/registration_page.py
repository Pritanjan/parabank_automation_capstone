from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import random


class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.url = "https://parabank.parasoft.com/parabank/index.htm"

        self.register_link = (By.LINK_TEXT, "Register")

        self.first_name = (By.ID, "customer.firstName")
        self.last_name = (By.ID, "customer.lastName")
        self.address = (By.ID, "customer.address.street")
        self.city = (By.ID, "customer.address.city")
        self.state = (By.ID, "customer.address.state")
        self.zip_code = (By.ID, "customer.address.zipCode")
        self.phone = (By.ID, "customer.phoneNumber")
        self.ssn = (By.ID, "customer.ssn")
        self.username = (By.ID, "customer.username")
        self.password = (By.ID, "customer.password")
        self.confirm_password = (By.ID, "repeatedPassword")

        self.register_button = (
            By.XPATH,
            "//input[@value='Register']"
        )

        self.success_message = (
            By.XPATH,
            "//h1[contains(text(),'Welcome')]"
        )

    def open_application(self):
        self.open_url(self.url)

    def click_register_link(self):
        self.click_element(self.register_link)

    def enter_registration_details(self):

        random_num = random.randint(1000, 9999)

        self.enter_text(self.first_name, "best")
        self.enter_text(self.last_name, "team")
        self.enter_text(self.address, "Hyderabad")
        self.enter_text(self.city, "Hyderabad")
        self.enter_text(self.state, "Telangana")
        self.enter_text(self.zip_code, "500001")
        self.enter_text(self.phone, "9876543210")
        self.enter_text(self.ssn, "123456789")

        username = f"bestteam{random_num}"

        self.enter_text(self.username, username)
        self.enter_text(self.password, "test123")
        self.enter_text(self.confirm_password, "test123")

    def click_register_button(self):
        self.click_element(self.register_button)

    def get_success_message(self):
        return self.get_text(self.success_message)