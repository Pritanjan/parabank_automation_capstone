Feature: Loan Application Processing
  As a bank customer
  I want to apply for loans
  So that I can get financial assistance

  Background:
    Given I am logged in as "john" with password "demo"

Scenario: Apply for loan with very high amount - should be Denied
    Given I navigate to the Request Loan page
    When I enter loan amount "999999999" and down payment "10"
    And I submit the loan application
    Then the loan status should be "Denied"

Scenario Outline: Data-driven loan testing
    Given I navigate to the Request Loan page
    When I enter loan amount "<amount>" and down payment "<down_payment>"
    And I submit the loan application
    Then the loan status should be "<expected_status>"

    Examples:
      | amount  | down_payment | expected_status |
      | 9999999 | 1            | Denied          |