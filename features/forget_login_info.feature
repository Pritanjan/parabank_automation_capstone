Feature: Forgot Login Information for Parabank Application

    Scenario: Navigate to forgot login information page
        Given user launches the Parabank application
        When user clicks on "Forgot login info?" link
        Then user should see the Forgot Login Information page

    Scenario: Retrieve login information with valid details
        Given user is on the Forgot Login Information page
        When user enters first name "John"
        And user enters last name "Doe"
        And user enters address "Address1"
        And user enters city "City1"
        And user enters state "State1"
        And user enters zip code "100001"
        And user enters ssn "123"
        # When user enters first name "John"
        # And user enters last name "Smith"
        # And user enters address "1431 Main St"
        # And user enters city "Beverly Hills"
        # And user enters state "CA"
        # And user enters zip code "73301"
        # And user enters ssn "5125559021"
        # When user enters first name "John"
        # And user enters last name "Doe"
        # And user enters address "123 Main St"
        # And user enters city "Anytown"
        # And user enters state "CA"
        # And user enters zip code "90210"
        # And user enters ssn "123456789"
        And user clicks on Find My Login Info button
        Then user should receive login information reset instructions

    Scenario: Display error when required details are missing
        Given user is on the Forgot Login Information page
        When user leaves required fields blank
        And user clicks on Find My Login Info button
        Then user should see a validation error message

    Scenario: Show error for invalid account information
        Given user is on the Forgot Login Information page
        When user enters invalid account details
        And user clicks on Find My Login Info button
        Then user should see an invalid information error message
