from selenium.webdriver.common.by import By

class MainLoginLocators:
    """
    Locators for the main login page.
    """

    USER_NAME_FIELD = (By.XPATH, "//input[@id='user-name']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")
    LOGIN_ERROR =(By.XPATH, "//*[contains(text(),'Username and password do not match')]")