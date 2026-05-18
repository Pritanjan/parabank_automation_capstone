from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class UpdateContactInfoPage(BasePage):
    # Locators
    address_input = (By.ID, "customer.address.street")
    phone_input = (By.ID, "customer.phoneNumber")
    update_button = (By.XPATH, "//input[@value='Update Profile']")
    confirmation_message = (By.XPATH, "//div[@id='rightPanel']/p")
    # Methods to interact with the page
    def enter_address(self, address):
        self.driver.find_element(*self.address_input).clear()
        self.driver.find_element(*self.address_input).send_keys(address)
    def enter_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_input).clear()
        self.driver.find_element(*self.phone_input).send_keys(phone_number)
    def click_update_profile(self):
        self.driver.find_element(*self.update_button).click()
    def get_confirmation_message(self):
        return self.driver.find_element(*self.confirmation_message).text
    