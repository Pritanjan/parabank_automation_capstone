Feature: Account Balance and Fund Transfer

  Scenario: User transfers funds between accounts and verifies balance update
    Given user launches the ParaBank application
    And user logs in with username "john" and password "demo"
    Then user should be navigated to Accounts Overview page
    And user captures the initial balance of source account
    And user captures the initial balance of destination account
    When user navigates to Transfer Funds page
    And user transfers amount "100" from source account to destination account
    Then transfer should be completed successfully