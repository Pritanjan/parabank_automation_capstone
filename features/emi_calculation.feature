Feature: Loan Application Processing
  As a bank customer
  I want to apply for loans
  So that I can get financial assistance

  Background:
    Given I am logged in as "john" with password "demo"
    

Scenario: Apply for loan with zero down payment
    Given I navigate to the Request Loan page
    When I enter loan amount "5000" and down payment "0"
    And I submit the loan application
    Then the loan response page should be displayed