Feature: Loan Approval Process

  Background:
    Given I am logged in as "john" with password "demo"

  Scenario: User submits a loan application and it gets approved
    Given I navigate to the Request Loan page
    When I enter loan amount '1000' and down payment '100'
    And I select from account
    And I submit the loan application
    And the loan application is reviewed by the system
    Then I should receive an approval message 'Approved'

  Scenario: Apply for a loan with valid amount
    Given I navigate to the Request Loan page
    When I enter loan amount '5000' and down payment '500'
    And I select from account
    And I submit the loan application
    Then I should receive an approval message 'Approved'

  Scenario: Apply for a loan with zero down payment
    Given I navigate to the Request Loan page
    When I enter loan amount '3000' and down payment '0'
    And I select from account
    And I submit the loan application
    Then I should receive an approval message 'Approved'
