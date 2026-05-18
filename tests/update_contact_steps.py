from pytest_bdd import scenarios, when, then
from pages.update_contact_page import UpdateContactPage

scenarios("../features/update_contact_info.feature")


@when("user navigates to Update Contact Info page")
def navigate_update_contact(driver):
    UpdateContactPage(driver).navigate_to_update_contact_page()


@when('user updates first name as "John"')
def update_first_name(driver):
    UpdateContactPage(driver).enter_first_name("John")


@when('user updates last name as "Doe"')
def update_last_name(driver):
    UpdateContactPage(driver).enter_last_name("Doe")


@when('user updates address as "New Street 101"')
def update_address(driver):
    UpdateContactPage(driver).enter_address("New Street 101")


@when('user updates city as "Lucknow"')
def update_city(driver):
    UpdateContactPage(driver).enter_city("Lucknow")


@when('user updates state as "Uttar Pradesh"')
def update_state(driver):
    UpdateContactPage(driver).enter_state("Uttar Pradesh")


@when('user updates zip code as "226001"')
def update_zip(driver):
    UpdateContactPage(driver).enter_zip_code("226001")


@when('user updates phone number as "9876543210"')
def update_phone(driver):
    UpdateContactPage(driver).enter_phone("9876543210")


@when("user clicks on update profile button")
def click_update(driver):
    UpdateContactPage(driver).click_update_profile()


@then("contact information should be updated successfully")
def validate_profile_update(driver):
    assert UpdateContactPage(driver).is_profile_updated()


@then("updated contact information should be displayed correctly")
def validate_updated_info(driver):
    assert UpdateContactPage(driver).is_profile_updated()