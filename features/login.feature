Feature: Login Functionality for Parabank Application

    Scenario: Login with valid credentials
        Given user launches the Parabank application
        When user enters valid username and password
        Then user should be redirected to account overview page

    Scenario: Login with invalid username
        Given user launches the Parabank application
        When user enters invalid username and valid password
        Then user should see login failed error message

    Scenario: Login with invalid password
        Given user launches the Parabank application
        When user enters valid username and invalid password
        Then user should see login failed error message

    Scenario: Login with blank credentials
        Given user launches the Parabank application
        When user leaves username and password blank
        Then user should see required field validation message

    Scenario: Logout successfully
        Given user logs in with valid credentials
        When user clicks on logout link
        Then user should be redirected to login page

    Scenario Outline: Login using multiple credentials
        Given user launches the Parabank application
        When user enters username "<username>" and password "<password>"
        Then login result should be "<result>"

        Examples:
            | username    | password     | result  |
            | priyanshu14 | priyanshu123 | success |
            | john123     | wrong123     | failure |
            | invalid     | demo         | failure |