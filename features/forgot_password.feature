Feature: Jules forgot password tests

  Background:
    Given sign in: I am a user on jules sign in page

  @tinta
    Scenario: wrong email validation message
    When sign in: I click the forgot password link
    When forgot password: I set my email to "abc"
    Then forgot password: I verify that email validation message is correct

  @tinta
    Scenario Outline: wrong email validation message with table data
    When sign in: I click the forgot password link
    When forgot password: I set my email to "<email_address>"
    Then forgot password: I verify that email validation message is correct

    Examples:
      | email_address |
      | abcde.com     |
      | abc           |
