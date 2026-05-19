Feature: Loan Application Processing
  As a bank customer
  I want to apply for loans
  So that I can get financial assistance

  Background:
    Given I am logged in as "john" with password "demo"

Scenario: Update contact information
    Given I navigate to the Update Contact Info page
    When I update my address to "123 Main St, Anytown, USA"
    And I update my phone number to "555-123-4567"
    And I submit the updated contact information
    Then I should see a confirmation message "Your contact information has been updated successfully"