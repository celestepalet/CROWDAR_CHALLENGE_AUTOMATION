from ui.pages.login_page import LoginPage
from ui.utils.constants import BASE_URL
from ui.pages.products_page import ProductsPage
from ui.pages.cart_page import CartPage
import pytest


@pytest.mark.add_to_cart
@pytest.mark.gui_testing
@pytest.mark.TC_2_1
def test_add_single_product_to_cart(browser):
    """Verifies that a user can successfully add a single product to the shopping cart from
    the Products page"""
    # Precondition: Login with valid credentials
    products_page = ProductsPage(browser)
    products_page.navigate_to(BASE_URL)
    LoginPage(browser).log_in()
    # Precondition: Ensure cart is empty
    products_page.reset_cart()
    # Click on "Add to cart" button of any product
    products_page.click_add_button()
    product_name = products_page.get_product_name()
    # Click on cart icon
    products_page.click_cart_button()
    # Cart page should be displayed with the product added
    expected_url = "https://www.saucedemo.com/cart.html"
    expected_page_title = "Swag Labs"
    actual_url = browser.current_url
    actual_title = browser.title
    assert actual_url == expected_url, f"Actual URL ({actual_url})  does not match the " \
                                       f"expected url({expected_url})"
    assert actual_title == expected_page_title, f"Actual title ({actual_title}) does not match " \
                                                f"the expected title ({expected_page_title})"
    cart_page = CartPage(browser)
    product_added_element = cart_page.get_added_product()[0]
    product_added_name = cart_page.get_added_product()[1]
    assert product_added_element.is_displayed(), "Added product is not displayed."
    assert product_added_name == product_name, f"Product name displayed ({product_added_name}) does not " \
                                               f".match with the added({product_name})"
    # Teardown
    cart_page.click_remove_button()
    ProductsPage(browser).log_out()


# This test fails because I am assuming that instead of the number "1" the cart icon shows the text "UNO"
@pytest.mark.add_to_cart
@pytest.mark.TC_2_4
@pytest.mark.gui_testing
@pytest.mark.falling
def test_cart_icon_counter_initialize(browser):
    """Verifies that the cart icon displays a counter when the user adds the first product"""
    # Precondition: Login with valid credentials
    products_page = ProductsPage(browser)
    products_page.navigate_to(BASE_URL)
    LoginPage(browser).log_in()
    # Precondition: Ensure cart is empty
    products_page.reset_cart()
    # Click on "Add to cart" button of any product
    products_page.click_add_button()
    # A counter with the number 1 should be displayed in the cart icon
    expected_counter_number = 'UNO'
    counter_element = products_page.get_cart_counter()[0]
    actual_counter_number = products_page.get_cart_counter()[1]
    assert counter_element.is_displayed(), "Products counter is not displayed."
    assert actual_counter_number == expected_counter_number, f"Counter number ({actual_counter_number}) " \
                                                             f"does not match with the expected" \
                                                             f"({expected_counter_number})"
    # Teardown
    products_page.reset_cart()
    ProductsPage(browser).log_out()
