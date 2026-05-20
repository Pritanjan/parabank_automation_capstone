from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.transaction_history_page import TransactionHistoryPage
from pages.bill_payment_page import BillPaymentPage
import time

scenarios("../features/transaction_history.feature")


# ── Background Steps ──────────────────────────────────────────────────────────

@given("user launches the ParaBank application")
def launch_app(browser):
    pass


@given('user logs in with username "priyanshu14" and password "priyanshu123"')
def login_user(browser):
    browser.find_element(By.NAME, "username").send_keys("priyanshu14")
    browser.find_element(By.NAME, "password").send_keys("priyanshu123")
    browser.find_element(By.XPATH, "//input[@value='Log In']").click()
    time.sleep(2)

# ── Accounts Overview Scenarios ───────────────────────────────────────────────

@given("user navigates to Accounts Overview page")
def navigate_accounts_overview(browser):
    txn_page = TransactionHistoryPage(browser)
    txn_page.click_accounts_overview()


@when("user selects an account number")
def select_account_number(browser):
    txn_page = TransactionHistoryPage(browser)
    txn_page.select_first_account()


@then("transaction history page should be displayed")
def verify_txn_page(browser):
    txn_page = TransactionHistoryPage(browser)
    assert txn_page.is_transaction_table_displayed(), \
        "Transaction table not visible!"


@then("transaction date, description, debit and credit details should be displayed")
def verify_txn_details(browser):
    txn_page = TransactionHistoryPage(browser)
    assert txn_page.are_transaction_details_visible(), \
        "Transaction columns missing!"


# ── Bill Payment in History Scenario ─────────────────────────────────────────

@given('user completes a bill payment of amount "100"')
def complete_bill_payment(browser):
    bill_page = BillPaymentPage(browser)
    bill_page.click_bill_pay()
    bill_page.enter_payee_details()
    bill_page.enter_payment_amount("100")
    bill_page.select_from_account()
    bill_page.click_send_payment()
    assert bill_page.is_payment_successful(), \
        "Bill payment failed during setup!"


@when("user navigates to transaction history for the payment account")
def go_to_txn_history(browser):
    txn_page = TransactionHistoryPage(browser)
    txn_page.click_accounts_overview()
    txn_page.select_first_account()


@then("bill payment transaction should be displayed in transaction history")
def verify_bill_in_history(browser):
    txn_page = TransactionHistoryPage(browser)
    assert txn_page.get_transaction_count() > 0, \
        "No transactions found!"


# ── Helper Function ───────────────────────────────────────────────────────────

def login_and_go_to_find_transactions(browser):
    browser.get("http://parabank.parasoft.com/parabank/index.htm")
    time.sleep(1)
    if "Log Out" not in browser.page_source:
        browser.find_element(By.NAME, "username").send_keys("priyanshu14")  # changed
        browser.find_element(By.NAME, "password").send_keys("priyanshu123")  # changed
        browser.find_element(By.XPATH, "//input[@value='Log In']").click()
        time.sleep(2)
    browser.find_element(By.LINK_TEXT, "Find Transactions").click()
    time.sleep(2)


# ── Find Transactions Navigate ────────────────────────────────────────────────

@given("user navigates to Find Transactions page")
def navigate_find_transactions(browser):
    login_and_go_to_find_transactions(browser)


# ── Find by Amount ────────────────────────────────────────────────────────────

@when('user enters amount "100" to search')
def enter_amount(browser):
    field = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "amount"))
    )
    field.clear()
    field.send_keys("100")


@when("user clicks Find Transactions by amount button")
def click_find_by_amount(browser):
    browser.find_element(By.ID, "findByAmount").click()
    time.sleep(2)


# ── Find by Date ──────────────────────────────────────────────────────────────

@when(parsers.parse('user enters date "{date}" to search'))
def enter_date(browser, date):
    login_and_go_to_find_transactions(browser)
    field = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "transactionDate"))
    )
    field.clear()
    field.send_keys(date)


@when("user clicks Find Transactions by date button")
def click_find_by_date(browser):
    browser.find_element(By.ID, "findByDate").click()
    time.sleep(2)


# ── Find by Date Range ────────────────────────────────────────────────────────

@when(parsers.parse('user enters from date "{from_date}" and to date "{to_date}"'))
def enter_date_range(browser, from_date, to_date):
    login_and_go_to_find_transactions(browser)
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "fromDate"))
    )
    browser.find_element(By.ID, "fromDate").clear()
    browser.find_element(By.ID, "fromDate").send_keys(from_date)
    browser.find_element(By.ID, "toDate").clear()
    browser.find_element(By.ID, "toDate").send_keys(to_date)


@when("user clicks Find Transactions by date range button")
def click_find_by_date_range(browser):
    browser.find_element(By.ID, "findByDateRange").click()
    time.sleep(2)


# ── Find by Transaction ID ────────────────────────────────────────────────────

@when(parsers.parse('user enters transaction ID "{txn_id}" to search'))
def enter_txn_id(browser, txn_id):
    login_and_go_to_find_transactions(browser)
    field = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "transactionId"))
    )
    field.clear()
    field.send_keys(txn_id)


@when("user clicks Find Transactions by ID button")
def click_find_by_id(browser):
    browser.find_element(By.ID, "findById").click()
    time.sleep(2)


# ── Then Steps ────────────────────────────────────────────────────────────────

@then("transaction results should be displayed")
def verify_results(browser):
    WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.ID, "transactionTable"))
    )
    assert browser.find_element(
        By.ID, "transactionTable"
    ).is_displayed(), "Transaction results table not shown!"


@then("transaction details page should be displayed")
def verify_txn_detail_page(browser):
    WebDriverWait(browser, 15).until(
        EC.presence_of_element_located(
            (By.XPATH, "//h1[contains(text(),'Transaction Details')]")
        )
    )
    assert "Transaction Details" in browser.page_source, \
        "Transaction details page not shown!"