from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage():
    """Holds all common functionalities and provides a wrapper for selenium functions"""

    def __init__(self, driver):
        self.driver = driver

    def click_on(self, by_locator):
        """Waits for the element to be visible and click on it"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def enter_text(self, by_locator, text):
        """Waits for the element to be visible and enter text"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def navigate_to(self, url):
        """Navigates in the browser to the specified url"""
        self.driver.get(url)

    def get_element(self, by_locator):
        """Waits for the element for verify if is displayed"""
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    def get_text(self, by_locator):
        """Waits for the element to be visible and returns the text on it"""
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text
