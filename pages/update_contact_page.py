from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UpdateContactPage:

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
    SUCCESS_MESSAGE_FALLBACK = (By.XPATH, "//*[contains(text(),'updated')]")

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_update_contact_page(self):
        self.driver.find_element(*self.UPDATE_CONTACT_LINK).click()

    def enter_first_name(self, first_name):
        field = self.driver.find_element(*self.FIRST_NAME)
        field.clear()
        field.send_keys(first_name)

    def enter_last_name(self, last_name):
        field = self.driver.find_element(*self.LAST_NAME)
        field.clear()
        field.send_keys(last_name)

    def enter_address(self, address):
        field = self.driver.find_element(*self.ADDRESS)
        field.clear()
        field.send_keys(address)

    def enter_city(self, city):
        field = self.driver.find_element(*self.CITY)
        field.clear()
        field.send_keys(city)

    def enter_state(self, state):
        field = self.driver.find_element(*self.STATE)
        field.clear()
        field.send_keys(state)

    def enter_zip_code(self, zip_code):
        field = self.driver.find_element(*self.ZIP_CODE)
        field.clear()
        field.send_keys(zip_code)

    def enter_phone(self, phone):
        field = self.driver.find_element(*self.PHONE)
        field.clear()
        field.send_keys(phone)

    def click_update_profile(self):
        self.driver.find_element(*self.UPDATE_BUTTON).click()
        # small implicit wait to let the update complete and message appear
        self.driver.implicitly_wait(1)

    #def is_profile_updated(self):
        #return self.driver.find_element(*self.SUCCESS_MESSAGE).is_displayed()
    
    def is_profile_updated(self, timeout=10):
        # try primary locator first, then fallback XPath containing 'updated'
        try:
            el = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
            )
            text = el.text or ""
            if len(text.strip()) > 0:
                return True
            # if element is visible but contains no text, treat as success
            if el.is_displayed():
                return True
        except Exception:
            pass

        try:
            el = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.SUCCESS_MESSAGE_FALLBACK)
            )
            text = el.text or ""
            if len(text.strip()) > 0:
                return True
            if el.is_displayed():
                return True
            return False
        except Exception:
            return False