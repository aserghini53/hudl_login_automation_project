# pages/login_page.py

from selenium.webdriver.common.by import By
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from test_data.constants import TestData

class LoginPage(BasePage):
	def __init__(self, driver):
		super().__init__(driver)

	def check_login_page_logo_present(self):
		self.is_visible(by_locator=(By.ID, LoginPageLocators.PAGE_LOGO))

	def check_login_page_title_present(self):
		self.is_visible(by_locator=(By.XPATH, LoginPageLocators.PAGE_LOGIN_TITLE))

	def enter_email(self, email):
		self.enter_text((By.ID, LoginPageLocators.EMAIL_INPUT), email)

	def click_continue_to_password(self):
		self.click((By.CSS_SELECTOR, LoginPageLocators.CONTINUE_TO_PASSWORD_BUTTON))

	def click_edit_email (self):
		self.click((By.CSS_SELECTOR, LoginPageLocators.EDIT_EMAIL))

	def check_email_content(self,mail):
		email_entered = self.get_element_text((By.CSS_SELECTOR, LoginPageLocators.EMAIL_INPUT_GREYED))
		assert email_entered == mail , \
			f"Expected error message: '{mail}', but got: '{email_entered}'"

	def click_google_auth_button(self):
		self.click((By.CSS_SELECTOR, LoginPageLocators.GOOGLE_AUTH_BUTTON))

	def click_facebook_auth_button(self):
		self.click((By.CSS_SELECTOR, LoginPageLocators.FACEBOOK_AUTH_BUTTON))

	def click_apple_auth_button(self):
		self.click((By.CSS_SELECTOR, LoginPageLocators.APPLE_AUTH_BUTTON))

	def enter_password(self, password):
		self.enter_text((By.ID, LoginPageLocators.PASSWORD_INPUT),password)

	def click_continue_to_login(self):
		self.click((By.CSS_SELECTOR, LoginPageLocators.CONTINUE_TO_LOGIN_BUTTON))

	def check_invalid_email_error_message(self):
		locator = By.ID, LoginPageLocators.INVALID_EMAIL_ERROR_MESSAGE
		self.is_visible(by_locator=locator)
		error_message = self.get_element_text(locator)
		assert error_message == TestData.INVALID_EMAIL_ERROR_MESSAGE , \
        f"Expected error message: '{TestData.INVALID_EMAIL_ERROR_MESSAGE}', but got: '{error_message}'"

	def check_invalid_email_or_password_error_message(self):
			locator = By.ID, LoginPageLocators.INVALID_EMAIL_OR_PASSWORD_ERROR_MESSAGE
			self.is_visible(by_locator=locator)
			error_message = self.get_element_text(locator)
			assert error_message == TestData.INVALID_EMAIL_OR_PASSWORD_ERROR_MESSAGE, \
				f"Expected error message: '{TestData.INVALID_EMAIL_ERROR_MESSAGE}', but got: '{error_message}'"

	def check_privacy_policy_link_present(self):
		self.is_visible(by_locator=(By.LINK_TEXT, LoginPageLocators.PRIVACY_POLICY_LINK))

	def check_terms_of_service_link_present(self):
		self.is_visible(by_locator=(By.LINK_TEXT, LoginPageLocators.TERMS_OF_SERVICE_LINK))

	def click_forget_password(self):
		self.click((By.LINK_TEXT, LoginPageLocators.FORGOT_PASSWORD_LINK))

	def click_create_account(self):
		self.click((By.LINK_TEXT, LoginPageLocators.CREATE_ACCOUNT_LINK))

	def check_login_page_elements_present(self):
		self.check_login_page_logo_present()
		self.check_login_page_title_present()
		self.check_privacy_policy_link_present()
		self.check_terms_of_service_link_present()
		# other elements check could be added (email, password inputs and google, apple and facebook auth etc.)

