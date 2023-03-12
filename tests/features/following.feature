Feature: Follow / Unfollow
  As a user I want to follow and unfollow other users
  Scenario: The user wants to follow another user
    Given the user is logged in 
    And clicks on another user profile
    When the user clicks the follow button
    Then the user is following the other user 
    And the followers and following numbers of the users increments by 1