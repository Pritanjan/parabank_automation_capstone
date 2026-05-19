Feature: Accounts Overview

  Scenario: Verify account dashboard details

    Given user logs into parabank application
    When user navigates to accounts overview page
    Then account details should display successfully