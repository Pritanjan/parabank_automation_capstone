Feature: Bill Payment Functionality for Parabank Application

  Background:
    Given user launches the ParaBank application
    And user logs in with username "priyanshu14" and password "priyanshu123"

  Scenario: Pay bill successfully with valid details
    Given user navigates to Bill Pay page
    When user enters valid payee information
    And user enters payment amount "100"
    And user selects account for bill payment
    And user clicks on Send Payment button
    Then bill payment should be completed successfully

  Scenario: Verify bill payment confirmation message
    Given user navigates to Bill Pay page
    When user enters valid payee information
    And user enters payment amount "50"
    And user selects account for bill payment
    And user clicks on Send Payment button
    Then user should see bill payment confirmation message

  Scenario: Pay bill with blank payee details
    Given user navigates to Bill Pay page
    When user leaves payee information blank
    And user clicks on Send Payment button
    Then appropriate bill payment validation message should be displayed