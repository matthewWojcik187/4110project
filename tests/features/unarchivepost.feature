Feature: Edit my archives
  As a user I want to edit my archive list
  Scenario: The user wants to remove an archived review
    Given the user is logged in
    And the user has archived posts
    When the user clicks on the "unarchive" button
    Then the review should be removed from the user's archived posts