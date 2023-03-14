Feature: User login
As a user, I want to be able to login as a returning user
Scenario: Successful login
  Given the user is on the “Sign in” page
  When the user enters their username with a corresponding password and token
  Then clicks the “sign in” button