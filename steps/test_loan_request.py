"""
test_loan_request.py - Test cases for Loan Application Processing
Parabank Automation Capstone - Loan Rejection Scenarios
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.loan_request import LoanRequestPage


# ─── Fixtures ──────────────────────────────────────────────────────────────

@pytest.fixture
def loan_page(browser):
    """Initialize Loan Request Page object."""
    return LoanRequestPage(browser)


@pytest.fixture
def login_user(browser):
    """Login with default credentials before each test."""
    # Navigate to login
    browser.get("http://parabank.parasoft.com/parabank/index.htm")
    
    # Find and fill login form
    username_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "j_username"))
    )
    password_field = browser.find_element(By.NAME, "j_password")
    login_button = browser.find_element(By.XPATH, "//input[@value='Log In']")
    
    # Enter credentials
    username_field.send_keys("john")
    password_field.send_keys("demo")
    login_button.click()
    
    # Wait for login to complete (verify we're on dashboard)
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Request Loan"))
    )
    
    yield browser


@pytest.fixture
def navigate_to_loan_page(login_user):
    """Navigate to Request Loan page after login."""
    loan_link = login_user.find_element(By.LINK_TEXT, "Request Loan")
    loan_link.click()
    
    # Wait for loan page to load
    WebDriverWait(login_user, 10).until(
        EC.presence_of_element_located((By.ID, "amount"))
    )
    
    yield login_user


# ─── Test Cases ────────────────────────────────────────────────────────────

class TestLoanRejection:
    """Test cases for Loan Rejection scenarios from loan_rejection.feature"""

    def test_apply_for_loan_with_very_high_amount_should_be_denied(
        self, navigate_to_loan_page, loan_page
    ):
        """
        Scenario: Apply for loan with very high amount - should be Denied
        
        Given I am logged in as "john" with password "demo"
        Given I navigate to the Request Loan page
        When I enter loan amount "999999999" and down payment "10"
        And I submit the loan application
        Then the loan status should be "Denied"
        """
        driver = navigate_to_loan_page
        
        # Enter loan amount and down payment
        loan_page.enter_loan_amount("999999999")
        loan_page.enter_down_payment("10")
        
        # Submit the loan application
        loan_page.click_apply_now()
        
        # Wait for and verify loan status is "Denied"
        wait = WebDriverWait(driver, 10)
        status_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//p[contains(text(), 'status') or contains(text(), 'Status')]")
            )
        )
        
        assert "Denied" in status_element.text or "denied" in status_element.text.lower(), \
            f"Expected loan status to be 'Denied', but got: {status_element.text}"

    @pytest.mark.parametrize(
        "amount,down_payment,expected_status",
        [
            ("9999999", "1", "Denied"),
        ]
    )
    def test_loan_rejection_data_driven(
        self, navigate_to_loan_page, loan_page, amount, down_payment, expected_status
    ):
        """
        Scenario Outline: Data-driven loan testing
        
        Given I am logged in as "john" with password "demo"
        Given I navigate to the Request Loan page
        When I enter loan amount "<amount>" and down payment "<down_payment>"
        And I submit the loan application
        Then the loan status should be "<expected_status>"
        
        Examples:
            | amount  | down_payment | expected_status |
            | 9999999 | 1            | Denied          |
        """
        driver = navigate_to_loan_page
        
        # Enter loan amount and down payment
        loan_page.enter_loan_amount(amount)
        loan_page.enter_down_payment(down_payment)
        
        # Submit the loan application
        loan_page.click_apply_now()
        
        # Wait for and verify loan status matches expected status
        wait = WebDriverWait(driver, 10)
        status_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//p[contains(text(), 'status') or contains(text(), 'Status')]")
            )
        )
        
        assert expected_status in status_element.text, \
            f"Expected loan status to be '{expected_status}', but got: {status_element.text}"

    @pytest.mark.parametrize(
        "amount,down_payment,expected_status",
        [
            ("999999999", "10", "Denied"),      # Very high amount
            ("9999999", "1", "Denied"),         # High amount, minimal down payment
            ("500000", "5000", "Denied"),       # High amount with higher down payment
            ("100000", "1000", "Denied"),       # Medium-high amount
        ]
    )
    def test_loan_rejection_multiple_scenarios(
        self, navigate_to_loan_page, loan_page, amount, down_payment, expected_status
    ):
        """
        Extended data-driven test with multiple rejection scenarios.
        Covers various high-value loan applications that should be rejected.
        """
        driver = navigate_to_loan_page
        
        # Enter loan amount and down payment
        loan_page.enter_loan_amount(amount)
        loan_page.enter_down_payment(down_payment)
        
        # Submit the loan application
        loan_page.click_apply_now()
        
        # Wait for and verify loan status
        wait = WebDriverWait(driver, 10)
        status_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//p[contains(text(), 'status') or contains(text(), 'Status')]")
            )
        )
        
        assert expected_status in status_element.text, \
            f"Amount: {amount}, Down Payment: {down_payment} - " \
            f"Expected '{expected_status}', but got: {status_element.text}"

    def test_loan_application_contains_application_id(
        self, navigate_to_loan_page, loan_page
    ):
        """
        Verify that after loan application (even if denied),
        the system returns an application ID for tracking.
        """
        driver = navigate_to_loan_page
        
        # Enter loan amount and down payment
        loan_page.enter_loan_amount("999999999")
        loan_page.enter_down_payment("10")
        
        # Submit the loan application
        loan_page.click_apply_now()
        
        # Wait for and verify application ID is displayed
        wait = WebDriverWait(driver, 10)
        app_id_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, 
                 "//*[contains(text(), 'Application ID') or contains(text(), 'application id')]")
            )
        )
        
        assert app_id_element is not None, \
            "Application ID should be displayed after loan application submission"

    def test_loan_rejection_message_clarity(
        self, navigate_to_loan_page, loan_page
    ):
        """
        Verify that loan rejection message is clear and informative.
        """
        driver = navigate_to_loan_page
        
        # Enter loan amount and down payment
        loan_page.enter_loan_amount("999999999")
        loan_page.enter_down_payment("10")
        
        # Submit the loan application
        loan_page.click_apply_now()
        
        # Wait for rejection message
        wait = WebDriverWait(driver, 10)
        status_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//p[contains(text(), 'status') or contains(text(), 'Status')]")
            )
        )
        
        # Verify status shows "Denied"
        assert "Denied" in status_element.text or "denied" in status_element.text.lower(), \
            f"Expected 'Denied' in status message, got: {status_element.text}"
        
        # Verify the status element is visible and readable
        assert status_element.is_displayed(), \
            "Loan status message should be visible to the user"
