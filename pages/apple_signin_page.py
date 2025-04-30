from selenium.webdriver.common.by import By
from locators.apple_signin_page_locators import AppleSignInPageLocators
from pages.base_page import BasePage


class AppleSignInPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def check_redirect_to_apple_signin_page(self):
        self.is_visible(by_locator=(By.XPATH, AppleSignInPageLocators.APPLE_LOGO))
        self.is_visible(by_locator=(By.CSS_SELECTOR, AppleSignInPageLocators.APPLE_USERNAME_INPUT))