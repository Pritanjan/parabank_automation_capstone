from pytest_bdd import scenarios, given, when, then, parsers

from pages.login_page import LoginPage
from pages.logout_page import LogoutPage

scenarios("../features/login.feature")


VALID_USERNAME = "priyanshu14"
VALID_PASSWORD = "demo"


@given("user launches the Parabank application")
def launch_application(browser):

    page = LoginPage(browser)

    page.open_application()


@given("user is on login page")
def verify_login_page(browser):

    assert "parabank" in browser.current_url.lower()


@when("user enters valid username and password")
def enter_valid_credentials(browser):

    page = LoginPage(browser)

    page.login(
        VALID_USERNAME,
        VALID_PASSWORD
    )


@when("user enters invalid username and valid password")
def invalid_username(browser):

    page = LoginPage(browser)

    page.login(
        "invalid_user",
        VALID_PASSWORD
    )


@when("user enters valid username and invalid password")
def invalid_password(browser):

    page = LoginPage(browser)

    page.login(
        VALID_USERNAME,
        "wrongpass"
    )


@when("user leaves username and password blank")
def blank_credentials(browser):

    page = LoginPage(browser)

    page.login("", "")


@then("user should be redirected to account overview page")
def verify_successful_login(browser):

    page = LoginPage(browser)

    assert page.is_logout_displayed()


@then("user should see login failed error message")
def verify_login_failure(browser):

    page = LoginPage(browser)

    assert "could not be verified" in \
           page.get_error_message().lower()


@then("user should see required field validation message")
def verify_blank_login(browser):

    assert "error" in browser.title.lower()


@given("user logs in with valid credentials")
def login_user(browser):

    page = LoginPage(browser)

    page.open_application()

    page.login(
        VALID_USERNAME,
        VALID_PASSWORD
    )

    assert page.is_logout_displayed()


@when("user clicks on logout link")
def logout(browser):

    page = LogoutPage(browser)

    page.click_logout()


@then("user should be redirected to login page")
def verify_logout_redirect(browser):

    page = LogoutPage(browser)

    assert page.is_login_page_displayed()


@when(parsers.parse('user enters username "{username}" and password "{password}"'))
def multiple_login(browser, username, password):

    page = LoginPage(browser)

    page.login(
        username,
        password
    )


@then(parsers.parse('login result should be "{result}"'))
def verify_multiple_login(browser, result):

    page = LoginPage(browser)

    if result == "success":

        assert page.is_logout_displayed()

    else:

        assert "could not be verified" in \
               page.get_error_message().lower()