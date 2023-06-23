import pytest
from page_objects.account_created_page import AccountCreatedPage
from page_objects.register_account_page import RegisterAccountPage
from test_data.register_data import account_info


class TestPositiveScenarios:

    @pytest.mark.register
    @pytest.mark.debug
    @pytest.mark.parametrize('first_name, last_name, email, telephone, fax, company, address1, address2, city, region_state, zip_code, country, login_name, password, password_confirm, subscribe, privacy_policy', [account_info.values()])
    def test_valid_input(self, driver, first_name, last_name, email, telephone, fax, company, address1, address2, city, region_state, zip_code, country, login_name, password, password_confirm, subscribe, privacy_policy):
        register_page = RegisterAccountPage(driver)
        register_page.open()
        register_page.type_form(first_name, last_name, email, telephone, fax, company, address1, address2, city, region_state, zip_code, country, login_name, password, password_confirm, subscribe, privacy_policy)
        account_created_page = AccountCreatedPage(driver)
        assert register_page.current_url == account_created_page.expected_url, "Actual URL is not the same as expected."
        