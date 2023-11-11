from selenium.webdriver.common.by import By


def locator_handler(locator, index='1'):
    """Returns the by xpath locator with the required index"""
    locator = f"{locator}[{index}]"
    locator_by_xpath = (By.XPATH, locator)
    return locator_by_xpath
