# PRODIGY_SQA_03 — Automated Login Test Suite

**Task:** Automated Login Test for a Web Application  
**Track:** Software Quality Assurance (SQA) Internship — Prodigy InfoTech  
**Website Under Test:** [DemoBlaze](https://www.demoblaze.com)  
**Framework:** Python + Pytest + Selenium 4  
**Date:** 2026-05-05

---

## 📁 Project Structure

```
PRODIGY_SQA_03/
│
├── config.py                  # Central config — URL, browser, credentials
├── pytest.ini                 # Pytest settings and markers
├── requirements.txt           # Python dependencies
│
├── utils/
│   ├── __init__.py
│   ├── driver_factory.py      # Browser WebDriver setup (Chrome/Firefox/Edge)
│   └── login_page.py          # Page Object Model for DemoBlaze login
│
├── tests/
│   ├── conftest.py            # Pytest fixtures (driver, login_page)
│   └── test_login.py          # All 28 test cases (positive + negative)
│
└── reports/
    └── test_report.html       # Auto-generated HTML report after run
```

---

## 🧪 Test Cases Summary

### ✅ Positive Test Cases (10)

| Test ID             | Description                                          |
|---------------------|------------------------------------------------------|
| TC-LOGIN-POS-001    | Login with valid username and valid password         |
| TC-LOGIN-POS-002    | Login modal opens on navbar click                    |
| TC-LOGIN-POS-003    | Username field accepts and retains typed input       |
| TC-LOGIN-POS-004    | Password field accepts and retains typed input       |
| TC-LOGIN-POS-005    | Modal closes automatically after successful login    |
| TC-LOGIN-POS-006    | Welcome message shows username after login           |
| TC-LOGIN-POS-007    | User can logout successfully after login             |
| TC-LOGIN-POS-008    | Modal Close (×) button dismisses the modal           |
| TC-LOGIN-POS-009    | Page title is correct on load                        |
| TC-LOGIN-POS-010    | Login modal contains both username and password fields |

### ❌ Negative Test Cases (18)

| Test ID             | Description                                          |
|---------------------|------------------------------------------------------|
| TC-LOGIN-NEG-001    | Wrong password with valid username                   |
| TC-LOGIN-NEG-002    | Non-existent username                                |
| TC-LOGIN-NEG-003    | Both username and password incorrect                 |
| TC-LOGIN-NEG-004    | Empty username field                                 |
| TC-LOGIN-NEG-005    | Empty password field                                 |
| TC-LOGIN-NEG-006    | Both fields empty                                    |
| TC-LOGIN-NEG-007    | Whitespace-only username                             |
| TC-LOGIN-NEG-008    | Whitespace-only password                             |
| TC-LOGIN-NEG-009    | Valid username but password in wrong case            |
| TC-LOGIN-NEG-010    | Username in different case (case sensitivity check)  |
| TC-LOGIN-NEG-011    | SQL injection attempt in username + password         |
| TC-LOGIN-NEG-012    | XSS payload in username field                        |
| TC-LOGIN-NEG-013    | Extremely long username (300 characters)             |
| TC-LOGIN-NEG-014    | Special characters in username field                 |
| TC-LOGIN-NEG-015    | Numeric-only credentials (unregistered)              |
| TC-LOGIN-NEG-016    | Correct user + completely wrong password             |
| TC-LOGIN-NEG-017    | Modal fields persistence after close/reopen          |
| TC-LOGIN-NEG-018    | Login button visibility and enabled state            |

**Total: 28 automated test cases**

---

## ⚙️ Setup Instructions

### 1. Clone or download this repository

```bash
git clone https://github.com/Shihab157/PRODIGY_SQA_03.git
cd PRODIGY_SQA_03
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

> `webdriver-manager` will automatically download the correct ChromeDriver/GeckoDriver.

### 3. Register a test account on DemoBlaze

Before running the tests:
1. Go to [https://www.demoblaze.com](https://www.demoblaze.com)
2. Click **Sign Up**
3. Enter the credentials from `config.py`:
   - Username: `prodigy_test_user`
   - Password: `Test@1234`
4. Click **Sign up** and confirm registration

> ⚠️ The tests will fail if this account doesn't exist. Change credentials in `config.py` if you use different ones.

### 4. Configure browser (optional)

Edit `config.py` to change browser or run headless:

```python
BROWSER   = "chrome"   # or "firefox" or "edge"
HEADLESS  = False       # True = no browser window (CI/CD mode)
```

---

## ▶️ Running the Tests

### Run all tests
```bash
pytest
```

### Run only positive tests
```bash
pytest -m positive
```

### Run only negative tests
```bash
pytest -m negative
```

### Run only smoke tests
```bash
pytest -m smoke
```

### Run a specific test by name
```bash
pytest tests/test_login.py::TestLoginPositive::test_TC_LOGIN_POS_001_valid_credentials
```

### Run with verbose output
```bash
pytest -v
```

### Run headless (no browser window)
Change `HEADLESS = True` in `config.py`, then run normally.

---

## 📊 HTML Test Report

After running, an HTML report is auto-generated at:

```
reports/test_report.html
```

Open it in any browser to see a detailed breakdown of all test results, including pass/fail status, duration, and error messages.

---

## 🛠️ Tech Stack

| Tool              | Purpose                                |
|-------------------|----------------------------------------|
| Python 3.10+      | Programming language                   |
| Selenium 4        | Browser automation                     |
| Pytest            | Test framework and runner              |
| pytest-html       | HTML test report generation            |
| webdriver-manager | Auto-download browser drivers          |
| Page Object Model | Design pattern for maintainability     |

---

## 📌 Notes

- Tests use `pytest.xfail` for known bugs (e.g., modal field persistence on Safari) so they are documented without blocking the suite.
- The suite is designed to be run locally or in CI/CD pipelines.
- Changing `HEADLESS = True` is recommended for CI environments.

---

*Prepared as part of SQA Internship Task-03 at Prodigy InfoTech.*
