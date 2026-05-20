Feature: Update Contact Information

  As a ParaBank customer
  I want to update my contact information
  So that my profile remains updated

  Background:
    Given user launches the ParaBank application
    And user logs in with username "john" and password "demo"
    Then user should be navigated to Accounts Overview page

  Scenario: Successfully update contact information

    When user navigates to Update Contact Info page
    And user updates first name as "John"
    And user updates last name as "Doe"
    And user updates address as "New Street 101"
    And user updates city as "Lucknow"
    And user updates state as "Uttar Pradesh"
    And user updates zip code as "226001"
    And user updates phone number as "9876543210"
    And user clicks on update profile button

    Then contact information should be updated successfully
