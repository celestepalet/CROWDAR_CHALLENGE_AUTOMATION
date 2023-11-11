from ui.pages.base_page import BasePage
from ui.locators import login_locators as locators
from ui.utils.constants import VALID_USERNAME, VALID_PASSWORD


class LoginPage(BasePage):
    """This class represents the login page"""
    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username: str):
        """Enters the text received in the username input"""
        self.enter_text(locators.USERNAME_INPUT, username)

    def enter_password(self, password: str):
        """Enters the text received in the password input"""
        self.enter_text(locators.PASSWORDS_INPUT, password)

    def click_login(self):
        """Clicks the login button in the login page"""
        self.click_on(locators.LOGIN_BUTTON)

    def get_error_message(self):
        """Returns the web element and its text"""
        error_message_element = self.get_element(locators.ERROR_MESSAGE)
        error_message_text = self.get_text(locators.ERROR_MESSAGE)
        return error_message_element, error_message_text

    def log_in(self):
        """Performs the logout process"""
        self.enter_username(VALID_USERNAME)
        self.enter_password(VALID_PASSWORD)
        self.click_login()
