from pytest_bdd import scenarios, given, when, then, parsers

from pages.forget_login_info import ForgotLoginInfoPage

scenarios("../features/forget_logon_info.feature")


@given("user launches the Parabank application")
def launch_application(browser):

    page = ForgotLoginInfoPage(browser)

    page.open_application()


@given("user is on the Forgot Login Information page")
def open_forgot_login_info_page(browser):

    page = ForgotLoginInfoPage(browser)

    page.open_application()
    page.click_forgot_login_info_link()

    assert page.is_forgot_login_page_displayed()


@when(parsers.parse('user clicks on "{link_text}" link'))
def click_forgot_login_info(browser, link_text):

    page = ForgotLoginInfoPage(browser)

    assert link_text.lower() == "forgot login info?"
    page.click_forgot_login_info_link()


@when(parsers.parse('user enters first name "{first_name}"'))
def enter_first_name(browser, first_name):

    page = ForgotLoginInfoPage(browser)
    page.enter_first_name(first_name)


@when(parsers.parse('user enters last name "{last_name}"'))
def enter_last_name(browser, last_name):

    page = ForgotLoginInfoPage(browser)
    page.enter_last_name(last_name)


@when(parsers.parse('user enters address "{address}"'))
def enter_address(browser, address):

    page = ForgotLoginInfoPage(browser)
    page.enter_address(address)


@when(parsers.parse('user enters city "{city}"'))
def enter_city(browser, city):

    page = ForgotLoginInfoPage(browser)
    page.enter_city(city)


@when(parsers.parse('user enters state "{state}"'))
def enter_state(browser, state):

    page = ForgotLoginInfoPage(browser)
    page.enter_state(state)


@when(parsers.parse('user enters zip code "{zip_code}"'))
def enter_zip_code(browser, zip_code):

    page = ForgotLoginInfoPage(browser)
    page.enter_zip_code(zip_code)


@when(parsers.parse('user enters ssn "{ssn}"'))
def enter_ssn(browser, ssn):

    page = ForgotLoginInfoPage(browser)
    page.enter_ssn(ssn)


@when("user leaves required fields blank")
def leave_required_fields_blank(browser):

    page = ForgotLoginInfoPage(browser)
    page.open_application()
    page.click_forgot_login_info_link()


@when("user enters invalid account details")
def enter_invalid_account_details(browser):

    page = ForgotLoginInfoPage(browser)
    page.open_application()
    page.click_forgot_login_info_link()
    page.enter_first_name("Invalid")
    page.enter_last_name("User")
    page.enter_address("Unknown")
    page.enter_city("Nowhere")
    page.enter_state("XX")
    page.enter_zip_code("00000")
    page.enter_ssn("000000000")


@when("user clicks on Find My Login Info button")
def click_find_login_info(browser):

    page = ForgotLoginInfoPage(browser)
    page.click_find_login_info_button()


@then("user should see the Forgot Login Information page")
def verify_forgot_login_page(browser):

    page = ForgotLoginInfoPage(browser)
    assert page.is_forgot_login_page_displayed()


@then("user should receive login information reset instructions")
def verify_login_info_reset_instructions(browser):

    page = ForgotLoginInfoPage(browser)
    message = page.get_success_message().lower()

    assert (
        "login info has been sent" in message
        or "login information has been sent" in message
        or "successfully sent" in message
    ), f"Expected success instruction message, got '{message}'"


@then("user should see a validation error message")
def verify_validation_error(browser):

    page = ForgotLoginInfoPage(browser)
    error = page.get_error_message().lower()

    assert (
        "error" in error
        or "required" in error
        or "invalid" in error
    ), f"Expected validation error message, got '{error}'"


@then("user should see an invalid information error message")
def verify_invalid_information_error(browser):

    page = ForgotLoginInfoPage(browser)
    error = page.get_error_message().lower()

    assert (
        "could not" in error
        or "invalid" in error
        or "error" in error
    ), f"Expected invalid information error, got '{error}'"
