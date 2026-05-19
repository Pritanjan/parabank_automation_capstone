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

  Scenario: Find transaction by amount
    Given user navigates to Find Transactions page
    When user enters amount "100" to search
    And user clicks Find Transactions by amount button
    Then transaction results should be displayed

  Scenario: Find transaction by date
    Given user navigates to Find Transactions page
    When user enters date "05-04-2025" to search
    And user clicks Find Transactions by date button
    Then transaction results should be displayed

  Scenario: Find transaction by date range
    Given user navigates to Find Transactions page
    When user enters from date "05-03-2026" and to date "05-06-2026"
    And user clicks Find Transactions by date range button
    Then transaction results should be displayed

  Scenario: Find transaction by transaction ID
    Given user navigates to Find Transactions page
    When user enters transaction ID "12478" to search
    And user clicks Find Transactions by ID button
    Then transaction details page should be displayed