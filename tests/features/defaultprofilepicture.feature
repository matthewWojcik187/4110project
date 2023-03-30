Feature: Changing profile picture back to default
  As a user I want to clear my profile picture
  Scenario: The user wants to change their profile picture back to its default
    Given the user is logged in
    And on the "Profile" page
    When the user clicks the “Edit your profile” button
    And the user clears the "Post the link" box
    And the user presses submit
    Then the users profile picture returns to the default