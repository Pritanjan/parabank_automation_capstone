from behave import *
from pages.login_page import LoginPage
from pages.accounts_overview_page import AccountsOverviewPage

@given('user logs into parabank application')
def step_impl(context):

    login = LoginPage(context.driver)

    login.login_to_application(
        "john",
        "demo"
    )

@when('user navigates to accounts overview page')
def step_impl(context):

    context.accounts = AccountsOverviewPage(
        context.driver
    )

    context.accounts.open_accounts_overview_page()

@then('account details should display successfully')
def step_impl(context):

    assert context.accounts.verify_accounts_overview_displayed()