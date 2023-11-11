from ui.pages.login_page import LoginPage
from ui.utils.constants import BASE_URL, VALID_USERNAME, VALID_PASSWORD, LOCKED_USERNAME
from ui.pages.products_page import ProductsPage
import pytest


@pytest.mark.login
@pytest.mark.TC_1_1
@pytest.mark.gui_testing
def test_login_with_valid_credentials(browser):
    """Verifies that a user can successfully log in to the system using valid credentials"""
    # Navigate to Log in url
    login_page = LoginPage(browser)
    login_page.navigate_to(BASE_URL)
    # Enter the valid username
    login_page.enter_username(VALID_USERNAME)
    # Enter the valid password
    login_page.enter_password(VALID_PASSWORD)
    # Click the "Login" button
    login_page.click_login()
    # Products page should be displayed
    expected_url = "https://www.saucedemo.com/inventory.html"
    expected_page_title = "Swag Labs"
    actual_url = browser.current_url
    actual_title = browser.title
    assert actual_url == expected_url, f"Actual URL ({actual_url})  does not match the " \
                                       f"expected url({expected_url})"
    assert actual_title == expected_page_title, f"Actual title ({actual_title}) does not match " \
                                                f"the expected title ({expected_page_title})"
    # Teardown
    ProductsPage(browser).log_out()


@pytest.mark.login
@pytest.mark.TC_1_3
@pytest.mark.gui_testing
def test_login_with_locked_username(browser):
    """Verifies that a user can successfully log in to the system using valid credentials"""
    # Navigate to Log in url
    login_page = LoginPage(browser)
    login_page.navigate_to(BASE_URL)
    # Enter the locked username
    login_page.enter_username(LOCKED_USERNAME)
    # Enter the valid password
    login_page.enter_password(VALID_PASSWORD)
    # Click the "Login" button
    login_page.click_login()
    # Log in page should still be displayed
    expected_url = "https://www.saucedemo.com/"
    expected_page_title = "Swag Labs"
    actual_url = browser.current_url
    actual_title = browser.title
    assert actual_url == expected_url, f"Actual URL ({actual_url})  does not match the " \
                                       f"expected url({expected_url})"
    assert actual_title == expected_page_title, f"Actual title ({actual_title}) does not match " \
                                                f"the expected title ({expected_page_title})"
    # Error message should be displayed
    error_element = login_page.get_error_message()[0]
    actual_message = login_page.get_error_message()[1]
    expected_message = "Epic sadface: Sorry, this user has been locked out."
    assert error_element.is_displayed(), "Error message is not displayed."
    assert actual_message == expected_message, f"Actual error message ({actual_message}) does not " \
                                               f".match the expected message({expected_message})"
