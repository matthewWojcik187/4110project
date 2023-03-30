Feature: Posting Reviews
  As a user I want to post reviews for items and products
  Scenario: User wants to post a review
    Given the test user is logged in 
    And on the “Home” page
    When the test user populates the “Say something” text box with a review
    And they click “Submit”
    Then blog is posted so that everyone can view it on the “Explore” page