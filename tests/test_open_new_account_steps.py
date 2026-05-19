from pytest_bdd import (
    scenarios,
    given,
    when,
    then,
    parsers
)

from pages.login_page import (
    LoginPage
)

from pages.open_new_account_page import (
    OpenNewAccountPage
)

scenarios(
    "../features/open_new_account.feature"
)


VALID_USERNAME = "priyanshu14"
VALID_PASSWORD = "priyanshu123"


@given(
    "user logs in with valid credentials"
)
def login_user(browser):

    login_page = LoginPage(browser)

    login_page.open_application()

    login_page.login(
        VALID_USERNAME,
        VALID_PASSWORD
    )

    assert (
        login_page.is_logout_displayed()
    )


@when(
    "user navigates to open new account page"
)
def navigate_open_account(browser):

    page = OpenNewAccountPage(browser)

    page.click_open_new_account()


@when(
    parsers.parse(
        'user selects "{account_type}" account type'
    )
)
def select_account_type(
    browser,
    account_type
):

    page = OpenNewAccountPage(browser)

    page.select_account_type(
        account_type
    )

    page.select_from_account()


@when(
    "user submits new account request"
)
def submit_new_account(browser):

    page = OpenNewAccountPage(browser)

    page.click_open_account_button()


@then(
    "new account should be created successfully"
)
def verify_account_created(browser):

    page = OpenNewAccountPage(browser)

    success_message = (
        page.get_success_message()
    )

    print(
        "Success Message:",
        success_message
    )

    assert (
        "Congratulations" in success_message
        or
        "Account Opened" in success_message
    )