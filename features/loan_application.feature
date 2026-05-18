Feature: Loan Application Processing

Scanario: Apply for a loan with valid amount
    Given I navigate to the Request Loan page
    When I enter loan amount '5000' and down payment '500'
    And  I submit the loan application
    Then I should see a confirmation message 'Your loan application has been submitted successfully.'

  Scenario: Apply for a loan with invalid amount
    Given I navigate to the Request Loan page
    When I enter loan amount '-1000' and down payment '500'
    And I submit the loan application
    Then I should see an error message 'We cannot grant a loan in that amount with your available funds.'

  Scenario: Apply for a loan with zero down payment
    Given I navigate to the Request Loan page
    When I enter loan amount '3000' and down payment '0'
    And I submit the loan application
    Then I should see a confirmation message 'Your loan application has been submitted successfully.'
