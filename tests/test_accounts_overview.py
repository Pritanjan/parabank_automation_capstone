from pytest_bdd import scenarios, given, when, then
from pages.accounts_overview_page import AccountsOverviewPage

scenarios("../features/accounts_overview.feature")


@given("user logs into parabank application")
def login_application(browser):

    browser.accounts = AccountsOverviewPage(browser)


@when("user navigates to accounts overview page")
def open_accounts_page(browser):

    browser.accounts.open_accounts_overview_page()


@then("account details should display successfully")
def verify_accounts(browser):

    assert browser.accounts.verify_accounts_page()