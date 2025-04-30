import pytest
import logging
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.google_signin_page import GoogleSignInPage
from pages.facebook_signin_page import FacebookSignInPage
from pages.apple_signin_page import AppleSignInPage
from test_data.constants import TestData

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class TestLogin:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.login = LoginPage(driver)
        logging.info("Opening login page")
        self.login.open(TestData.URL)
        self.home = HomePage(driver)
        self.google_signin = GoogleSignInPage(driver)
        self.facebook_signin = FacebookSignInPage(driver)
        self.apple_signin = AppleSignInPage(driver)

    def test_login_with_valid_email_and_password(self,driver):
        """
        Test successful login with valid email and password
        Steps:
        1. Open login page
        2. check Page elements: logo, page title, Privacy Policy and Terms of Service
        3. Enter valid user email
        4. Continue to password
        5. Enter valid password
        6. Complete login
        7. Check home page elements
        8. logout
        """
        try:
            logging.info("Checking login page elements")
            self.login.check_login_page_elements_present()
            logging.info("Entering user email")
            self.login.enter_email(TestData.USER_EMAIL)
            logging.info("Click on continue")
            self.login.click_continue_to_password()
            logging.info("Check that email was entered correctly")
            self.login.check_email_content(TestData.USER_EMAIL)
            logging.info("Entering user password")
            self.login.enter_password(TestData.USER_PASSWORD)
            logging.info("Click on continue")
            self.login.click_continue_to_login()
            logging.info("Check home page elements")
            self.home.check_home_page_elements_present()
        except Exception as e:
            logging.exception(f"Login failed: {e}")
            driver.save_screenshot("screenshots/test_login_with_valid_email_and_password.png")
            pytest.fail(f"Login failed: {e}")

        logging.info("Logging out")
        self.home.logout()



    def test_login_with_invalid_email_format(self,driver):
        """ Test invalid login with invalid email and password
        Steps:
        1. Open login page
        2. check Page elements: logo, page title, Privacy Policy and Terms of Service
        3. Enter invalid email format (not respecting the email format)
        4. Continue to password
        5. Check error message
        """
        logging.info("Checking login page elements")
        self.login.check_login_page_elements_present()
        logging.info("Entering user email")
        self.login.enter_email(TestData.INVALID_EMAIL_FORMAT)
        logging.info("Click on continue")
        self.login.click_continue_to_password()
        logging.info("Checking error message")
        self.login.check_invalid_email_error_message()

    def test_edit_email (self,driver):
        """ Test edit email
        Steps:
        1. Open login page
        2. check Page elements: logo, page title, Privacy Policy and Terms of Service
        3. Enter valid user email
        4. Continue to password
        5. Click Edit email
        6. Enter a new valid user email
        7. Continue to password
        8. Check that email was correctly edited
        9. Enter valid password
        10. Complete login
        11. Check home page elements
        12. logout
        """
        logging.info("Checking login page elements")
        self.login.check_login_page_elements_present()
        logging.info("Entering user email")
        self.login.enter_email(TestData.INCORRECT_EMAIL)
        logging.info("Click on continue")
        self.login.click_continue_to_password()
        logging.info("Click on edit email")
        self.login.click_edit_email()
        logging.info("Entering user email")
        self.login.enter_email(TestData.USER_EMAIL)
        logging.info("Click on continue")
        self.login.click_continue_to_password()
        logging.info("Check that email was entered correctly")
        self.login.check_email_content(TestData.USER_EMAIL)
        logging.info("Entering user password")
        self.login.enter_password(TestData.USER_PASSWORD)
        logging.info("Click on continue")
        self.login.click_continue_to_login()
        logging.info("Check home page elements")
        self.home.check_home_page_elements_present()
        logging.info("Logging out")
        self.home.logout()

    def test_login_with_invalid_credentials (self,driver):
        """ Test invalid login with invalid email and password
         Steps:
          1. Open login page
          2. check Page elements: logo, page title, Privacy Policy and Terms of Service
          3. Enter an incorrect email (valid format)
          4. Continue to password
          5. Enter an incorrect password
          6. Complete login
          7. Check error message
         """
        logging.info("Checking login page elements")
        self.login.check_login_page_elements_present()
        logging.info("Entering user email")
        self.login.enter_email(TestData.INCORRECT_EMAIL)
        logging.info("Click on continue")
        self.login.click_continue_to_password()
        logging.info("Check that email was entered correctly")
        self.login.check_email_content(TestData.INCORRECT_EMAIL)
        logging.info("Entering user password")
        self.login.enter_password(TestData.INCORRECT_PASSWORD)
        logging.info("Click on continue")
        self.login.click_continue_to_login()
        logging.info("Checking error message")
        self.login.check_invalid_email_or_password_error_message()

    def test_google_login_button_redirects_to_google_auth(self,driver):
        """ Test the Google authentication redirect page
              Steps:
               1. Open login page
               2. Check Page elements: logo, page title, Privacy Policy and Terms of Service
               3. Click on Google authentication link Open login page
               4. Check Google Signin Page elements
              """
        logging.info("Checking login page elements")
        self.login.check_login_page_elements_present()
        logging.info("Click on Google Authent")
        self.login.click_google_auth_button()
        logging.info("Checking Google Singin page elements")
        self.google_signin.check_redirect_to_google_signin_page()

    def test_facebook_login_button_redirects_to_facebook_auth(self,driver):
        """ Test the Facebook authentication redirect page
                Steps:
                1. Open login page
                2. Check Page elements: logo, page title, Privacy Policy and Terms of Service
                3. Click on Facebook authentication link Open login page
                4. Check Facebook Signin Page elements
                """
        logging.info("Checking login page elements")
        self.login.check_login_page_elements_present()
        logging.info("Click on Facebook Authent")
        self.login.click_facebook_auth_button()
        logging.info("Checking Facebook Singin page elements")
        self.facebook_signin.check_redirect_to_facebook_signin_page()

    def test_apple_login_button_redirects_to_apple_auth(self,driver):
        """ Test the Apple authentication redirect page
                Steps:
                1. Open login page
                2. Check Page elements: logo, page title, Privacy Policy and Terms of Service
                3. Click on Apple authentication link Open login page
                4. Check Apple Signin Page elements
                """
        logging.info("Checking login page elements")
        self.login.check_login_page_elements_present()
        logging.info("Click on Apple Authent")
        self.login.click_apple_auth_button()
        logging.info("Checking Apple Singin page elements")
        self.apple_signin.check_redirect_to_apple_signin_page()
