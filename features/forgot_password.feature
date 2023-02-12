Feature: Jules forgot password tests
  # se ruleaza inaintea fiecarui test
Background:
  Given sign_in: I am an user on Jules sign in page

  @tinta
  Scenario: Wrong email validation message
    When sign_in: I click the forgot password link
    When forgot_pwd: I set my email to "Margelatu"
    Then forgot_pwd: I verify that the email validation is correct
