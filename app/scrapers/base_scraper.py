from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

class BaseScrapper():
    def __init__(self, url: str, show_browser: bool):
        self.url= url
        self.show_browser= show_browser

    def __enter__(self):
        chrome_options = Options()
        if not self.show_browser:
            # Runs Chrome in headless mode.
            chrome_options.add_argument("--headless")

        # Setup Selenium with ChromeDriver
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

        # Navigate to the page
        self.driver.get(self.url)

        return self

    def __exit__(self, type_, value, traceback):
        self.driver.quit()