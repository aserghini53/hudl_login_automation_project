from selenium.webdriver.common.by import By
from locators.google_signin_page_locators import GoogleSignInPageLocators
from pages.base_page import BasePage


class GoogleSignInPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def check_redirect_to_google_signin_page(self):
        self.is_visible(by_locator=(By.XPATH, GoogleSignInPageLocators.SIGNIN_WITH_GOOGLE_TITLE))
        self.is_visible(by_locator=(By.ID, GoogleSignInPageLocators.USERNAME_INPUT))

