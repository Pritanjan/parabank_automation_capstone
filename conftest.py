import os
import tempfile
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service


BASE_URL = (
    "http://parabank.parasoft.com/parabank/index.htm"
)


def _cached_chromedriver():
    driver_roots = (
        Path.home() / ".cache" / "selenium",
        Path.home() / ".wdm" / "drivers" / "chromedriver",
    )
    drivers = []

    for root in driver_roots:
        if root.exists():
            drivers.extend(root.rglob("chromedriver.exe"))

    if not drivers:
        return None

    return max(
        drivers,
        key=lambda driver_path: driver_path.stat().st_mtime
    )


def _create_chrome_driver(options):
    cached_driver = _cached_chromedriver()

    if cached_driver:
        return webdriver.Chrome(
            service=Service(str(cached_driver)),
            options=options
        )

    return webdriver.Chrome(options=options)


def _chrome_options(user_data_dir):
    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument(
        "--disable-session-crashed-bubble"
    )
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--remote-allow-origins=*")
    options.add_argument(f"--user-data-dir={user_data_dir.name}")

    if os.getenv("HEADLESS", "").lower() in ("1", "true", "yes"):
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

    return options


@pytest.fixture(scope="function")
def browser():
    driver = None
    user_data_dir = None

    for _ in range(2):
        user_data_dir = tempfile.TemporaryDirectory()
        options = _chrome_options(user_data_dir)

        try:
            driver = _create_chrome_driver(options)
            driver.implicitly_wait(10)
            driver.set_page_load_timeout(30)
            driver.get(BASE_URL)
            break
        except WebDriverException:
            if driver:
                try:
                    driver.quit()
                except Exception:
                    pass
            user_data_dir.cleanup()
            driver = None
            user_data_dir = None

    if driver is None:
        raise WebDriverException("Chrome could not start a stable session")

    try:
        yield driver
    finally:
        try:
            driver.delete_all_cookies()
            driver.quit()
        except Exception:
            pass

        if user_data_dir:
            user_data_dir.cleanup()


@pytest.fixture(scope="function")
def driver(browser):
    return browser