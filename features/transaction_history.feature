Feature: Transaction History Validation for Parabank Application

  Background:
    Given user launches the ParaBank application
    And user logs in with username "john" and password "demo"

  Scenario: View transaction history for selected account
    Given user navigates to Accounts Overview page
    When user selects an account number
    Then transaction history page should be displayed

  Scenario: Verify transaction details are visible
    Given user navigates to Accounts Overview page
    When user selects an account number
    Then transaction date, description, debit and credit details should be displayed

  Scenario: Verify bill payment transaction appears in transaction history
    Given user completes a bill payment of amount "100"
    When user navigates to transaction history for the payment account
    Then bill payment transaction should be displayed in transaction history