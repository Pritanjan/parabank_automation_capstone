from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC   

class LoanApplicationPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    # locators 
    LOAN_AMOUNT =  (By.ID, "amount")
    DOWN_PAYMENT = (By.ID, "downPayment")
    FROM_ACCOUNT = (By.ID, "fromAccountId")
    APPLY_NOW_BUTTON = (By.XPATH, "//input[@value='Apply Now']")
    
    APPROVAL_MESSAGE = (
        By.XPATH,
        "//h1[contains(text(),'Loan Request Processed')]"
    )

    RESULT_MESSAGE = (
        By.ID,
        "loanStatus"
    )

    ERROR_MESSAGE = (
        By.ID,
        "loanRequestDenied"
    )
    
    def enter_loan_amount(self, amount):
        self.driver.find_element(*self.LOAN_AMOUNT).clear()
        self.driver.find_element(*self.LOAN_AMOUNT).send_keys(amount)
    
    def enter_down_Payemnt(self, payment):
        self.driver.find_element(*self.DOWN_PAYMENT).clear()
        self.driver.find_element(*self.DOWN_PAYMENT).send_keys(payment)

    def select_from_account(self, account_id):        
        from_account_dropdown = self.driver.find_element(*self.FROM_ACCOUNT)
        for option in from_account_dropdown.find_elements(By.TAG_NAME, 'option'):
            if option.get_attribute('value') == account_id:
                option.click()
                break
    
    def click_apply_now(self):
        self.driver.find_element(*self.APPLY_NOW_BUTTON).click()
    
    def get_result(self):
        return self.wait.until(
            EC.visiibility_of_element_located((By.ID, "loanRequestApproved"))
        )
        
    def get_errot_message(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.ID, "loanRequestDenied"))
        )
