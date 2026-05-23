#Banking Loan & Financial Transaction Automation Testing

## Project Overview

This project automates the testing of banking loan processing and financial transactions using the ParaBank demo application. The framework is developed using Python, Selenium WebDriver, Pytest, and the Page Object Model (POM) design pattern.

The automation suite validates important banking workflows such as user registration, login, account creation, loan request processing, fund transfers, bill payments, transaction validation, and account management.

The framework is designed to simulate real-world banking operations and ensure that the application behaves correctly under different customer actions and transaction scenarios.

---

# Problem Statement

Manual testing of banking applications involving loans, account transactions, and fund management is repetitive, time-consuming, and prone to human error.

Since banking systems handle sensitive financial operations, an automation framework is required to validate critical functionalities such as:

* User authentication
* Account creation
* Loan processing
* Fund transfer
* Balance updates
* Transaction validation
* Contact information updates
* Transaction history accuracy

This project helps improve testing efficiency, reliability, and execution speed through automated testing.

---

# Objectives

* Automate end-to-end banking workflows
* Validate loan request processing
* Verify account creation functionality
* Validate fund transfer operations
* Verify bill payment functionality
* Perform positive and negative testing
* Support reusable and scalable automation design
* Generate detailed HTML execution reports
* Improve test coverage and execution efficiency

---

# Application Under Test

## ParaBank Demo Application

🔗 URL: [http://parabank.parasoft.com/parabank/index.htm](http://parabank.parasoft.com/parabank/index.htm)

ParaBank is a demo online banking application provided by Parasoft for automation practice and testing.

### Features Automated in This Project

* User Registration
* User Login
* Open New Savings Account
* Open New Checking Account
* Account Overview
* Fund Transfer
* Bill Payment
* Loan Request
* Update Contact Information
* Transaction History Validation
* Logout Functionality

---

# Tech Stack

| Component            | Technology              |
| -------------------- | ----------------------- |
| Programming Language | Python                  |
| Automation Tool      | Selenium WebDriver      |
| Testing Framework    | Pytest                  |
| BDD Support          | pytest-bdd              |
| Design Pattern       | Page Object Model (POM) |
| Reporting            | HTML Reports            |
| Browser Support      | Chrome & Edge           |
| Version Control      | Git & GitHub            |

---

# Framework Architecture

The framework follows the Page Object Model (POM) architecture for better maintainability, readability, and reusability.

---

# Project Structure

```bash
parabank_automation_capstone/
│
├── pages/
│   ├── login_page.py
│   ├── register_page.py
│   ├── dashboard_page.py
│   ├── open_account_page.py
│   ├── transfer_funds_page.py
│   ├── bill_pay_page.py
│   ├── loan_request_page.py
│   └── update_contact_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_register.py
│   ├── test_open_new_account.py
│   ├── test_transfer_funds.py
│   ├── test_bill_pay.py
│   ├── test_loan_request.py
│   └── test_update_contact_info.py
│
├── utilities/
│   ├── driver_factory.py
│   ├── config_reader.py
│   ├── screenshot_helper.py
│   └── report_helper.py
│
├── screenshots/
│
├── reports/
│
├── requirements.txt
├── pytest.ini
├── conftest.py
└── README.md
```

---

# Key Features of the Framework

## Selenium WebDriver Automation

Automates browser interactions for banking workflows.

## Page Object Model (POM)

Separates locators and page methods from test cases for better code organization.

## Pytest Framework

Provides test execution, fixtures, assertions, and reporting support.

## BDD Support with pytest-bdd

Supports behavior-driven testing for readable test scenarios.

## HTML Reporting

Generates execution reports for test result analysis.

## Reusable Utilities

Includes reusable helper functions for browser setup, screenshots, and reporting.

---

# Automated Test Scenarios

## Registration Testing

* Register new users
* Validate successful registration

## Login Testing

* Verify valid login
* Verify invalid login scenarios

## Open New Account Testing

* Open savings account
* Open checking account
* Validate account creation

## Fund Transfer Testing

* Transfer funds between accounts
* Verify balance updates

## Bill Payment Testing

* Add payee details
* Submit payment
* Verify payment confirmation

## Loan Request Testing

* Submit loan request
* Validate loan approval response

## Contact Information Testing

* Update customer contact information
* Validate successful update

---

# Installation & Setup

## Clone Repository

```bash
git clone https://github.com/Pritanjan/parabank_automation_capstone.git
```

## Navigate to Project Directory

```bash
cd parabank_automation_capstone
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running Test Cases

## Run All Tests

```bash
pytest
```

## Run Tests with Verbose Output

```bash
pytest -v
```

## Generate HTML Report

```bash
pytest --html=reports/report.html --self-contained-html
```

## Run Specific Test File

```bash
pytest tests/test_login.py
```

---

# Reporting

The framework supports HTML reporting for easy result analysis.

Generated reports contain:

* Passed test cases
* Failed test cases
* Error details
* Execution summary
* Timestamp information

---

# Advantages of This Framework

* Scalable automation structure
* Easy maintenance
* Reusable code components
* Clear folder organization
* Faster execution
* Better reporting and debugging
* Supports multiple banking workflows

---

# Future Enhancements

* Jenkins CI/CD Integration
* Docker Integration
* Parallel Execution with pytest-xdist
* Allure Reporting
* API Automation Integration
* Database Validation
* Cross-browser Grid Execution

