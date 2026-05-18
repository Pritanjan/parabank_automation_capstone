from pytest_bdd import scenarios, given, when, then

from pages.login_page import LoginPage
from pages.logout_page import LogoutPage

scenarios("../features/logout.feature")


VALID_USERNAME = "priyanshu14"
VALID_PASSWORD = "demo"


@given("user launches the Parabank application")
def launch_application(browser):

    page = LoginPage(browser)

    page.open_application()

@given("user logs in with valid credentials")
def login_user(browser):

    page = LoginPage(browser)

    page.open_application()

    page.login(
        VALID_USERNAME,
        VALID_PASSWORD
    )

    page.wait.until(
        lambda driver: "overview" in driver.current_url.lower()
    )


@when("user clicks on logout link")
def logout(browser):

    page = LogoutPage(browser)

    page.click_logout()


@then("user should be redirected to login page")
def verify_logout(browser):

    page = LogoutPage(browser)

    assert page.is_login_page_displayed()


@when("user clicks browser back button")
def browser_back(browser):

    browser.back()


@then("user should not access account overview page")
def verify_session_ended(browser):

    assert "overview" not in \
           browser.current_url.lower()


@then("login form should be displayed")
def verify_login_form(browser):

    page = LogoutPage(browser)

    assert page.is_login_page_displayed()


@when("user tries to access application URL again")
def access_application_again(browser):

    browser.get(
        "http://parabank.parasoft.com/parabank/index.htm"
    )


@then("user should be asked to login again")
def verify_login_required(browser):

    page = LogoutPage(browser)

    assert page.is_login_page_displayed()