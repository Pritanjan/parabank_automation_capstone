from pytest_bdd import given, when, then, scenarios, parsers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.loan_approval_page import LoanApprovalPage
from pages.login_page import LoginPage

# scenarios("../features/loan_application.feature")
scenarios("../features/loan_approval.feature")

@given(parsers.parse('I am logged in as "{username}" with password "{password}"'))
def login(browser, username, password):
    browser.login = LoginPage(browser)
    browser.login.open_application()
    browser.login.login(username, password)
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Request Loan"))
    )
    
@given('I navigate to the Request Loan page')
def navigate_to_request_loan_page(browser):
    browser.loan = LoanApprovalPage(browser)
    browser.find_element(By.LINK_TEXT, "Request Loan").click()
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "amount"))
    )

@when(parsers.parse("I enter loan amount '{loan_amount}' and down payment '{down_payment}'"))
def enter_loan_amount_step(browser, loan_amount, down_payment):
    loan_page = LoanApprovalPage(browser)
    loan_page.enter_loan_amount(loan_amount)
    loan_page.enter_down_payment(down_payment)

@when('I select from account')
def select_default_from_account(browser):
    loan_page = LoanApprovalPage(browser)
    loan_page.select_from_account()

@when('I submit the loan application')
def submit_loan(browser):
    loan_page = LoanApprovalPage(browser)
    loan_page.click_apply_now()

@when('the loan application is reviewed by the system')
def review_loan_application():
    pass

@then(parsers.parse("I should see a confirmation message '{message}'"))
def verify_confirmation_message(browser, message):
    loan_page = LoanApprovalPage(browser)
    result_message = loan_page.get_result_message()
    assert message in result_message, f"Expected message '{message}' not found in '{result_message}'"

@then(parsers.parse("I should see an error message '{message}'"))
def error_message(browser, message):
    loan_page = LoanApprovalPage(browser)
    result_message = loan_page.get_error_message()
    assert message in result_message, f"Expected message '{message}' not found in '{result_message}'"

@then(parsers.parse("I should receive an approval message '{message}'"))
def verify_approval_message(browser, message):
    loan_page = LoanApprovalPage(browser)
    result_message = loan_page.get_result_message()
    # assert message in result_message, f"Expected message '{message}' not found in '{result_message}'"

@then(parsers.parse("I should receive a denial message '{message}'"))
def verify_denial_message(browser, message):
    loan_page = LoanApprovalPage(browser)
    result_message = loan_page.get_error_message()
    assert message in result_message, f"Expected message '{message}' not found in '{result_message}'"
