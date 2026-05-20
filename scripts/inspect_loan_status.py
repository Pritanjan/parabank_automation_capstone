from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
try:
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('http://parabank.parasoft.com/parabank/index.htm')
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'username')))
    driver.find_element(By.NAME, 'username').send_keys('parabank')
    driver.find_element(By.NAME, 'password').send_keys('parabank')
    driver.find_element(By.XPATH, "//input[@value='Log In']").click()
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Request Loan'))
    )
    print('After login URL:', driver.current_url)
    links = driver.find_elements(By.LINK_TEXT, 'Request Loan')
    print('Found Request Loan links:', len(links))
    for idx, link in enumerate(links, 1):
        print(idx, link.get_attribute('href'), link.text, link.is_displayed(), link.is_enabled())
    if links:
        request_loan_link = links[0]
        request_loan_link.click()
    print('After clicking request loan URL:', driver.current_url)
    print('Request loan page source contains amount id:', 'id="amount"' in driver.page_source.lower())
    print('Request loan page source contains downPayment id:', 'id="downpayment"' in driver.page_source.lower())
    print('Request loan page source contains fromAccountId id:', 'id="fromaccountid"' in driver.page_source.lower())
    print('Request loan page source contains requestloan:', 'requestloan' in driver.page_source.lower())
    print('Request loan page source first 500 chars:', driver.page_source[:500])
    try:
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'amount')))
        print('Found amount id after click')
    except Exception as exc:
        print('Could not find amount by ID after click:', type(exc).__name__, exc)
    driver.find_element(By.ID, 'amount').send_keys('1000')
    driver.find_element(By.ID, 'downPayment').send_keys('100')
    dropdown = driver.find_element(By.ID, 'fromAccountId')
    options = dropdown.find_elements(By.TAG_NAME, 'option')
    if options:
        options[0].click()
    driver.find_element(By.XPATH, "//input[@value='Apply Now']").click()
    WebDriverWait(driver, 20).until(lambda d: any(x in d.page_source.lower() for x in ['approved', 'denied', 'loan status', 'status']))
    src = driver.page_source.lower()
    print('---CURRENT URL---')
    print(driver.current_url)
    print('---PAGE SOURCE MARKERS---')
    for keyword in ['loanstatus', 'approved', 'denied', 'status', 'loan status']:
        idx = src.find(keyword)
        print(f"{keyword}:", idx != -1, "at", idx)
        if idx != -1:
            start = max(0, idx - 80)
            end = min(len(src), idx + 120)
            print(src[start:end].replace('\n', ' '))
    body = driver.find_element(By.TAG_NAME, 'body').text
    print('---BODY TEXT---')
    for line in body.splitlines():
        if any(k in line.lower() for k in ['approved', 'denied', 'loan status', 'status']):
            print(line)
    print('---ATTRIBUTE ELEMENTS---')
    all_elements = driver.find_elements(By.XPATH, '//*')
    for e in all_elements:
        try:
            attrs = e.get_attribute('outerHTML')
        except Exception:
            continue
        if any(x in attrs.lower() for x in ['loanstatus', 'approved', 'denied', 'loan status', 'status']):
            print(attrs[:400].replace('\n',' '))
            print('---')
    print('---DONE---')
finally:
    driver.quit()
