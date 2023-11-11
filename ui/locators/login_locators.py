from selenium.webdriver.common.by import By

USERNAME_INPUT = (By.ID, "user-name")
PASSWORDS_INPUT = (By.ID, "password")
LOGIN_BUTTON = (By.ID, "login-button")
ERROR_MESSAGE = (By.XPATH, "//div[@class='error-message-container error']")
