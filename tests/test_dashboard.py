from pytest_bdd import scenarios, given, when, then

from pages.dashboard_page import DashboardPage


scenarios("../features/dashboard.feature")


@given("user logs into parabank application")
def login_application(browser):

    browser.dashboard = DashboardPage(browser)

    browser.dashboard.open_application()

    browser.dashboard.login(
        "john",
        "demo"
    )


@when("user navigates to dashboard page")
def open_dashboard(browser):

    pass


@then("dashboard should display successfully")
def verify_dashboard(browser):

    assert browser.dashboard.dashboard_displayed()