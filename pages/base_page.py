from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_page(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.driver.find_element(locator)

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click

    def enter_text(self, locator, text):
        element = self.driver.find_element(locator)
        element.clear()
        element.send_keys(text)

    def select_from_dropdown(self, locator, text):
        select_element = self.driver.find_element(locator)
        select = Select(select_element)
        select.select_by_visible_text(text)