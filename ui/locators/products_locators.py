from selenium.webdriver.common.by import By


MENU_BUTTON = (By.ID, "react-burger-menu-btn")
LOGOUT_OPTION = (By.ID, "logout_sidebar_link")
RESET_OPTION = (By.ID, "reset_sidebar_link")
ADD_TO_CAR_BUTTON = "(//button[contains(@id,'add-to-cart')])"
CART_BUTTON = (By.ID, "shopping_cart_container")
PRODUCT_NAME = "(//div[@class='inventory_item_name '])"
CART_COUNTER = (By.XPATH, "//span[@class='shopping_cart_badge']")
REMOVE_BUTTON = "(//button[contains(@id,'remove')])"
X_BUTTON = (By.ID, "react-burger-cross-btn")
