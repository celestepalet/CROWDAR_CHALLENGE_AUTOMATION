from ui.pages.base_page import BasePage
from ui.locators import products_locators as locators
from ui.utils.locator_handler import locator_handler


class ProductsPage(BasePage):
    """This class represents the products page"""
    def __init__(self, driver):
        super().__init__(driver)

    def click_add_button(self, index='1'):
        """Clicks the add to cart button of the element according to the index"""
        self.click_on(locator_handler(locators.ADD_TO_CAR_BUTTON, index))

    def click_menu_button(self):
        """Clicks the hamburger menu button"""
        self.click_on(locators.MENU_BUTTON)

    def click_logout_option(self):
        """Clicks the logout option in the menu"""
        self.click_on(locators.LOGOUT_OPTION)

    def click_reset_option(self):
        """Clicks the reset option in the menu"""
        self.click_on(locators.RESET_OPTION)

    def click_cart_button(self):
        """Clicks the cart icon"""
        self.click_on(locators.CART_BUTTON)

    def click_remove_button(self, index='1'):
        """Clicks the remove button of the element according to the index"""
        self.click_on(locator_handler(locators.REMOVE_BUTTON, index))

    def get_cart_counter(self):
        """Returns the web element and its text"""
        counter_element = self.get_element(locators.CART_COUNTER)
        counter_text = self.get_text(locators.CART_COUNTER)
        return counter_element, counter_text

    def get_product_name(self, index='1'):
        """Returns the name of the product according to the index"""
        return self.get_text(locator_handler(locators.PRODUCT_NAME, index))

    def click_x_menu_button(self):
        """Clicks the x button in the menu"""
        self.click_on(locators.X_BUTTON)

    def log_out(self):
        """Performs the login process"""
        self.click_menu_button()
        self.click_logout_option()

    def reset_cart(self):
        """Performs the reset app state process"""
        self.click_menu_button()
        self.click_reset_option()
        self.click_x_menu_button()
