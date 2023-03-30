Feature: Logging in with two factor authentication
  As a user I want to login user two factor authentication and make a mistake to know it works
  Scenario: The user wants to login using two factor authentication
    Given the user is on the login page
    And enters their username,password, and incorrect two factor token
    When the user presses sign in
    Then the user is not logged in