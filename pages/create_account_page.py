from selenium.webdriver.common.by import By
from locators.create_account_page import CreateAccountPageLocators
from pages.base_page import BasePage
from test_data.constants import TestData

class CreateAccountPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def check_create_account_page_elements_present(self):
        self.is_visible(by_locator=(By.ID, CreateAccountPageLocators.LOGO))
        self.is_visible(by_locator=(By.XPATH, CreateAccountPageLocators.PAGE_TITLE))
        self.is_visible(by_locator=(By.ID, CreateAccountPageLocators.FIRST_NAME_INPUT))
        self.is_visible(by_locator=(By.ID, CreateAccountPageLocators.LAST_NAME_INPUT))
        self.is_visible(by_locator=(By.ID, CreateAccountPageLocators.EMAIL_INPUT))

    #this class should contain the test account creation workflow
