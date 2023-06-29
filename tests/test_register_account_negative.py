import pytest

from page_objects.register_account_page import RegisterAccountPage

class TestNegativeScenarios:

    # 1 - Test Case: Privacy Police Unchecked
    @pytest.mark.register
    @pytest.mark.negative
    def test_privacy_police_unchecked(self, driver):
        register_page = RegisterAccountPage(driver)
        register_page.open()
        register_page.type_required_fields()
        register_page.check_privacy_police()
        register_page.click_continue_button()
        error_message = register_page.reformat_text(register_page.get_error_message())
        expected_message = register_page.reformat_text("Error: You must agree to the Privacy Policy!")
        assert error_message == expected_message, "It's not the expected error message."

    # 2- Test case: Invalid e-mail format
    @pytest.mark.register
    @pytest.mark.negative
    @pytest.mark.debug
    def test_invalid_email_format(self, driver):
        register_page = RegisterAccountPage(driver)
        register_page.open()
        register_page.type_required_fields()
        register_page.set_email("invalidformat@")
        register_page.click_continue_button()
        error_message = register_page.reformat_text(register_page.get_error_message())
        expected_message = register_page.reformat_text("Email Address does not appear to be valid!")
        assert error_message == expected_message, "It's not the expected error message."