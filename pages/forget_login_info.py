from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ForgotLoginInfoPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.url = "https://parabank.parasoft.com/parabank/index.htm"

        self.forgot_login_info_link = (
            By.LINK_TEXT,
            "Forgot login info?"
        )

        self.first_name = (By.ID, "firstName")
        self.last_name = (By.ID, "lastName")
        self.address = (By.ID, "address.street")
        self.city = (By.ID, "address.city")
        self.state = (By.ID, "address.state")
        self.zip_code = (By.ID, "address.zipCode")
        self.ssn = (By.ID, "ssn")

        self.find_login_info_button = (
            By.XPATH,
            "//input[@value='Find My Login Info']"
        )

        self.page_header = (
            By.XPATH,
            "//h1[contains(text(),'Forgot login info') or contains(text(),'Customer Lookup') or contains(text(),'Forgot Login')]"
        )

        self.success_message = (
            By.XPATH,
            "//p[contains(text(),'Your login info has been sent') or contains(text(),'login information has been sent') or contains(text(),'successfully sent')]"
        )

        self.field_error_message = (
            By.XPATH,
            "//span[contains(@class,'error') and contains(@id,'errors')]"
        )

        self.page_error_message = (
            By.XPATH,
            "//p[@class='error' or contains(text(),'could not be found') or contains(text(),'error')]"
        )

    def open_application(self):
        self.open_url(self.url)

    def navigate_to_forgot_login_info(self):
        self.open_application()
        self.click_element(self.forgot_login_info_link)

    def click_forgot_login_info_link(self):
        self.click_element(self.forgot_login_info_link)

    def enter_first_name(self, first_name):
        self.enter_text(self.first_name, first_name)

    def enter_last_name(self, last_name):
        self.enter_text(self.last_name, last_name)

    def enter_address(self, address):
        self.enter_text(self.address, address)

    def enter_city(self, city):
        self.enter_text(self.city, city)

    def enter_state(self, state):
        self.enter_text(self.state, state)

    def enter_zip_code(self, zip_code):
        self.enter_text(self.zip_code, zip_code)

    def enter_ssn(self, ssn):
        self.enter_text(self.ssn, ssn)

    def click_find_login_info_button(self):
        self.click_element(self.find_login_info_button)

    def is_forgot_login_page_displayed(self):
        return self.is_displayed(self.page_header)

    def get_success_message(self):
        return self.get_element_text_safe(self.success_message)

    def get_error_message(self):
        error_text = self.get_element_text_safe(self.page_error_message)

        if error_text:
            return error_text

        return self.get_element_text_safe(self.field_error_message)


if __name__ == "__main__":
    print("Forgot Login Info Page executed successfully")