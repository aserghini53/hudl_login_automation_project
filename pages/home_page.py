
from selenium.webdriver.common.by import By
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
from test_data.constants import TestData

class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def check_home_page_logo_present(self):
        self.is_visible(by_locator=(By.CSS_SELECTOR, HomePageLocators.LOGO))

    def check_home_page_home_link_present(self):
        self.is_visible(by_locator=(By.XPATH, HomePageLocators.HOME_LINK))

    def check_home_search_bar_present(self):
        self.is_visible(by_locator=(By.CSS_SELECTOR, HomePageLocators.SEARCH_BAR))

    def check_home_page_elements_present(self):
        self.check_home_page_logo_present()
        self.check_home_page_home_link_present()
        self.check_home_search_bar_present()

    def logout(self):
        self.hover_element(by_locator=(By.CSS_SELECTOR, HomePageLocators.AVATAR))
        self.click(by_locator=(By.CSS_SELECTOR , HomePageLocators.LOGOUT))
