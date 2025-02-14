
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Config:
    """
    Configuration settings for the tests.
    """
    BASE_URL = "https://www.saucedemo.com/"  # Replace with your actual base URL

    @staticmethod
    def get_driver():
        """
        Returns the webdriver instance.
        """
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options

        chrome_options = Options()
        # Add your desired Chrome options here
        #chrome_options.add_argument("--headless") 
        chrome_options.add_argument("--start-maximized")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver