from behave import *
# Ghiven, When, Add, But, Then  -  gherkin sintax
# Ghiven seteaza situatia crenta
# When defineste  pasii din test
# Then efectuiaza verificarea testului

@Given('sign_in : I am an user on Jules sign in page')
def step_impl(context):
    context.sign_in_page.navigate_to_sign_in_page()

@When('sign_in: I set my email to "{email}"')
def step_impl(context,email):
    context.sign_in_page.set.email(email)

@When('sign_in: I set my password to "{pwd}"')
def step_impl(context, pwd):
    context.sign_in_page.set_pwd(pwd)

@When('sign_in: I click the login button')
def step_impl(context):
    context.sign_in_page.click_login_button()

@When('sign_in: I click the forgot password link')
def step_impl(context):
    context.sign_in_page.click_forgot_pwd_link()

@Then('sign_in: I am returned to the home page')
def step_impl(context):
    context.sign_in_page.check_current_url()



