Feature: Open New Account Functionality

    Scenario: User opens a new savings account successfully

        Given user logs in with valid credentials

        When user navigates to open new account page

        And user selects "SAVINGS" account type

        And user submits new account request

        Then new account should be created successfully


    Scenario: User opens a new checking account successfully

        Given user logs in with valid credentials

        When user navigates to open new account page

        And user selects "CHECKING" account type

        And user submits new account request

        Then new account should be created successfully