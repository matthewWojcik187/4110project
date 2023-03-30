Feature: User registration
  As a user, I want to be able to create an account
  Scenario: Successful account creation
    Given the user is on the “Register” page
    When the user enters a valid username, valid email, valid password and confirms the password
    And clicks the “Register” button
    Then the user has now successfully created an account