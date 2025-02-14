import time
import pytest
from pages.main_login_page import MainLoginPage

class TestMainLogin:
    @pytest.mark.smoke
    def test_login_successful_C01(self):
        login_page = MainLoginPage()
        login_page.login("standard_user", "secret_sauce")
        login_page.click_login_button()
        assert login_page.is_login_successful(), "Login failed"
        time.sleep(3)
        #login_page.close()

    @pytest.mark.smoke
    def test_login_wrong_password_C02(self):
        login_page = MainLoginPage()
        login_page.login("standard_user", "wrong_password")
        login_page.click_login_button()
        login_page.login_error_message()

    @pytest.mark.smoke
    def test_login_wrong_username_C03(self):
        login_page = MainLoginPage()
        login_page.login("wrong_username", "secret_sauce")
        login_page.click_login_button()
        login_page.login_error_message()