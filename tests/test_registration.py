from pytest_bdd import scenarios, given, when, then
from pages.registration_page import RegistrationPage

scenarios("../features/registration.feature")


@given("user launches parabank application")
def launch_application(browser):

    browser.register = RegistrationPage(browser)

    browser.register.open_application()


@when("user clicks on register link")
def click_register(browser):

    browser.register.click_register_link()


@when("user enters registration details")
def enter_details(browser):

    browser.register.enter_registration_details()


@when("user clicks register button")
def click_register_button(browser):

    browser.register.click_register_button()


@then("user account should be created successfully")
def verify_registration(browser):

    message = browser.register.get_success_message()

    assert "welcome" in message.lower()