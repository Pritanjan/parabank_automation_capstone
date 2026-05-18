Feature: Loan Approval Process

Scanario: User submits a loan application and it gets approved
    Given I have submitted a loan application with amount '1000' and down payment '500'
    When the loan application is reviewed by the system
    Then I should receive an approval message 'Congratulations! Your loan application has been approved.'

  Scenario: User submits a loan application and it gets denied
    Given I navigate to the Request Loan page
    When I have submitted a loan application with amount '10000' and down payment '1000'
    And I submit the loan application
    Then I should receive a denial message 'You do not have sufficient funds for the given down payment.'
    