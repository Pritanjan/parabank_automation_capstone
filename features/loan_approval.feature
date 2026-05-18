Feature: Loan Approval Process

Scenario: User submits a loan application and it gets approved
    Given I navigate to the Request Loan page
    When I enter loan amount '1000' and down payment '500'
    And I select from account '12345'
    And I submit the loan application
    And the loan application is reviewed by the system
    Then I should receive an approval message 'Congratulations! Your loan application has been approved.'

  Scenario: User submits a loan application and it gets denied
    Given I navigate to the Request Loan page
    When When I enter loan amount '10000' and down payment '1000'
    And I select from account '12345'
    And I submit the loan application
    And the loan application is reviewed by the system
    Then I should receive a denial message 'You do not have sufficient funds for the given down payment.'
    