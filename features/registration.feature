Feature: User Registration

  Scenario: Successful User Registration

    Given user launches parabank application
    When user clicks on register link
    And user enters registration details
    And user clicks register button
    Then user account should be created successfully