Feature: Viewing reviews
  As a user I want to archive my favorite posts 
  Scenario: The user wants to archive their favorite posts
    Given the user is logged in
    And on the “Explore” page 
    When the user clicks the “favorite” button
    Then the post is put in their archive
