from behave import *


# Ghiven, When, Add, But, Then  -  gherkin sintax
# Ghiven seteaza situatia curenta
# When defineste  pasii din test
# Then efectuiaza verificarea testului

@Given('sign in: I am a user on jules sign in page')
def step_impl(context):
    context.sign_in_page.navigate_to_sign_in_page()


@When('sign_in: I set my email to "{email}"')
def step_impl(context, email):
    context.sign_in_page.set_email(email)


@When('sign_in: I set my password to "{pwd}"')
def step_impl(context, pwd):
    context.sign_in_page.set_pwd(pwd)


@When('sign_in: I click the login button')
def step_impl(context):
    context.sign_in_page.click_login_button()


@When('sign in: I click the forgot password link')
def step_impl(context):
    context.sign_in_page.click_forgot_pwd_link()


@Then('sign_in: I am returned to the home page')
def step_impl(context):
    context.sign_in_page.check_current_url()
