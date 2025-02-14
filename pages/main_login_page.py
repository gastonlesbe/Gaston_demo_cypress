from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from config import Config
from locators.main_login_locators import MainLoginLocators

class MainLoginPage:
    def __init__(self):
        self.driver = Config.get_driver()
        self.driver.get(Config.BASE_URL) 
    
    def enter_username(self, username):
        try:
            self.driver.find_element(*MainLoginLocators.USER_NAME_FIELD).send_keys(username)
        except NoSuchElementException as e:
            print(f"Error entering username: {e}")
    
    def enter_password(self, password):
        try:
            self.driver.find_element(*MainLoginLocators.PASSWORD_FIELD).send_keys(password)
        except NoSuchElementException as e:
            print(f"Error entering password: {e}")
    
    def click_login_button(self):
        try:
            self.driver.find_element(*MainLoginLocators.LOGIN_BUTTON).click()
        except NoSuchElementException as e:
            print(f"Error clicking login button: {e}")
    
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def login_error_message(self):
        try:
            return self.driver.find_element(*MainLoginLocators.LOGIN_ERROR).text
        except NoSuchElementException as e:
            print(f"Error getting login error message: {e}")
    
    def is_login_successful(self):
        return "inventory" in self.driver.current_url
    
    def is_login_failed(self):
        return "error" in self.driver.current_url

    def close(self):
        self.driver.quit()