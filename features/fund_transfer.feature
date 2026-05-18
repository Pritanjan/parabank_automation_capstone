# features/fund_transfer.feature

Feature: Fund Transfer Between Accounts
  As a bank customer
  I want to transfer funds between my accounts
  So that I can manage my money efficiently

  Background:
    Given I am logged in as "john" with password "demo"

  Scenario: Successful fund transfer between accounts
    Given I navigate to the Transfer Funds page
    When I enter transfer amount "100"
    And I select source and destination accounts
    And I click the Transfer button
    Then the transfer should be successful
    And I should see "Transfer Complete!" message

  Scenario: Transfer with valid small amount
    Given I navigate to the Transfer Funds page
    When I enter transfer amount "50"
    And I select source and destination accounts
    And I click the Transfer button
    Then the transfer should be successful

  Scenario: Verify account balance updates after transfer
    Given I navigate to the Transfer Funds page
    When I enter transfer amount "200"
    And I select source and destination accounts
    And I click the Transfer button
    Then the transfer should be successful
    And I navigate to the accounts overview
    Then account balances should be updated
