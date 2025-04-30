from selenium.webdriver.common.by import By
from locators.facebook_signin_page_locators import FacebookSignInPageLocators
from pages.base_page import BasePage


class FacebookSignInPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def check_redirect_to_facebook_signin_page(self):
        self.is_visible(by_locator=(By.CSS_SELECTOR, FacebookSignInPageLocators.FACEBOOK_LOGO))
        self.is_visible(by_locator=(By.ID, FacebookSignInPageLocators.FACEBOOK_EMAIL_INPUT))
        self.is_visible(by_locator=(By.ID, FacebookSignInPageLocators.FACEBOOK_PASSWORD))
