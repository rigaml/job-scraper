from typing import Optional
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager


class ScrapperContextManager():
    """
    A context manager for setting up and managing a web scraping session.

    This class sets up a Chrome WebDriver instance with the specified options,
    navigates to the provided URL, and manages the lifetime of the WebDriver session.
    The `__enter__` method initializes the WebDriver session, and the `__exit__`
    method quits the WebDriver session when the context is exited.

    Args:
        url (str): The URL to navigate to within the context.
        show_browser (bool): Whether to show the Chrome browser window (True) or run in headless mode (False).

    Attributes:
        url (str): The URL to navigate to within the context.
        show_browser (bool): Whether to show the Chrome browser window or run in headless mode.
        driver (WebDriver): The Chrome WebDriver instance.
    """

    def __init__(self, url: str, show_browser: bool):
        """
        Initialize the instance.

        Args:
            url (str): The URL to navigate.
            show_browser (bool): Whether to show the Chrome browser window (True) or run in headless mode (False). 
            Keep in mind that to show the browser(True), environment that runs the application should have a graphical interface.
        """
        self.url = url
        self.show_browser = show_browser
        self.driver: webdriver.Chrome

    def __enter__(self):
        """Set up the Chrome WebDriver session and navigate to the specified URL."""
        chrome_options = Options()

        if not self.show_browser:
            # Runs Chrome in headless mode.
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--window-size=2560,1080")
            chrome_options.add_argument("--enable-javascript")
            chrome_options.add_argument("--disable-gpu")
            # chrome_options.add_argument("--no-sandbox")
            # chrome_options.add_argument("--disable-dev-shm-usage")
            # service = Service("/usr/bin/chromedriver")

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

        # Navigate to the page
        self.driver.get(self.url)

        return self

    def __exit__(self, type_, value, traceback):
        """
        Quit the Chrome WebDriver session when the context is exited.

        Args:
            exc_type (type): The type of the exception raised, or None if no exception occurred.
            exc_value (Exception): The instance of the exception raised, or None if no exception occurred.
            traceback (traceback): The traceback object associated with the exception, or None if no exception occurred.
        """
        self.driver.quit()
