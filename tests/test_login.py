from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage

scenarios("../features/login.feature")


@given("user logs in with valid credentials")
def valid_login(browser):

    browser.login = LoginPage(browser)

    browser.login.open_application()

    browser.login.login("john", "demo")


@when("user enters valid username and password")
def enter_valid_credentials(browser):

    browser.login = LoginPage(browser)

    browser.login.open_application()

    browser.login.login("john", "demo")


@when("user enters invalid username and valid password")
def invalid_username(browser):

    browser.login = LoginPage(browser)

    browser.login.open_application()

    browser.login.login("wronguser", "demo")


@when("user enters valid username and invalid password")
def invalid_password(browser):

    browser.login = LoginPage(browser)

    browser.login.open_application()

    browser.login.login("john", "wrongpass")


@when("user leaves username and password blank")
def blank_credentials(browser):

    browser.login = LoginPage(browser)

    browser.login.open_application()

    browser.login.login("", "")


@when(parsers.re(
    r'user enters username "(?P<username>.*)" and password "(?P<password>.*)"'
))
def multiple_login(browser, username, password):

    browser.login = LoginPage(browser)

    browser.login.open_application()

    browser.login.login(username, password)


@when("clicks on login button")
def click_login(browser):
    pass


@when("user clicks on logout button")
def logout(browser):

    browser.login.click_logout()


@then("user should be redirected to account overview page")
def verify_success(browser):

    assert "overview" in browser.login.get_current_url().lower()


@then("user should see login failed error message")
def verify_error(browser):

    error = browser.login.get_error_message()

    assert "could not be verified" in error.lower()


@then("user should see required field validation message")
def verify_blank(browser):

    error = browser.login.get_error_message()

    assert "please enter a username and password" in error.lower()


@then("user should be redirected to login page")
def verify_logout(browser):

    current_url = browser.login.get_current_url().lower()

    assert "index" in current_url or "login" in current_url


@then(parsers.parse('login result should be "{result}"'))
def login_result(browser, result):

    current_url = browser.login.get_current_url().lower()

    if result == "success":

        assert "overview" in current_url

    else:

        assert "login" in current_url or "index" in current_url