from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from pages.accounts_overview_page import AccountsOverviewPage
from pages.transfer_funds_page import TransferFundsPage


scenarios("../features/account_balance.feature")


@given("user launches the ParaBank application")
def launch_application(driver):
    driver.get("https://parabank.parasoft.com/parabank")


@given(parsers.parse(
    'user logs in with username "{username}" and password "{password}"'
))
def login(driver, username, password):
    LoginPage(driver).login(username, password)


@then("user should be navigated to Accounts Overview page")
def verify_accounts_page(driver):
    assert AccountsOverviewPage(
        driver
    ).is_accounts_overview_displayed()


@then("user captures the initial balance of source account")
def capture_initial_source_balance(driver):
    global initial_source_balance
    initial_source_balance = (
        AccountsOverviewPage(driver).get_source_balance()
    )


@then("user captures the initial balance of destination account")
def capture_initial_destination_balance(driver):
    global initial_destination_balance
    initial_destination_balance = (
        AccountsOverviewPage(driver).get_destination_balance()
    )


@when("user navigates to Transfer Funds page")
def navigate_transfer_page(driver):
    TransferFundsPage(driver).navigate_to_transfer_funds()


@when(parsers.parse(
    'user transfers amount "{amount}" from source account to destination account'
))
def transfer_amount(driver, amount):
    TransferFundsPage(driver).transfer_funds(amount)


@then("transfer should be completed successfully")
def verify_transfer(driver):
    assert TransferFundsPage(
        driver
    ).is_transfer_successful()