from ui.pages.base_page import BasePage
from ui.locators import cart_locators as locators
from ui.utils.locator_handler import locator_handler


class CartPage(BasePage):
    """This class represents the cart page"""
    def __init__(self, driver):
        super().__init__(driver)

    def get_added_product(self, index='1'):
        """Returns the web element and its text"""
        added_product_element = self.get_element(locator_handler(locators.PRODUCT_NAME, index))
        added_product_text = self.get_text(locator_handler(locators.PRODUCT_NAME, index))
        return added_product_element, added_product_text

    def click_remove_button(self, index='1'):
        """Clicks the remove button of the element according to the index"""
        self.click_on(locator_handler(locators.REMOVE_BUTTON, index))
