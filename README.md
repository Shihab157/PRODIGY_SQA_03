# PRODIGY_ST_03 — Automated Login Test Suite

> **Prodigy InfoTech Software Testing Internship | Task 03**
> **Author:** Shihab157
> **Target:** [SauceDemo](https://www.saucedemo.com/)

---

## 📋 Task Overview

Write a test suite that automates testing of **login functionality** on a web application. The suite must include:

- ✅ **Positive test cases** — valid credentials that should succeed
- ❌ **Negative test cases** — invalid credentials, empty fields, locked accounts, injection attempts

---

## 🧪 Test Cases

### Positive Cases (3)

| ID     | Description                                | Expected Result          |
|--------|--------------------------------------------|--------------------------|
| TC-P01 | Standard user with valid credentials       | Redirected to inventory  |
| TC-P02 | Page title after successful login          | Title = "Swag Labs"      |
| TC-P03 | Performance glitch user (valid password)   | Redirected to inventory  |

### Negative Cases (9)

| ID     | Description                                | Expected Result          |
|--------|--------------------------------------------|--------------------------|
| TC-N01 | Invalid username AND invalid password      | Error message shown      |
| TC-N02 | Valid username, wrong password             | Error message shown      |
| TC-N03 | Wrong username, valid password             | Error message shown      |
| TC-N04 | Empty username field                       | "Username is required"   |
| TC-N05 | Empty password field                       | "Password is required"   |
| TC-N06 | Both fields empty                          | Error message shown      |
| TC-N07 | Locked-out user account                   | "locked out" error       |
| TC-N08 | SQL injection attempt                      | Login blocked            |
| TC-N09 | Whitespace-only credentials               | Login blocked            |

---

## 🛠️ Tech Stack

| Tool              | Purpose                        |
|-------------------|--------------------------------|
| Python 3.10+      | Programming language           |
| Selenium 4.x      | Browser automation             |
| pytest            | Test framework & runner        |
| pytest-html       | HTML test reports              |
| Google Chrome     | Browser (headless mode)        |

---

## 🚀 Setup & Run

### 1. Clone the repository

```bash
git clone https://github.com/Shihab157/PRODIGY_ST_03.git
cd PRODIGY_ST_03
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> **Note:** ChromeDriver must match your installed Chrome version.  
> Download from: https://chromedriver.chromium.org/downloads  
> Or use `webdriver-manager` (already in requirements).

### 4. Run the full test suite

```bash
pytest
```

### 5. View the HTML report

After running, open `reports/test_report.html` in your browser.

---

## 📁 Project Structure

```
PRODIGY_ST_03/
├── tests/
│   └── test_login.py       # All test cases (positive + negative)
├── reports/
│   └── test_report.html    # Generated after running pytest
├── screenshots/            # Optional: save screenshots on failure
├── pytest.ini              # pytest configuration
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## 🔐 Test Credentials (SauceDemo)

| Username                | Password       | Type          |
|-------------------------|----------------|---------------|
| `standard_user`         | `secret_sauce` | Valid user    |
| `performance_glitch_user` | `secret_sauce` | Valid (slow) |
| `locked_out_user`       | `secret_sauce` | Locked        |

---

## 📸 Sample Output

```
tests/test_login.py::TestPositiveLogin::test_TC_P01_valid_standard_user PASSED
tests/test_login.py::TestPositiveLogin::test_TC_P02_page_title_after_login PASSED
tests/test_login.py::TestPositiveLogin::test_TC_P03_performance_glitch_user PASSED
tests/test_login.py::TestNegativeLogin::test_TC_N01_invalid_username_and_password PASSED
tests/test_login.py::TestNegativeLogin::test_TC_N02_valid_username_wrong_password PASSED
tests/test_login.py::TestNegativeLogin::test_TC_N03_wrong_username_valid_password PASSED
tests/test_login.py::TestNegativeLogin::test_TC_N04_empty_username PASSED
tests/test_login.py::TestNegativeLogin::test_TC_N05_empty_password PASSED
tests/test_login.py::TestNegativeLogin::test_TC_N06_both_fields_empty PASSED
tests/test_login.py::TestNegativeLogin::test_TC_N07_locked_out_user PASSED
tests/test_login.py::TestNegativeLogin::test_TC_N08_sql_injection_attempt PASSED
tests/test_login.py::TestNegativeLogin::test_TC_N09_whitespace_only_credentials PASSED

12 passed in 45.67s
```

---

## 📄 License

This project is part of the Prodigy InfoTech Internship program.
