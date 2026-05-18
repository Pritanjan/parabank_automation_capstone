from pytest_bdd import scenarios, when, then
from pages.find_transactions_page import FindTransactionsPage

scenarios("../features/find_transactions.feature")


@when("user navigates to Find Transactions page")
def navigate_find_transactions(driver):
    FindTransactionsPage(driver).navigate_to_find_transactions()


@when('user searches transaction by date "05-18-2026"')
def search_transaction_date(driver):
    FindTransactionsPage(driver).search_by_date("05-18-2026")


@when('user searches transaction by amount "100"')
def search_transaction_amount(driver):
    FindTransactionsPage(driver).search_by_amount("100")


@when('user searches transaction by id "12345"')
def search_transaction_id(driver):
    FindTransactionsPage(driver).search_by_id("12345")


@when('user searches transaction by id "999999"')
def search_invalid_transaction(driver):
    FindTransactionsPage(driver).search_by_id("999999")


@then("transaction details should be displayed")
def validate_transaction_details(driver):
    assert FindTransactionsPage(driver).is_transaction_displayed()


@then("matching transaction records should be displayed")
def validate_amount_transactions(driver):
    assert FindTransactionsPage(driver).is_transaction_displayed()


@then("corresponding transaction details should be displayed")
def validate_transaction_id(driver):
    assert FindTransactionsPage(driver).is_transaction_displayed()


@then("no transaction result message should be displayed")
def validate_no_transaction(driver):
    assert FindTransactionsPage(driver).is_no_transaction_message_displayed()