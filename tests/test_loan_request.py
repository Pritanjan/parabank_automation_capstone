"""
test_loan_request.py - Loan rejection BDD steps.
Parabank Automation Capstone - Loan Application Processing
"""

from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.loan_request import LoanRequestPage


scenarios("../features/loan_rejection.feature")


@given(parsers.parse('I am logged in as "{username}" with password "{password}"'))
def login(browser, username, password):
    browser.login = LoginPage(browser)
    browser.login.open_application()
    browser.login.login(username, password)
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Request Loan"))
    )


@given("I navigate to the Request Loan page")
def navigate_to_loan_page(browser):
    browser.loan = LoanRequestPage(browser)
    request_loan_link = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Request Loan"))
    )
    request_loan_link.click()
    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.ID, "amount"))
    )


@when(parsers.parse('I enter loan amount "{amount}" and down payment "{down_payment}"'))
def enter_loan_amount_and_down_payment(browser, amount, down_payment):
    browser.loan.enter_loan_amount(amount)
    browser.loan.enter_down_payment(down_payment)


@when("I submit the loan application")
def submit_loan_application(browser):
    browser.loan.click_apply_now()


@then(parsers.parse('the loan status should be "{expected_status}"'))
def verify_loan_status(browser, expected_status):
    status_locator = (
        By.XPATH,
        f"//*[contains(text(), '{expected_status}') or contains(text(), '{expected_status.lower()}') ]"
    )
    status_text = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(status_locator)
    ).text
    assert expected_status.lower() in status_text.lower(), \
        f"Expected loan status '{expected_status}', but got: '{status_text}'"
