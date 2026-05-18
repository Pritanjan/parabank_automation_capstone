Feature: Find Transactions

  As a ParaBank customer
  I want to search transactions
  So that I can verify transaction details

  Background:
    Given user launches the ParaBank application
    And user logs in with username "john" and password "demo"
    Then user should be navigated to Accounts Overview page

  Scenario: Search transaction by date

    When user navigates to Find Transactions page
    And user searches transaction by date "05-18-2026"

    Then transaction details should be displayed

  Scenario: Search transaction by amount

    When user navigates to Find Transactions page
    And user searches transaction by amount "100"

    Then matching transaction records should be displayed

  Scenario: Search transaction by transaction id

    When user navigates to Find Transactions page
    And user searches transaction by id "12345"

    Then corresponding transaction details should be displayed

  Scenario: Validate no transaction found message

    When user navigates to Find Transactions page
    And user searches transaction by id "999999"

    Then no transaction result message should be displayed