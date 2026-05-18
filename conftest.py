import pytest

from selenium import webdriver

from selenium.webdriver.chrome.service import (
    Service
)

from webdriver_manager.chrome import (
    ChromeDriverManager
)


BASE_URL = (
    "http://parabank.parasoft.com/parabank/index.htm"
)

    driver = webdriver.Chrome(
        service=service
    )

@pytest.fixture(scope="function")
def browser():

    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument(
        "--disable-session-crashed-bubble"
    )

    service = Service(
        ChromeDriverManager().install()
    )

    driver = webdriver.Chrome(
        service=service,
        options=options
    )

    driver.implicitly_wait(10)

    driver.set_page_load_timeout(30)

    try:

        driver.get(BASE_URL)

    except Exception:

        driver.refresh()

    yield driver

    try:

        driver.delete_all_cookies()

        driver.quit()

    except Exception:

        pass
