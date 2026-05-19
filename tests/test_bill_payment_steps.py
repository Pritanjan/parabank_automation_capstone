from pytest_bdd import scenarios, given, when, then
from pages.bill_payment_page import BillPaymentPage

scenarios("../features/bill_payment.feature")


# ── Background Steps ──────────────────────────────────────────────────────────

@given("user launches the ParaBank application")
def launch_application(browser):
    pass  # browser fixture already opens BASE_URL


@given('user logs in with username "john" and password "demo"')
def login_user(browser):
    browser.find_element("name", "username").send_keys("john")
    browser.find_element("name", "password").send_keys("demo")
    browser.find_element("xpath", "//input[@value='Log In']").click()


# ── Scenario Steps ────────────────────────────────────────────────────────────

@given("user navigates to Bill Pay page")
def navigate_to_bill_pay(browser):
    bill_page = BillPaymentPage(browser)
    bill_page.click_bill_pay()


@when("user enters valid payee information")
def enter_payee_information(browser):
    bill_page = BillPaymentPage(browser)
    bill_page.enter_payee_details()


@when('user enters payment amount "100"')
def enter_payment_amount_100(browser):
    bill_page = BillPaymentPage(browser)
    bill_page.enter_payment_amount("100")


@when('user enters payment amount "50"')
def enter_payment_amount_50(browser):
    bill_page = BillPaymentPage(browser)
    bill_page.enter_payment_amount("50")


@when("user selects account for bill payment")
def select_account(browser):
    bill_page = BillPaymentPage(browser)
    bill_page.select_from_account()


@when("user clicks on Send Payment button")
def click_send_payment(browser):
    bill_page = BillPaymentPage(browser)
    bill_page.click_send_payment()


@then("bill payment should be completed successfully")
def verify_payment_success(browser):
    bill_page = BillPaymentPage(browser)
    assert bill_page.is_payment_successful(), \
        "Bill payment success message not found!"


@then("user should see bill payment confirmation message")
def verify_confirmation_message(browser):
    bill_page = BillPaymentPage(browser)
    msg = bill_page.get_success_message()
    assert "Bill Payment Complete" in msg, \
        f"Expected confirmation but got: '{msg}'"


@when("user leaves payee information blank")
def leave_payee_blank(browser):
    pass  # intentionally empty


@then("appropriate bill payment validation message should be displayed")
def verify_validation_message(browser):
    bill_page = BillPaymentPage(browser)
    error = bill_page.get_validation_error()
    assert error != "", \
        "Expected validation error but none displayed!"