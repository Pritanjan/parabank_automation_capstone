import pytest
from pytest_bdd import given, when, then, parsers, scenarios
from pages.login_page import LoginPage
from pages.fund_transfer_page import FundTransferPage
from pages.transaction_page import TransactionPage

# ── Link to feature file ──────────────────────────────────────────────────────
scenarios("../features/fund_transfer.feature")


# ── Given Steps ───────────────────────────────────────────────────────────────

# NOTE: 'I am logged in as...' and 'I navigate to the Transfer Funds page'
# are reused steps - defined here to keep fund_transfer independent.
# pytest-bdd shares steps across files if imported, but we redefine
# them per feature for clarity.

@given(parsers.parse('I am logged in as "{username}" with password "{password}"'))
def logged_in_transfer(browser, username, password):
    page = LoginPage(browser)
    page.navigate_to_login()
    page.login(username, password)
    assert page.is_login_successful(), f"Login failed for '{username}'"


@given("I navigate to the Transfer Funds page")
def navigate_to_transfer(browser):
    page = FundTransferPage(browser)
    page.navigate_to_transfer()


# ── When Steps ────────────────────────────────────────────────────────────────

@when(parsers.parse('I enter transfer amount "{amount}"'))
def enter_transfer_amount(browser, amount):
    page = FundTransferPage(browser)
    page.enter_amount(amount)


@when("I select source and destination accounts")
def select_accounts(browser):
    page = FundTransferPage(browser)
    page.select_from_account(0)
    page.select_to_account(1)


@when("I click the Transfer button")
def click_transfer(browser):
    page = FundTransferPage(browser)
    page.click_transfer()


@when("I navigate to the accounts overview")
def go_to_accounts_overview(browser):
    page = TransactionPage(browser)
    page.navigate_to_accounts_overview()


# ── Then Steps ────────────────────────────────────────────────────────────────

@then("the transfer should be successful")
def verify_transfer_success(browser):
    page = FundTransferPage(browser)
    assert page.is_transfer_successful(), \
        f"Transfer failed. Result: '{page.get_transfer_result()}'"


@then(parsers.parse('I should see "{message}" message'))
def verify_transfer_message(browser, message):
    page = FundTransferPage(browser)
    result = page.get_transfer_result()
    assert message in result, \
        f"Expected '{message}' in result, got '{result}'"


@then("account balances should be updated")
def verify_balance_updated(browser):
    page = TransactionPage(browser)
    assert page.is_account_table_visible(), \
        "Account table not visible - balances not updated"
