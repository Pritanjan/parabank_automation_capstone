Feature: Logout Functionality for Parabank Application

    Scenario: Logout successfully from application
        When user clicks on logout link
        Then user should be redirected to login page

    Scenario: Verify session after logout
        When user clicks on logout link
        And user clicks browser back button
        Then user should not access account overview page

    Scenario: Verify login page displayed after logout
        When user clicks on logout link
        Then login form should be displayed

    Scenario: Verify user session timeout after logout
        When user clicks on logout link
        And user tries to access application URL again
        Then user should be asked to login again