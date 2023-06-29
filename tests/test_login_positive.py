import pytest
from page_objects.account_dashboard_page import AccountDashboardPage

from page_objects.login_page import LoginPage


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