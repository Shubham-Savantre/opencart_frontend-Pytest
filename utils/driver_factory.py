from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory:
    @staticmethod
    def get_driver():
        # Create options for the Firefox WebDriver
        options = Options()

        options.set_preference("dom.webdriver.enabled", False)  # Bypass bot detection
        options.set_preference("useAutomationExtension", False)  # Disable automation extension

        options.add_argument("--start-maximized")  # Start the browser maximized
        options.add_argument("--disable-notifications")  # Disable notifications
        # options.add_argument("--private")  # Use private browsing mode (if needed)
        options.add_argument("--lang=en-US")  # Set browser language to English (optional)

        # Make the browser headless
        options.add_argument("--headless")

        # Initialize Firefox WebDriver with the options
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

        # Note: You don't need to maximize the window in headless mode, but if needed, you can do so
        # driver.maximize_window()  # Optional: maximize the browser window

        return driver
