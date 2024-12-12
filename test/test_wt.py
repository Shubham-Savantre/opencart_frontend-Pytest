import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.register_page import RegisterPage
from utils.config import *
from utils.driver_factory import DriverFactory

@pytest.fixture
def setup():
    driver = DriverFactory.get_driver()
    yield driver
    driver.quit()


def test_walkthrough(setup):
    driver = setup
    reg_page = RegisterPage(driver)
    reg_page.open_page(BASE_URL)
    reg_page.enter_first_name(FIRST_NAME)
    reg_page.enter_last_name(LAST_NAME)
    reg_page.enter_email(EMAIL)
    reg_page.enter_password(PASSWORD)
    reg_page.click_accept_policy()
    reg_page.click_continue_button()

    success_message_locator = (By.XPATH, "//h1[normalize-space()='Your Account Has Been Created!']")
    success_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located(success_message_locator)).text

    assert "Your Account Has Been Created!" in success_message