from behave import *
from pages.registration_page import RegistrationPage

@given('user launches parabank application')
def step_impl(context):

    pass

@when('user clicks on register link')
def step_impl(context):

    context.registration = RegistrationPage(
        context.driver
    )

    context.registration.click_register_link()

@when('user enters registration details')
def step_impl(context):

    context.registration.enter_registration_details()

@when('user clicks register button')
def step_impl(context):

    context.registration.click_register_button()

@then('user account should be created successfully')
def step_impl(context):

    assert "Welcome" in context.driver.page_source