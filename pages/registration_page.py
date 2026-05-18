from selenium.webdriver.common.by import By
import random

class RegistrationPage:

    def __init__(self, driver):

        self.driver = driver

        self.register_link = (
            By.LINK_TEXT,
            "Register"
        )

        self.first_name = (
            By.ID,
            "customer.firstName"
        )

        self.last_name = (
            By.ID,
            "customer.lastName"
        )

        self.address = (
            By.ID,
            "customer.address.street"
        )

        self.city = (
            By.ID,
            "customer.address.city"
        )

        self.state = (
            By.ID,
            "customer.address.state"
        )

        self.zip_code = (
            By.ID,
            "customer.address.zipCode"
        )

        self.phone = (
            By.ID,
            "customer.phoneNumber"
        )

        self.ssn = (
            By.ID,
            "customer.ssn"
        )

        self.username = (
            By.ID,
            "customer.username"
        )

        self.password = (
            By.ID,
            "customer.password"
        )

        self.confirm_password = (
            By.ID,
            "repeatedPassword"
        )

        self.register_button = (
            By.XPATH,
            "//input[@value='Register']"
        )

    def click_register_link(self):

        self.driver.find_element(
            *self.register_link
        ).click()

    def enter_registration_details(self):

        random_number = random.randint(1000,9999)

        username = "user" + str(random_number)

        self.driver.find_element(
            *self.first_name
        ).send_keys("Lavanya")

        self.driver.find_element(
            *self.last_name
        ).send_keys("Test")

        self.driver.find_element(
            *self.address
        ).send_keys("Hyderabad")

        self.driver.find_element(
            *self.city
        ).send_keys("Hyderabad")

        self.driver.find_element(
            *self.state
        ).send_keys("Telangana")

        self.driver.find_element(
            *self.zip_code
        ).send_keys("500001")

        self.driver.find_element(
            *self.phone
        ).send_keys("9876543210")

        self.driver.find_element(
            *self.ssn
        ).send_keys("123456789")

        self.driver.find_element(
            *self.username
        ).send_keys(username)

        self.driver.find_element(
            *self.password
        ).send_keys("admin123")

        self.driver.find_element(
            *self.confirm_password
        ).send_keys("admin123")

    def click_register_button(self):

        self.driver.find_element(
            *self.register_button
        ).click()