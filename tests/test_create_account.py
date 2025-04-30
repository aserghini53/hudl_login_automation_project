import pytest
import logging

from pages.login_page import LoginPage
from pages.create_account_page import CreateAccountPage
from test_data.constants import TestData

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class TestAccountCreation:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.login = LoginPage(driver)
        self.create_account = CreateAccountPage(driver)
        logging.info("Opening login page")
        self.login.open(TestData.URL)

    def test_check_create_account_page_displayed_from_enter_email_step(self,driver):
        """
        Test create account page is correctly displayed
        Steps:
        1. Open login page
        2. check Page elements: logo, page title, Privacy Policy and Terms of Service
        3. Click on create account
        4. Check create account elements
        """
        try:
            logging.info("Checking login page elements")
            self.login.check_login_page_elements_present()
            logging.info("Click on Create account")
            self.login.click_create_account()
            logging.info("Checking Create account elements")
            self.create_account.check_create_account_page_elements_present()
        except Exception as e:
            logging.exception(f"Create Account Page not displayed correctly: {e}")
            pytest.fail(f"Create Account Page not displayed correctly: {e}")

    def test_check_create_account_page_displayed_from_enter_password_step(self,driver):
        """
        Test create account page is correctly displayed
        Steps:
        1. Open login page
        2. check Page elements: logo, page title, Privacy Policy and Terms of Service
        3. Enter valid user email
        4. Continue to password
        5. Click on create account
        6. Check create account elements
        """
        try:
            logging.info("Checking login page elements")
            self.login.check_login_page_elements_present()
            logging.info("Entering user email")
            self.login.enter_email(TestData.USER_EMAIL)
            logging.info("Click on continue")
            self.login.click_continue_to_password()
            logging.info("Click on Create account")
            self.login.click_create_account()
            logging.info("Checking Create account elements")
            self.create_account.check_create_account_page_elements_present()
        except Exception as e:
            logging.exception(f"Create Account Page not displayed correctly: {e}")
            pytest.fail(f"Create Account Page not displayed correctly: {e}")