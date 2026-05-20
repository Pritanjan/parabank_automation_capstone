from pytest_bdd import scenarios, when, then, given
from pages.update_contact_page import UpdateContactPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

scenarios("../features/update_contact_information.feature")



@given("user launches the ParaBank application")
def launch_application(driver):

    driver.get(
        "https://parabank.parasoft.com/parabank/index.htm"
    )


@given('user logs in with username "john" and password "demo"')
def login(driver):

    wait = WebDriverWait(driver, 10)

    username = wait.until(
        EC.presence_of_element_located(
            (By.NAME, "username")
        )
    )

    password = driver.find_element(
        By.NAME,
        "password"
    )

    username.clear()
    username.send_keys("john")

    password.clear()
    password.send_keys("demo")

    driver.find_element(
        By.XPATH,
        "//input[@value='Log In']"
    ).click()


@then("user should be navigated to Accounts Overview page")
def verify_login(driver):

    WebDriverWait(driver, 10).until(
        EC.url_contains("overview")
    )

    assert "overview" in driver.current_url.lower()

@when("user navigates to Update Contact Info page")
def navigate_update_contact(driver):
    UpdateContactPage(driver).navigate_to_update_contact_page()


@when('user updates first name as "John"')
def update_first_name(driver):
    UpdateContactPage(driver).enter_first_name("John")


@when('user updates last name as "Doe"')
def update_last_name(driver):
    UpdateContactPage(driver).enter_last_name("Doe")


@when('user updates address as "New Street 101"')
def update_address(driver):
    UpdateContactPage(driver).enter_address("New Street 101")


@when('user updates city as "Lucknow"')
def update_city(driver):
    UpdateContactPage(driver).enter_city("Lucknow")


@when('user updates state as "Uttar Pradesh"')
def update_state(driver):
    UpdateContactPage(driver).enter_state("Uttar Pradesh")


@when('user updates zip code as "226001"')
def update_zip(driver):
    UpdateContactPage(driver).enter_zip_code("226001")


@when('user updates phone number as "9876543210"')
def update_phone(driver):
    UpdateContactPage(driver).enter_phone("9876543210")


@when("user clicks on update profile button")
def click_update(driver):
    UpdateContactPage(driver).click_update_profile()


@then("contact information should be updated successfully")
def validate_profile_update(driver):
    assert UpdateContactPage(driver).is_profile_updated()
