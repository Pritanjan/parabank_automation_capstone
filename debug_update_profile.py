from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--remote-allow-origins=*')
options.add_argument('--window-size=1920,1080')

driver = webdriver.Chrome(options=options)

try:
    driver.implicitly_wait(10)
    driver.get('https://parabank.parasoft.com/parabank/index.htm')
    driver.find_element(By.NAME, 'username').send_keys('john')
    driver.find_element(By.NAME, 'password').send_keys('demo')
    driver.find_element(By.XPATH, "//input[@value='Log In']").click()
    WebDriverWait(driver, 10).until(EC.url_contains('overview'))
    driver.find_element(By.LINK_TEXT, 'Update Contact Info').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'customer.firstName')))
    driver.find_element(By.ID, 'customer.firstName').clear()
    driver.find_element(By.ID, 'customer.firstName').send_keys('John')
    driver.find_element(By.ID, 'customer.lastName').clear()
    driver.find_element(By.ID, 'customer.lastName').send_keys('Doe')
    driver.find_element(By.ID, 'customer.address.street').clear()
    driver.find_element(By.ID, 'customer.address.street').send_keys('New Street 101')
    driver.find_element(By.ID, 'customer.address.city').clear()
    driver.find_element(By.ID, 'customer.address.city').send_keys('Lucknow')
    driver.find_element(By.ID, 'customer.address.state').clear()
    driver.find_element(By.ID, 'customer.address.state').send_keys('Uttar Pradesh')
    driver.find_element(By.ID, 'customer.address.zipCode').clear()
    driver.find_element(By.ID, 'customer.address.zipCode').send_keys('226001')
    driver.find_element(By.ID, 'customer.phoneNumber').clear()
    driver.find_element(By.ID, 'customer.phoneNumber').send_keys('9876543210')
    driver.find_element(By.XPATH, "//input[@value='Update Profile']").click()
    time.sleep(3)
    print('URL after submit:', driver.current_url)
    locators = [
        ('id updateProfileResult', (By.ID, 'updateProfileResult')),
        ('xpath updated', (By.XPATH, "//*[contains(text(),'updated') or contains(text(),'Updated') or contains(text(),'updated successfully') or contains(text(),'successfully') or contains(text(),'success')]")),
    ]
    for name, locator in locators:
        try:
            el = driver.find_element(*locator)
            print(name, '=>', repr(el.text), 'visible', el.is_displayed())
        except Exception as e:
            print(name, 'not found', type(e).__name__, str(e))
    source = driver.page_source
    if 'updateProfileResult' in source:
        idx = source.index('updateProfileResult')
        print(source[max(0, idx-200):idx+500])
    else:
        print('no updateProfileResult in page source')
finally:
    driver.quit()
