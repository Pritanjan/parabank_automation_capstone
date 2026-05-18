from pytest_bdd import given, when, then, scenarios, parsers
from pages.loan_application_page import LoanApplicationPage
from pages.base_page import BasePage

scenarios("../features/loan_application.feature")
scenarios("../features/loan_approval.feature")

# here call users login passwrod fun 

BASE_URL = BasePage.BASE_URL

@given('I navigate to the Request Loan page')
def navigate_to_request_loan_page(driver):
    driver.get(f"{BASE_URL}/requestloan.htm")

@when(parsers.parse('I enter loan amount "{amount}" and down payment "{down_payment}"'))
def enter_loan_amount(driver, loan_amount, down_payment):
    loan_page = LoanApplicationPage(driver)
    loan_page.enter_loan_amount(loan_amount)
    loan_page.enter_down_Payemnt(down_payment)

@when(parsers.parse('I select from account "{account_id}"'))
def select_from_account(driver, account_id):
    loan_page = LoanApplicationPage(driver)
    loan_page.select_from_account(account_id)   

@when('I submit the loan application')
def submit_loan(driver):
    loan_page = LoanApplicationPage(driver)
    loan_page.click_apply_now()

@then(parsers.parse('I should see a confirmation message "{message}"'))
def verify_confirmation_message(driver, message):
    loan_page = LoanApplicationPage(driver)
    result_message = loan_page.get_result()
    
    assert message in result_message.text, f"Expected message '{message}' not found in '{result_message.text}'"


@then(parsers.parse('I should see an error message "{message}"'))
def error_message(driver, message):
    loan_page = LoanApplicationPage(driver)
    error_message = loan_page.get_errot_message()
    
    assert message in error_message.text, f"Expected message '{message}' not found in '{error_message.text}'"
