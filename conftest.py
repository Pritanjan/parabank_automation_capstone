"""
conftest.py - Global fixtures and hooks for Pytest-BDD
Banking Automation Project - Parabank
"""

import pytest
import os
from datetime import datetime

from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


BASE_URL = "http://parabank.parasoft.com/parabank/index.htm"

REPORTS_DIR = os.path.join(
    os.path.dirname(__file__),
    "reports"
)


def pytest_addoption(parser):

    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome | firefox"
    )


@pytest.fixture(scope="function")
def browser(request):

    browser_name = request.config.getoption("--browser").lower()

    if browser_name == "firefox":

        service = FirefoxService(
            GeckoDriverManager().install()
        )

        driver = webdriver.Firefox(service=service)

    else:

        service = ChromeService(
            ChromeDriverManager().install()
        )

        options = webdriver.ChromeOptions()

        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")

        driver = webdriver.Chrome(
            service=service,
            options=options
        )

    driver.implicitly_wait(10)

    driver.get(BASE_URL)

    yield driver

    driver.quit()


@pytest.fixture(scope="session", autouse=True)
def setup_reports():

    os.makedirs(REPORTS_DIR, exist_ok=True)


def pytest_bdd_before_scenario(request, feature, scenario):

    print(f"\n▶ SCENARIO: {scenario.name}")


def pytest_bdd_after_scenario(request, feature, scenario):

    print(f"\n✓ DONE: {scenario.name}")


def pytest_bdd_step_error(
        request,
        feature,
        scenario,
        step,
        step_func,
        step_func_args,
        exception
):

    driver = request.getfixturevalue("browser")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    screenshot_name = (
        f"{scenario.name.replace(' ', '_')}_{timestamp}.png"
    )

    screenshot_path = os.path.join(
        REPORTS_DIR,
        screenshot_name
    )

    driver.save_screenshot(screenshot_path)

    print(f"\n📸 Screenshot saved: {screenshot_path}")


def pytest_html_report_title(report):

    report.title = "Banking Automation Report - Parabank"