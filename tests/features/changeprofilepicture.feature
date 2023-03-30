Feature: Changing profile picture
  As a user I want to change my profile picture
  Scenario: The user wants to change their profile picture
    Given the user is logged in
    And on the "Profile" page
    When the user clicks the “Edit your profile” button
    And the user pastes a link to an imgur in the "Post the link" box
    And the user presses submit
    Then the users profile picture updates
