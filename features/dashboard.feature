Feature: Dashboard Functionality

    Scenario: Verify dashboard page after successful login

        Given user logs into parabank application
        When user navigates to dashboard page
        Then dashboard should display successfully