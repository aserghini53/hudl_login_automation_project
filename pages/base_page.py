# pages/base_page.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 30)

	def open (self, url):
		self.driver.get(url)

	def click (self, by_locator):
		element = self.wait.until(EC.element_to_be_clickable(by_locator))	
		element.click()

	def enter_text(self, by_locator, text):
		element = self.wait.until(EC.visibility_of_element_located(by_locator))
		element.clear()
		element.send_keys(text)

	def is_visible(self, by_locator):
		element = self.wait.until(EC.visibility_of_element_located(by_locator))
		return bool(element)

	def get_element_text(self, by_locator):
		element = self.wait.until(EC.visibility_of_element_located(by_locator))
		return element.text

	def hover_element(self, by_locator):
		element = self.wait.until(EC.visibility_of_element_located(by_locator))
		ActionChains(self.driver).move_to_element(element).perform()
