Feature: Login Functionality for Parabank Application

  

    Scenario: Login with valid credentials
        When user enters valid username and password
        And clicks on login button
        Then user should be redirected to account overview page

    Scenario: Login with invalid username
        When user enters invalid username and valid password
        And clicks on login button
        Then user should see login failed error message

    Scenario: Login with invalid password
        When user enters valid username and invalid password
        And clicks on login button
        Then user should see login failed error message

    Scenario: Login with blank credentials
        When user leaves username and password blank
        And clicks on login button
        Then user should see required field validation message

    Scenario: Logout successfully
        Given user logs in with valid credentials
        When user clicks on logout button
        Then user should be redirected to login page

    Scenario Outline: Login using multiple credentials
        When user enters username "<username>" and password "<password>"
        And clicks on login button
        Then login result should be "<result>"

        Examples:
            | username | password | result  |
            | john     | demo     | success |
            | john123  | wrong123 | failure |
            | invalid  | demo     | failure |
            |          |          | failure |