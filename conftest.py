import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


BASE_URL = "http://parabank.parasoft.com/parabank/index.htm"


@pytest.fixture(scope="function")
def browser():

    service = Service(
        ChromeDriverManager().install()
    )

    driver = webdriver.Chrome(
        service=service
    )

    driver.maximize_window()

    driver.implicitly_wait(10)

    driver.get(BASE_URL)

    yield driver

    driver.quit()
    