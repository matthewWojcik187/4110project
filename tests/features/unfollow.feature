 Feature: Follow / Unfollow
 Scenario: The user wants to unfollow another user
    Given the user is logged in
    And clicks on a followed user
    When the user clicks the unfollow button
    Then the user unfollows the other user
    And the followers and following numbers of the users decrements by 1