Feature: Logging in with two factor authentication
  As a user I want to login user two factor authentication
  Scenario: The user wants to login using two factor authentication
    Given the user is on the login page
    And enters their username,password, two factor token
    When the user presses sign in
    Then the user is logged in