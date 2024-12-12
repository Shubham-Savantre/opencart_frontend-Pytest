from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RegisterPage(BasePage):

    first_name_locator = (By.ID, "input-firstname")
    last_name_locator = (By.ID, "input-lastname")
    email_locator = (By.ID, "input-email")
    password_locator = (By.ID, "input-password")
    privacy_locator = (By.NAME, "agree")
    continue_locator = (By.XPATH, "//button[@class='btn btn-primary']")
    my_account_locator = (By.XPATH, "//span[normalize-space()='My Account']")
    logout_locator = (By.XPATH, "//a[@class='dropdown-item'][normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver= driver

    def enter_first_name(self, first_name):
        self.enter_text(self.first_name_locator, first_name)

    def enter_last_name(self, last_name):
        self.enter_text(self.last_name_locator, last_name)

    def enter_email(self, emailID):
        self.enter_text(self.email_locator, emailID)

    def enter_password(self, password):
        self.enter_text(self.password_locator, password)

    def click_accept_policy(self):
        self.click_element(self.privacy_locator)

    def click_continue_button(self):
        self.click_element(self.continue_locator)

    def click_my_account(self):
        self.click_element(self.my_account)

    def select_logout(self):
        self.click_element(self.logout_locator)