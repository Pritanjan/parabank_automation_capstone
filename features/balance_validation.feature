Feature: Account Balance Validation

  As a ParaBank customer
  I want to validate account balances after fund transfer
  So that I can ensure transactions are processed correctly

  Background:
    Given user launches the ParaBank application
    And user logs in with username "john" and password "demo"
    Then user should be navigated to Accounts Overview page

  Scenario: Validate balance deduction after fund transfer

    Given user captures the initial balance of source account
    And user captures the initial balance of destination account

    When user navigates to Transfer Funds page
    And user transfers amount "100" from source account to destination account
    Then transfer should be completed successfully

    When user navigates to Accounts Overview page again
    And user captures updated balance of source account
    And user captures updated balance of destination account

    Then source account balance should be reduced by "100"
    And destination account balance should be increased by "100"

  Scenario: Validate account balance is displayed correctly

    Given user is on Accounts Overview page

    Then all account balances should be displayed
    And available balance should match current balance

  Scenario: Validate balance after multiple transfers

    Given user captures initial balance of source account

    When user navigates to Transfer Funds page
    And user transfers amount "50" from source account to destination account
    Then transfer should be completed successfully

    When user transfers amount "25" from source account to destination account
    Then transfer should be completed successfully

    And user navigates to Accounts Overview page again
    Then source account balance should be reduced by "75"

  Scenario: Validate transfer with insufficient balance

    Given user navigates to Transfer Funds page

    When user transfers amount "999999" from source account to destination account

    Then appropriate transfer failure message should be displayed