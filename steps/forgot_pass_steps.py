from behave import *


@When('forgot password: I set my email to "{email}"')
def step_impl(context, email):
    context.sign_in_page.set_email(email)


@Then('forgot password: I verify that email validation message is correct')
def step_impl(context):
    context.forgot_pass.verify_error_email_message()