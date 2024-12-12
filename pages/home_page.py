from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):

    my_account = (By.XPATH, "//a[@class='dropdown-toggle show']//i[@class='fa-solid fa-caret-down']")


    def __init__(self, driver):
        self.driver = driver

    def click_my_account(self):
        self.click_element(self.my_account)

    def select_register_from_dropdown(self, text):
        self.driver.select_from_dropdown(text)