# Banking Loan & Financial Transaction Automation Testing

## Project Overview

This project automates the testing of banking loan processing and financial transactions using the ParaBank demo application. It focuses on validating core banking workflows such as customer authentication, loan application processing, EMI validation, fund transfers, and transaction history verification.

The automation framework is designed to simulate real-world banking scenarios and ensure the application behaves correctly under various customer profiles, loan conditions, and transaction cases.

---

## Problem Statement

Manual testing of banking systems involving loans, EMI calculations, and financial transactions is time-consuming and prone to errors. Since banking applications deal with sensitive financial data, a robust automation framework is essential to validate critical functionalities such as:

- Loan application approval/rejection
- EMI calculation
- Fund transfer
- Balance updates
- Transaction history accuracy
- Security validations

---

## Objectives

- Automate loan application workflows
- Validate EMI calculations and payment schedules
- Perform data-driven testing for multiple loan/customer profiles
- Verify fund transfer transactions and balance updates
- Support cross-browser execution
- Enable parallel test execution
- Generate detailed reports
- Validate backend APIs for loan and transaction processing

---

## Application Under Test

### ParaBank Demo Application

🔗 URL: http://parabank.parasoft.com/parabank/index.htm

ParaBank is a free demo banking website provided by Parasoft. It simulates real banking operations and is widely used for automation practice.

Features used in this project:

- User Registration
- Login
- Account Overview
- Loan Request
- Fund Transfer
- Bill Payment
- Transaction History

---

## Tech Stack

| Component | Technology |
|----------|-----------|
| Programming Language | Python |
| Automation Tool | Selenium WebDriver |
| Testing Framework | pytest |
| Design Pattern | Page Object Model (POM) |
| Reporting | HTML Reports |
| CI/CD | GitHub Actions (Optional) |

---

## Project Structure

```bash
BankingAutomationProject/
│
├── tests/
│   ├── test_login.py
│   ├── test_loan.py
│   ├── test_fund_transfer.py
│   └── test_transaction_history.py
│
├── pages/
│   ├── login_page.py
│   ├── dashboard_page.py
│   ├── loan_page.py
│   └── transfer_page.py
│
├── utilities/
│   ├── utils_report.py
|
├── screenshots/
│
├── requirements.txt
├── pytest.ini
└── README.md
