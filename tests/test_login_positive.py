import pytest
from page_objects.account_dashboard_page import AccountDashboardPage
from page_objects.forgot_password_page import ForgotPasswordPage

from page_objects.login_page import LoginPage
from page_objects.logout_page import LogoutPage


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_login_successfully(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.type_user_credentials("johndoe1234", "Password123")
        login_page.click_login_button()
        account_dashboard_page = AccountDashboardPage(driver)
        assert login_page.current_url == account_dashboard_page.get_url(), "Actual URL is not the same as expected."
        assert account_dashboard_page.get_header_text() == "MY ACCOUNT", "The header text is not the expected."
    
    @pytest.mark.login
    @pytest.mark.positive
    def test_reset_password_successfully(self, driver):
        login_page = LoginPage(driver)
        login_page.open()  
        login_page.click_forgot_password()
        forgot_password_page = ForgotPasswordPage(driver)
        assert login_page.current_url == forgot_password_page.get_url(), "Actual URL is not the same as expected."
        forgot_password_page.type_user_credentials("johndoe1234", "johndoe@email.com")
        forgot_password_page.click_continue_button()
        assert login_page.current_url == login_page.get_url(), "Actual URL is not the same as expected."
        assert login_page.get_success_message() == "×\nSuccess: Password reset link has been sent to your e-mail address."
    
    @pytest.mark.login
    @pytest.mark.positive
    def test_logoff_successfully(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.type_user_credentials("johndoe1234", "Password123")
        login_page.click_login_button()
        account_dashboard_page = AccountDashboardPage(driver)
        account_dashboard_page.click_logoff_button()
        logout_page = LogoutPage(driver)
        assert account_dashboard_page.current_url == logout_page.get_url(), "Actual URL is not the same as expected."