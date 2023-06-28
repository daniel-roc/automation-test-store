import pytest
from page_objects.account_created_page import AccountCreatedPage
from page_objects.register_account_page import RegisterAccountPage


class TestPositiveScenarios:

    # 1- Test case: Valid input
    @pytest.mark.register
    @pytest.mark.positive
    def test_valid_input(self, driver):
        register_page = RegisterAccountPage(driver)
        register_page.open()
        register_page.type_all_fields()
        register_page.click_continue_button()
        account_created_page = AccountCreatedPage(driver)
        assert register_page.current_url == account_created_page.expected_url, "Actual URL is not the same as expected."


    # 2- Test case: Minimum input required
    @pytest.mark.register
    @pytest.mark.positive
    def test_minimun_input_required(self, driver):
        register_page = RegisterAccountPage(driver)
        register_page.open()
        register_page.type_required_fields()
        register_page.click_continue_button()
        account_created_page = AccountCreatedPage(driver)
        assert register_page.current_url == account_created_page.expected_url, "Actual URL is not the same as expected."        

        