def pytest_addoption(parser):
    """Allows to choose the browser with a tag from the command line"""
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name (chrome/firefox/edge)")
