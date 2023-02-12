from behave import *

@When('forgot_pwd: I set my email to "{email}"')
def step_impl(context,email):
    context.sign_in_page.set.email(email)

@Then('forgot_pwd: I verify that the email validaition is correct')
def step_impl(context):
    context.forgot_pass.verify_error_email_message()