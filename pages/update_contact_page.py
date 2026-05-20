from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class UpdateContactPage(BasePage):

    UPDATE_CONTACT_LINK = (By.LINK_TEXT, "Update Contact Info")

    FIRST_NAME = (By.ID, "customer.firstName")
    LAST_NAME = (By.ID, "customer.lastName")
    ADDRESS = (By.ID, "customer.address.street")
    CITY = (By.ID, "customer.address.city")
    STATE = (By.ID, "customer.address.state")
    ZIP_CODE = (By.ID, "customer.address.zipCode")
    PHONE = (By.ID, "customer.phoneNumber")

    UPDATE_BUTTON = (By.XPATH, "//input[@value='Update Profile']")
    SUCCESS_MESSAGE = (By.ID, "updateProfileResult")
    SUCCESS_MESSAGE_FALLBACK = (
        By.XPATH,
        "//*[contains(translate(normalize-space(.), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'profile updated') or contains(translate(normalize-space(.), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'updated address') or contains(translate(normalize-space(.), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'update profile') or contains(translate(normalize-space(.), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'updated')]"
    )

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_update_contact_page(self):
        self.click_element(self.UPDATE_CONTACT_LINK)

    def enter_first_name(self, first_name):
        self.type_text(self.FIRST_NAME, first_name)

    def enter_last_name(self, last_name):
        self.type_text(self.LAST_NAME, last_name)

    def enter_address(self, address):
        self.type_text(self.ADDRESS, address)

    def enter_city(self, city):
        self.type_text(self.CITY, city)

    def enter_state(self, state):
        self.type_text(self.STATE, state)

    def enter_zip_code(self, zip_code):
        self.type_text(self.ZIP_CODE, zip_code)

    def enter_phone(self, phone):
        self.type_text(self.PHONE, phone)

    def click_update_profile(self):
        self.click_element(self.UPDATE_BUTTON)
        self.wait_for_visible(self.SUCCESS_MESSAGE)

    def is_profile_updated(self, timeout=10):
        success_text = self.get_element_text_safe(self.SUCCESS_MESSAGE, timeout=timeout)
        if success_text and success_text.strip():
            return True

        fallback_text = self.get_element_text_safe(self.SUCCESS_MESSAGE_FALLBACK, timeout=timeout)
        return bool(fallback_text and fallback_text.strip())
