"""
PRODIGY_ST_03 - Automated Login Test Suite
Target: https://www.saucedemo.com/
Author: Shihab157
Track: Software Testing (ST)
"""

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException, NoSuchElementException


# ─────────────────────────────────────────────
# Constants
# ─────────────────────────────────────────────
BASE_URL = "https://www.saucedemo.com/"
TIMEOUT = 10

# Credentials from SauceDemo documentation
VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"

LOCKED_USER = "locked_out_user"
PERFORMANCE_USER = "performance_glitch_user"

INVALID_USERNAME = "invalid_user_123"
INVALID_PASSWORD = "wrong_password_456"

# Selectors
USERNAME_FIELD = (By.ID, "user-name")
PASSWORD_FIELD = (By.ID, "password")
LOGIN_BUTTON   = (By.ID, "login-button")
ERROR_MSG      = (By.CSS_SELECTOR, "[data-test='error']")
INVENTORY_PAGE = (By.CLASS_NAME, "inventory_container")


# ─────────────────────────────────────────────
# Fixture
# ─────────────────────────────────────────────
@pytest.fixture(scope="function")
def driver():
    """Set up Chrome WebDriver in headless mode."""
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    driver.get(BASE_URL)
    yield driver
    driver.quit()


# ─────────────────────────────────────────────
# Helper
# ─────────────────────────────────────────────
def do_login(driver, username, password):
    """Fill and submit the login form."""
    wait = WebDriverWait(driver, TIMEOUT)
    wait.until(EC.presence_of_element_located(USERNAME_FIELD))

    user_field = driver.find_element(*USERNAME_FIELD)
    pass_field = driver.find_element(*PASSWORD_FIELD)

    user_field.clear()
    pass_field.clear()

    user_field.send_keys(username)
    pass_field.send_keys(password)
    driver.find_element(*LOGIN_BUTTON).click()
    time.sleep(1)


def get_error_message(driver):
    """Return error message text or empty string."""
    try:
        wait = WebDriverWait(driver, TIMEOUT)
        elem = wait.until(EC.presence_of_element_located(ERROR_MSG))
        return elem.text.strip()
    except TimeoutException:
        return ""


def is_logged_in(driver):
    """Check whether the inventory page is displayed."""
    try:
        WebDriverWait(driver, TIMEOUT).until(
            EC.presence_of_element_located(INVENTORY_PAGE)
        )
        return True
    except TimeoutException:
        return False


# ═════════════════════════════════════════════
# POSITIVE TEST CASES
# ═════════════════════════════════════════════

class TestPositiveLogin:
    """TC-P01 … TC-P03 – valid-credential scenarios."""

    def test_TC_P01_valid_standard_user(self, driver):
        """TC-P01: Standard user with correct credentials should reach inventory."""
        do_login(driver, VALID_USERNAME, VALID_PASSWORD)
        assert is_logged_in(driver), \
            "TC-P01 FAILED: Did not reach inventory page with valid credentials."
        assert "inventory" in driver.current_url, \
            "TC-P01 FAILED: URL does not contain 'inventory'."
        print("\n✅ TC-P01 PASSED: Standard user logged in successfully.")

    def test_TC_P02_page_title_after_login(self, driver):
        """TC-P02: After login the page title should be 'Swag Labs'."""
        do_login(driver, VALID_USERNAME, VALID_PASSWORD)
        assert is_logged_in(driver), "TC-P02 PRE-CONDITION: Login must succeed."
        assert driver.title == "Swag Labs", \
            f"TC-P02 FAILED: Expected title 'Swag Labs', got '{driver.title}'."
        print("\n✅ TC-P02 PASSED: Page title is correct after login.")

    def test_TC_P03_performance_glitch_user(self, driver):
        """TC-P03: Performance-glitch user should also reach inventory (slower)."""
        do_login(driver, PERFORMANCE_USER, VALID_PASSWORD)
        # Give extra time for slow user
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(INVENTORY_PAGE)
            )
            logged_in = True
        except TimeoutException:
            logged_in = False
        assert logged_in, \
            "TC-P03 FAILED: Performance glitch user did not reach inventory."
        print("\n✅ TC-P03 PASSED: Performance glitch user logged in successfully.")


# ═════════════════════════════════════════════
# NEGATIVE TEST CASES
# ═════════════════════════════════════════════

class TestNegativeLogin:
    """TC-N01 … TC-N08 – invalid / edge-case scenarios."""

    def test_TC_N01_invalid_username_and_password(self, driver):
        """TC-N01: Completely wrong credentials should show an error."""
        do_login(driver, INVALID_USERNAME, INVALID_PASSWORD)
        error = get_error_message(driver)
        assert error != "", \
            "TC-N01 FAILED: No error message shown for invalid credentials."
        assert not is_logged_in(driver), \
            "TC-N01 FAILED: User was logged in with invalid credentials!"
        print(f"\n✅ TC-N01 PASSED: Error shown → '{error}'")

    def test_TC_N02_valid_username_wrong_password(self, driver):
        """TC-N02: Correct username but wrong password should show an error."""
        do_login(driver, VALID_USERNAME, "wrong_password_!!!")
        error = get_error_message(driver)
        assert error != "", \
            "TC-N02 FAILED: No error message for wrong password."
        assert not is_logged_in(driver), \
            "TC-N02 FAILED: User logged in with wrong password!"
        print(f"\n✅ TC-N02 PASSED: Error shown → '{error}'")

    def test_TC_N03_wrong_username_valid_password(self, driver):
        """TC-N03: Wrong username but correct password should show an error."""
        do_login(driver, "unknown_user_xyz", VALID_PASSWORD)
        error = get_error_message(driver)
        assert error != "", \
            "TC-N03 FAILED: No error message for wrong username."
        assert not is_logged_in(driver), \
            "TC-N03 FAILED: User logged in with wrong username!"
        print(f"\n✅ TC-N03 PASSED: Error shown → '{error}'")

    def test_TC_N04_empty_username(self, driver):
        """TC-N04: Empty username field should show an error."""
        do_login(driver, "", VALID_PASSWORD)
        error = get_error_message(driver)
        assert error != "", \
            "TC-N04 FAILED: No error message for empty username."
        assert "Username is required" in error, \
            f"TC-N04 FAILED: Unexpected error text: '{error}'"
        print(f"\n✅ TC-N04 PASSED: Error shown → '{error}'")

    def test_TC_N05_empty_password(self, driver):
        """TC-N05: Empty password field should show an error."""
        do_login(driver, VALID_USERNAME, "")
        error = get_error_message(driver)
        assert error != "", \
            "TC-N05 FAILED: No error message for empty password."
        assert "Password is required" in error, \
            f"TC-N05 FAILED: Unexpected error text: '{error}'"
        print(f"\n✅ TC-N05 PASSED: Error shown → '{error}'")

    def test_TC_N06_both_fields_empty(self, driver):
        """TC-N06: Both fields empty should show a validation error."""
        do_login(driver, "", "")
        error = get_error_message(driver)
        assert error != "", \
            "TC-N06 FAILED: No error message when both fields are empty."
        print(f"\n✅ TC-N06 PASSED: Error shown → '{error}'")

    def test_TC_N07_locked_out_user(self, driver):
        """TC-N07: Locked-out user should receive an account-locked error."""
        do_login(driver, LOCKED_USER, VALID_PASSWORD)
        error = get_error_message(driver)
        assert error != "", \
            "TC-N07 FAILED: No error message for locked-out user."
        assert "locked out" in error.lower(), \
            f"TC-N07 FAILED: Expected 'locked out' in error, got: '{error}'"
        assert not is_logged_in(driver), \
            "TC-N07 FAILED: Locked-out user was able to log in!"
        print(f"\n✅ TC-N07 PASSED: Error shown → '{error}'")

    def test_TC_N08_sql_injection_attempt(self, driver):
        """TC-N08: SQL injection payload should not bypass authentication."""
        do_login(driver, "' OR '1'='1", "' OR '1'='1")
        assert not is_logged_in(driver), \
            "TC-N08 FAILED: SQL injection bypassed login! Critical vulnerability."
        print("\n✅ TC-N08 PASSED: SQL injection attempt correctly rejected.")

    def test_TC_N09_whitespace_only_credentials(self, driver):
        """TC-N09: Whitespace-only credentials should not log the user in."""
        do_login(driver, "   ", "   ")
        assert not is_logged_in(driver), \
            "TC-N09 FAILED: Whitespace-only input bypassed login."
        print("\n✅ TC-N09 PASSED: Whitespace-only credentials correctly rejected.")
