from selenium.webdriver.common.by import By
from locators.home_page_locators import HomePageLocators
from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage
from test_data.constants import TestData

class ResetPasswordPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def check_reset_password_logo_present(self):
        self.is_visible(by_locator=(By.ID, ResetPasswordPageLocators.PAGE_LOGO))

    def check_reset_password_page_title_present(self):
        self.is_visible(by_locator=(By.XPATH, ResetPasswordPageLocators.PAGE_TITLE))

    def check_reset_password_description_present(self):
        self.is_visible(by_locator=(By.ID, ResetPasswordPageLocators.PAGE_DESCRIPTION))

    def enter_email(self, email):
        self.enter_text((By.ID, ResetPasswordPageLocators.EMAIL_INPUT), email)

    def click_continue(self):
        self.click((By.XPATH, ResetPasswordPageLocators.CONTINUE_BUTTON))

    def click_go_back(self):
        self.click((By.XPATH, ResetPasswordPageLocators.GO_BACK_BUTTON))

    def check_invalid_email_error_message(self):
        locator = By.ID, ResetPasswordPageLocators.INVALID_EMAIL_ERROR_MESSAGE
        self.is_visible(by_locator=locator)
        error_message = self.get_element_text(locator)
        assert error_message == TestData.INVALID_EMAIL_ERROR_MESSAGE, \
            f"Expected error message: '{TestData.INVALID_EMAIL_ERROR_MESSAGE}', but got: '{error_message}'"

    def check_check_password_reset_page_elements_present(self):
        self.check_reset_password_page_title_present()
        self.check_reset_password_logo_present()
        self.check_reset_password_description_present()