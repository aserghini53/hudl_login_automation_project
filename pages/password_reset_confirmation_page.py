
from selenium.webdriver.common.by import By
from locators.password_reset_confirmation_page_locators import PasswordResetConfirmationPageLocators
from pages.base_page import BasePage
from test_data.constants import TestData

class PasswordResetConfirmationPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def check_password_reset_confirmation_message(self):
        self.is_visible(by_locator=(By.XPATH, PasswordResetConfirmationPageLocators.RESET_PASSWORD_CONFIRMATION_MESSAGE))
