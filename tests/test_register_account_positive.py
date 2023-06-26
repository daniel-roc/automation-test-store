import pytest
from page_objects.account_created_page import AccountCreatedPage
from page_objects.register_account_page import RegisterAccountPage
from test_data.account_data import account_info


class TestPositiveScenarios:

    # 1- Test case: Valid input

    @pytest.mark.register
    @pytest.mark.debug
    @pytest.mark.parametrize('first_name, last_name, telephone, fax, company, address1, address2, city, region_state, zip_code, country, subscribe, privacy_policy', [account_info.values()])
    def test_valid_input(self, driver, faker, first_name, last_name, telephone, fax, company, address1, address2, city, region_state, zip_code, country, subscribe, privacy_policy):
        register_page = RegisterAccountPage(driver)
        register_page.open()
        username = faker.user_name()
        password = faker.password()
        email = faker.email()
        register_page.type_form(first_name, last_name, email, telephone, fax, company, address1, address2, city, region_state, zip_code, country, username, password, password, subscribe, privacy_policy)
        account_created_page = AccountCreatedPage(driver)
        assert register_page.current_url == account_created_page.expected_url, "Actual URL is not the same as expected."
        