import pytest
from ui.utils.browser import Browser
import datetime


@pytest.fixture(scope="session")
def browser(request):
    """Sets ui tests by opening the browser and closing it"""
    driver = Browser.get_driver(request.config.getoption("--browser"))
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_exception_interact(report):
    """Saves a screenshots when a test fails with unique name"""
    if report.failed:
        driver = Browser.get_driver()
        date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        driver.save_screenshot(f"screenshots/{date}.png")
