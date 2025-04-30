import pytest
import logging

from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage
from pages.password_reset_confirmation_page import PasswordResetConfirmationPage
from test_data.constants import TestData

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class TestForgetPassword:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.login = LoginPage(driver)
        self.reset_password = ResetPasswordPage(driver)
        self.password_reset_confirmation = PasswordResetConfirmationPage(driver)
        logging.info("Opening login page")
        self.login.open(TestData.URL)

    def test_forget_password_with_valid_email(self,driver):
        """
        Test successful forget password
        Steps:
        1. Open login page
        2. check Page elements: logo, page title, Privacy Policy and Terms of Service
        3. Enter valid user email
        4. Continue to password
        5. Click on forgot password
        6. Check Reset Password page elements
        7. Enter valid email
        8. Click on Continue
        9. Check reset password confirmation
        """
        try:
            logging.info("Checking login page elements")
            self.login.check_login_page_elements_present()
            logging.info("Entering user email")
            self.login.enter_email(TestData.INCORRECT_EMAIL)
            logging.info("Click on continue")
            self.login.click_continue_to_password()
            logging.info("Click on Forgot Password")
            self.login.click_forget_password()
            logging.info("Check Reset Password page elements")
            self.reset_password.check_check_password_reset_page_elements_present()
            logging.info("Entering user email")
            self.reset_password.enter_email(TestData.INCORRECT_EMAIL)
            logging.info("Click on continue")
            self.reset_password.click_continue()
            logging.info("Check Password Reset message")
            self.password_reset_confirmation.check_password_reset_confirmation_message()
        except Exception as e:
            logging.exception(f"Reset Password failed: {e}")
            driver.save_screenshot("screenshots/test_forget_password_with_valid_email")
            pytest.fail(f"Reset password failed: {e}")

    def test_forget_password_with_invalid_email_format(self,driver):
        """
        Test invalid email format in forget password flow
        Steps:
        1. Open login page
        2. check Page elements: logo, page title, Privacy Policy and Terms of Service
        3. Enter valid user email
        4. Continue to password
        5. Click on forgot password
        6. Check Reset Password page elements
        7. Enter an invalid email format
        8. Click on Continue
        9. Check error message
        """

        logging.info("Checking login page elements")
        self.login.check_login_page_elements_present()
        logging.info("Entering user email")
        self.login.enter_email(TestData.INCORRECT_EMAIL)
        logging.info("Click on continue")
        self.login.click_continue_to_password()
        logging.info("Click on Forgot Password")
        self.login.click_forget_password()
        logging.info("Check Reset Password page elements")
        self.reset_password.check_check_password_reset_page_elements_present()
        logging.info("Entering invalid email format")
        self.reset_password.enter_email(TestData.INVALID_EMAIL_FORMAT)
        logging.info("Click on continue")
        self.reset_password.click_continue()
        logging.info("Check error message")
        self.reset_password.check_invalid_email_error_message()

    def test_forget_password_go_back_to_login_page(self):
        """
        Test return to login page from forget password page
        Steps:
        1. Open login page
        2. check Page elements: logo, page title, Privacy Policy and Terms of Service
        3. Enter valid user email
        4. Continue to password
        5. Click on forgot password
        6. Check Reset Password page elements
        7. Click on go back
        8. check Page elements: logo, page title, Privacy Policy and Terms of Service
        """
        logging.info("Checking login page elements")
        self.login.check_login_page_elements_present()
        logging.info("Entering user email")
        self.login.enter_email(TestData.INCORRECT_EMAIL)
        logging.info("Click on continue")
        self.login.click_continue_to_password()
        logging.info("Click on Forgot Password")
        self.login.click_forget_password()
        logging.info("Check Reset Password page elements")
        self.reset_password.check_check_password_reset_page_elements_present()
        logging.info("Click on go back")
        self.reset_password.click_go_back()
        logging.info("Check Page elements")
        self.login.check_login_page_elements_present()


