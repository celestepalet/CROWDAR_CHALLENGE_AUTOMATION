from selenium import webdriver


class Browser:
    """A class that provides a browser instance"""
    _driver = None
    _driver_options = {"edge": {"driver": webdriver.Edge, "options": webdriver.EdgeOptions()},
                      "chrome": {"driver": webdriver.Chrome, "options": webdriver.ChromeOptions()},
                      "firefox": {"driver": webdriver.Firefox, "options": webdriver.FirefoxOptions()}}

    @classmethod
    def get_driver(cls, browser="chrome"):
        """ Returns an instance of the webdriver for the selected browser"""
        if cls._driver is None:
            cls._driver = cls.create_instance(browser)
        return cls._driver

    @classmethod
    def create_instance(cls, browser="chrome"):
        """Creates an WebDriver customized instance"""
        if browser.lower() in cls._driver_options:
            browser_config = cls._driver_options.get(browser)
            driver_class = browser_config.get("driver")
            options = browser_config.get("options")
        else:
            raise ValueError(f"Unsupported browser: {browser}")
        driver = driver_class(options=options)
        cls._driver = driver
        return cls._driver
