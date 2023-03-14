Feature: Test User registration
  As a test user, I want to be able to create an account
  Scenario: Successful account creation
    Given the test user is on the “Register” page
    When the test user enters a valid username, valid email, valid password and confirms the password
    And clicks the “Register” button
    Then the test user has now successfully created an account