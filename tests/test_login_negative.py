import pytest
from page_objects.account_dashboard_page import AccountDashboardPage

from page_objects.login_page import LoginPage


class TestNegativeScenarios:
    
    @pytest.mark.login
    @pytest.mark.negative
    def test_login_incorrect_username(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.type_user_credentials("johndoe123", "Password123")
        login_page.click_login_button()
        error_message = login_page.get_error_message()
        assert error_message == "×\nError: Incorrect login or password provided.", "It's not the expected error message."
    
    @pytest.mark.login
    @pytest.mark.negative
    def test_login_incorrect_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.type_user_credentials("johndoe1234", "Password12")
        login_page.click_login_button()
        error_message = login_page.get_error_message()
        assert error_message == "×\nError: Incorrect login or password provided.", "It's not the expected error message."    